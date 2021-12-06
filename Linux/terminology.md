# Environment Variables
Environment variables are global system variables accessible by all the processes/users running under the OS, such as Windows, macOS and Linux.
Environment variables are useful to store system-wide values, for examples,

- `PATH` the most frequently-used environment variable, which stores a list of directions to search for executable programs.

- `OS` the operating system

## macOS/Linux Environment Variables
Environment variables in macOS/Unixes are *case-sensitive*.

Global environment variables (available to ALL processes) are named in uppercase, with words joined with underscore(`_`), e.g. `JAVE_HOME`. 

Local variables (available to the current process only) are in lowercase. The recommended way is by editing you **._bash_profile** file. 
This file is read and the commands in it executed by **Bash** every time you log in to the system.
The file is specific to your user so it won't affect other users on the same system.

### Using Environment Variables in Bash Shell
Most of the Unixes (Ubuntu/macOS) use the so-called Bash shell.


### Permanently setting an Environment Variable in Bash Shell


# References
https://medium.com/geekculture/path-macos-best-practice-for-path-environment-variables-on-mac-os-35ec4076a486 