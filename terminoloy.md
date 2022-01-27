# Binary
A binary executable file is a file in a machine language for a specific processor. 
Binary executable code that is represented in specific processor instructions. 
These instructions are executed by a processor directly.
Most of OS files are binary files.

There also exist binary data files - files that contain certain binary structures. These files are usually created by binary executable files and are used by them to store specific data.


# UUID
A **universally unique identifier** (**UUID**) is a 128-bit label used for information in computer systems.

The term *globally unique identifier* (**GUID**) is also used.

# TLS
Transport layer Security (TLS) encrypts data sent over the Internet to ensure that eavesdroppers and hackers are unable to se what you transmit which is particularly useful for private and sensitive information such as passwords, credit card numbers, and personal correspondence.

## What is TLS?
TLS is a cryptographic protocol that provides end-to-end security of data sent between applications over the Internet.

TLS evolved from **Secure Socket Layers** (SSL).

It should be noted that TLS does not sexure data on end systems. It simply ensures the secure delivery of data over the Internet, avoiding possible eavesdropping and/or alteration of the content.

TLS is normally implemented on top of TCP in order to encrypt Application Layer protocols such as HTTP, FTP, SMTP and IMAP, although it can also be implemented on UDP, DCCP and SCTP as well. This is known as Datagram Transport Layer Security (DTLS).

## How does TLS work?
TLS uses a combination of symmetric and asymmetric cryptography, as this provides a god compromise between performance and security when transimitting data securely.

With symmetric cryptography, data is encrypted and decrypted with a secret key known to both sender and recipient.

Asymmetric cryptography uses key pairs - a public key, and a private key. The public key is mathematically related to the private key, but given sufficient key length, it is computationally impractical to derive the private key from the public key.

TLS uses asymmetric cryptography for securely generating and exchanging a session key. The session key is then used for encrypting the data transmitted by one party, and for decrypting the data received at the other end. Once the session is over, the session key is discarded.


## Note
HTTPS is an implementation of TLS encryption on top of the HTTP protocol, which is used by all websites as well as some other web services. Any websites that uses HTTPS is therefore employing TLS encryption.