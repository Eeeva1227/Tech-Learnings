# Secure Shell (SSH)

## What is SSH?
SSH, also known as Secure Shell or Secure Socket Shell, is a **network protocol** that gives users, particular system administrators, a secure way to access a computer over an unsecured network.

SSH also refers to **the suite of utilities that implement the SSH prototcol**. 

Secure Shell provides strong password authentication and public key authentication, as well as encrypted data communications between two computers connecting over an open network, such as the internet.

In addition to strong encryption, SSH is used by network administrators to manage systems and applications remotely, enabling them to log in to another computer over a network, execute commands and move files from one computer to another.

SSH can also be used to create secure tunnels for other application protocols.


## How does SSH work?

The most basic use of SSH is to connect to a remote host for a terminal session.
The form of the command is:
```
ssh UserName@SSHserver.example.com
```

This command will cause the client to attempt to connect to the server named `SSHserver.example.come` using the user ID `UserName`.


## What is SSH used for?
SSH connections have been used to secure many different types of communications between a local machine and a remote host, inluding secure remote access to resources, remote execution of commands, delivery of software patches, and updates and other administrative or management tasks.

All SSH traffic is encrypted. Whether users are transferring a file, browsing the web or running a command, their actions are private.


## Secure Shell capabilities

## SSH Commands
- `ssh-keygen` is a program to **create a new authentication key pair for SSH**, which can be used to automate logins, to implement SSO and to authenticate hosts.

- `scp` is a program used for copying files from one computer to another and is an SSH-secured version of `rcp`.

- `sftp` is a program used to copy files from one computer to another and is an SSH-secured version of `ftp`, the original File Transfer Protocol.





## References
https://www.techtarget.com/searchsecurity/definition/Secure-Shell 
