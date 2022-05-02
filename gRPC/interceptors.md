# What are gRPC Interceptors?
Components of a gRPC application that allows us to interact with a proto message or context either before - or after - it is sent or received by the client or server.

- modify each request before it is sent
- on the server side, we can intercept the message before the actual function call is executed.


1. Tracing: viewing the flow of data through an application from request to response.
2. Authorization

# Types of Interceptor

## Client Unary Interceptor
Executed on the client before the singular request is made to a function on the server side.

## Server Unary Interceptor
Executed server side when a singular request is received from a client.

## Client Stream Interceptor
Intercepting before sending each chunk of message

## Server Stream Interceptor
Intercepting after receiving each chunk of message