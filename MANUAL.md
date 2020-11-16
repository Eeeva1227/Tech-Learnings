## design choice
- every client keeps track of a map where `key=pathname` and `val=metadata`.
The metadata at client side consists of t
1. two struct fuse_file_info pointer (one for server and the other for client)
2. `Tc` for current file 
- t_client and t_server are tracked via last_modfied time of cached file and server file

### copying a file from server to client
When clients open a file, a fresh copy will always be transferred from server to client.
With read calls - read() and getattr(), if the file is opened for read-only and the freshness check fails, current client will fetch a fresh copy from server to client.

The functionality is implemented in a helper function `fetch_file()`, and it invokes a rpc call `lock()` to 
acquire the read_lock.

For fetching the file, client read data from server file via read rpc call, and write to local cached file via local file system, repeat the read and write process until the end of file is reached.

After the fetching finishes, Tc will be updated to curent time. The client then fetches t_server via a getattr rpc call, and then invoke a sys call `utimensat` to upate t_client to t_server.

The client then invokes a rpc call `unlock()` to 
release the lock with the previous mode.

### copying a file from the client to server
The writer client will periodically write back to server, and will flush file when the client closes the file.

When a file that was opened for write is closed, the cached file will be transfered back to server from client.
With write calls, i.e. write(), truncate(), utimens() and mknod(), the cached file will be transfered back to server if the freshness check fails after the write is done.

The functionality is implemented in a helper function `flush_file()`, and it invokes a rpc call `lock()` to 
acquire the write_lock.

For flushing, the client read from local file and write to server via a write rpc call, repeat the process until end of file is reached in local cached file.

After the flushing finishes, Tc will be updated to curent time. The client then fetches t_client via system call `getattr` and then update t_server to t_client via a utimens rpc call.

The client then invokes a rpc call `unlock()` to 
release the lock with the previous mode.


### atomic transfering

The transfering is guaranteened to be atomic with the helper of rw_lock.
If a client attempts to transfer a file for read only, the client invokes a rpc call `lock()` to 
acquire the read_lock.
The server then invokes a function `watdfs_lock()` to acquire the rw_lock for current file.
After the transfering finishes, the client invokes a rpc call `unlock()` to 
release the grabbed lock, and the server then invokes a function `watdfs_unlock()` to release the
acquired lock.

If a client attempts to transfer a file back for write, the client invokes a rpc call `lock()` to 
acquire the write_lock.
The server then invokes a function `watdfs_lock()` to acquire the rw_lock for current file.
After the transfering finishes, the client invokes a rpc call `unlock()` to 
release the grabbed lock, and the server then invokes a function `watdfs_unlock()` to release the
acquired lock.

With the help of rw_lock, a file can be transferred from a server to multiple clients in parallel, as multiple read_lock can be grabbed by concurrent clients.
However, only one single writer client can grab the write_lock at one time, therefore writing back the file to server is mutually exclusive to all other reads and writes.

### cache invalidation testing
Cache freshness will be check for both read calls and write calls.

--- read calls, freshness check fails
1. open a file for read only
2. open the same file from another client for write
3. writer sleeps for cache_interval, and write some new data to the file. the file should be flushed back and t_server should be upated. 
4. sleep the read client for 3 * cache_interval, and the read client reads the file via a read() call. The freshness check for read client should fail, and a new file should be fetched from server, the reader should read new data from step 3. Tc and t_client should be updated.
5. check Tc, t_client and t_server at both clients and the server.

--- read calls, freshness check passes
1. open a file for read only
2. open the same file from another client for write
3. writer sleep for cache_interval, and write some new data to the file. t_server should be upated.
4. the read client reads the file via a read() call before cache times out (set cache_interval to a large value). The freshness check for read client passes, the reader will not read new data from step 3. Tc and t_client should not be updated.

--- write calls, freshness check fails
1. a write client opens a file for write
2. writer sleeps for cache_interval, and write some new data to the file. the file should be flushed back and t_server should be upated. 

--- write calls, freshness check passed
1. a write client opens a file for write
2. writer immediately writes some new data to the file. the file should not be flushed back and t_server should not be upated. 
3. when the file is closed, the file will be flushed back, Tc and t_server will be updated.


### mutual exclusion at client
The filedata map stored in userdata has `key=pathname` and `val=metadata` functions as global variables.
When a file is opened, an entry will be emplaced into the map for current filename.
When a file is closed, the corresponding entry will be removed from the map.
Therefore, if a client attempts to open a file that is already opened, an entry will be found in the map, and it then return the error -EMFILE.

### mutual exclusion at server
The mutual exclusion at server forces that only a single writer at a time.
The server keeps track of a map `files` where `key=pathname` and `val=metadata`.
The file metadata consists of
- a boolean value `iswrite` indicates whether the file is currently opened by a writer (i.e has write access)
- a rw_lock pointer pointing to the rw_Lock for current file
- a mutex lock pointer pointing to the mutex lock that guards the bool var `iswrite`

When `open()` is called at server via a rpc call from client, the server checks whether the
filename is in the map `files`
- if it is not in `files`, the server creates the metadata for current file. If current file has write access, set
`iswrite` to `true`, and `false` otherwise. Besides, create and init the mutex lock and rw_lock for current file.

- if it is in `files`, which means the locks have already been initialized for current filename.
If the current client attempts to open the file for write, if the bool value `iswrite` for current file's metadata
is `true`, the function set return code as `-EACCES`. Otherwise, the client can successfully open the file
and then set `iswrite` for current file to `true`.
Otherwise, if the client only attempts to read or `iswrite` is set to `false`,

When `close()` is called for a file and the file was opened for write, which means `iswrite` is currently set to `true`, sever set `iswrite` in current file's metadata to `false` so that other writers can then open the file for write access.

## functionalities that have not been implemented
When mutliple clients attempt to open the same file for write, one client is expected to get EACCES on double file open for write, but this functionality does not work at this point.
The functionality is already implemented with rw_lock and mutex_lock, however, one test fails and need further debug.

## error codes
The following error codes are returned
1. ENOENT - when cient attempts to open a file that does not exist
2. EACCES - returned when the client attempts to invoke write calls on a file that was opened for read only
3. EMFILE - returned when the client attempts to open a file that was already opened but not yet closed.
4. EINVAL - returned when rpc call fails

## testing

--- Basic functionality test
1. open a non-existing file without O_CREAT, the operation fails with -ENOENT
2. open a non-existing file with O_CREAT and close it, the operations succeed, and a cache file is
created in the cache directory. Testing with other flags with O_CREAT, i.e. O_CREAT | O_RDONLY, O_CREAT | O_WRONLY and O_CREAT | O_WRONLY, read/write to the file, and close the file.
3. open an existing file with O_RDONLY, read it and then close, the operations succeed, and a cache file is
created in the cache directory. Test with freshness check fails - fetch the file, and freshness check passes - read local caching file directly.
4. open an existing file with O_RDONLY but write to it, the operation fails with -EACCES
5. truncate a file that is not opened yet, the file sould be opened, fetched, truncated locally, flushed to server and closed.
6. truncate a file that is already opened, the file sould be truncated, and closed. Test with freshness check fails - flush the file, and freshness check passes - simply return.
7. mknod is called with a file that is non-existing yet, the file will be created.
8. mknod is called with a file with an existing file, the operation should fail and return -EMFILE.
9. utimens is called with a file that is not opened yet, the file sould be opened, fetched, utimensat locally, flushed to server and closed.
10. utimens is called with a file that is already opened, the operation is performed locally (utimensat), and closed. Test with freshness check fails - flush the file, and freshness check passes - simply return.
11. getattr of a file that is not opened yet, the file sould be opened, fetched, truncated locally, flushed to server and closed.
12. getattr of a file that is already opened yet. If not in write mode and freshness check failed, fetch the file and gettattr of the fetched file locally. Otherwise, getattr of the local cached file.
13. opening a file with different mode testing, i.e. O_APPEND, O_EXCL (O_CREAT, O_RDONLY, O_WRONLY, and O_RDWR are tested in other tests)
14. open a file for read only, call fsync(), test it in the cases with other writer (the file is already opened for write), the opreation should fail with -EACCESS. Testing without a current writer will succeed.
15. open a file for write, call fsync(), test it in the cases with/withou other writer both succeed.

--- Concurrency test
1. atomic file transfering - a write client and two read clients tries to open the same file at the same time, after the write client finishes writing, the two read clients either read the original data (withouout write client's writes) or the new data(with the write client writes)
2. atomic file transfering - three read clients tries to open the same file at the same time, all read clients succeed and start fetching file immediately, i,e. they should not be blocked.
3. mutual exclusion at server - one write client attempts to open a file for write when there is already a write client opened it (and not closed yet), the write client second write client should get error -EACCES.
4.  mutual exclusion at server - one write client attempts to open a file for write and close it. Another write client attempts to open it afterwards, both write clients should succeed.
5. mutual exclusion at client - a client attempts to open a file again before it closes it, the operation should fail with -EMFILE.


