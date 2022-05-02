# Domain Name
- A string of text that maps to a numeric IP address.
- Domain names are managed by domain *registries*, which delegates the reservastion of domain names toregistrars..
- Anyone who wants to create a website can register a domain name with a registrar.

# URL
- A **uniform resource locator**, sometimes called a web address
- Contains the domain name of a site as well as other information, including the transfer protocol and the path.

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

## TLS Certificate
Digital certificates, also known as identity certificate or **public key certificates**, are digital files that are used to certify the ownership of a public key.

TLS certificates are a type pf digital certificate, issed by a Certificate Authority (CA). The CA signs the certificate, certifying that they have  verified that it belongs to the owners of the domain name which is the subject of the certificate.

TLS certificates usually contain the following information:
- The subject domain name
- The subject organization
- The name of the issuing CA
- Additional or alternative subject domain names, including subdomains, if any
- Issue data
- Expiry date
- The public key (The private key, however, is a secret.)
- The digital signature by the CA

## How does TLS certificate work?
When a user tries to connect to a server, the server sends them its TLS certificate.

The user then verifies the server's certificate using CA certificate that are present on the user's device to establish a secure connection.

This verification process uses publick key cryptography, such as RSA, or ECC, to prove the CA signed the certificate.




## Note
HTTPS is an implementation of TLS encryption on top of the HTTP protocol, which is used by all websites as well as some other web services. Any websites that uses HTTPS is therefore employing TLS encryption.




# DNS
The **Domain Name System** (**DNS**) is the phonebook of the Internet.

1. Human access information online through *domain names*, like *nytimes.com* or *espn.com*.

2. Web browsers interact through **Internet Protocol** (**IP**) addresses.

3. DNS translates domain name to IP addresses so browers can load internet resources.

Each device connected to the Internet has a uniqur IP address which other machines use to find. DNS servers eliminates the need for humans to memorize IP addresses such as 192.168.1.1(ipv4).

## DNS Caching
DNS caching involves storing data closer to the requesting client so that the DNS query can be resolved earlier and additional queries further down the DNS lookup chain can be avoided, thereby improving load times and reducing bandwidth/CPU consumption.

DNS data can be cached in a variety of locations, each of which will store DNS records for a set amount of time determined by a time-to-live (TTL).

