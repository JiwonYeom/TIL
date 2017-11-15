## Client Server Communication
reference: https://classroom.udacity.com/courses/ud897/lessons/8162118632/concepts/81883228140923

```
# HTTP REQUEST 

// [METHOD(VERB)] [path] [version]
GET /pictures/kitty.jpg HTTP/1.1

--- headers ---
Host: www.google.com    // required
User-Agent: Mozilla/5.0
Connection: Keep-alive
Accept : text/html
...
```

```
# HTTP Response
HTTP/1.1 200 OK
Content-Length: 16824   //required
```

### Verbs

- HEAD : gets headers of the file without getting the content. Check cache / enough space to take in the file

### Netcat
- `nc http://netcat.127.0.0.1.xip.io 8080`
```
[verb] / [protocol]
Host: [Host address]
[Header Name]: [value]
```

### Head of Line Blocking
- request that takes a long time makes rest of the request wait for a long time, causing the whole process to lag.
- In order to solve this, another connection must be opened and that is costly.

- every time browser wants to make a request, it needs TCP handshake
- HTTP2 concept of `keep-alive` comes in
- Without `Connection : keep-alive` header, connection drops after a response.

### HTTPS
- TLS : Encrypts data in a way that only intended targets can read the data.
    - chain of trust : server identificates itself with both data about itself and fingerprint of the encryption key
    - encryption: public key & private key. Asymmetric encryption = public key encryption
    - hashing: transforming data into short representative strings.
        - must be impossible to re-convert
        - should never be identical
- Why a certificate?
    - to have proof that the document was seen / created by the entity.
    - server signs a document & encrypts it with private key.
    - But if the data is large, encrypting the whole thing can take a long time.
    - Instead of encrypting the whole data, it is hashed first and then the hash is encrypted.
    - browser needs to only confirm if the data is unchanged.
    - If the hash is not matched = invalid signature
- TLS process step-by-step
    - server sends ou the the certificate (public key, domain, and signature)
    - browsers have their public key, so they can easily check if the signature is valid.
- Mixed content: when you open a website that is supposed to be delivered through HTTPS but resources are from non-TLS secured origins. (Ex.jquery from non-TLS CDN)

### HTTP2
- request numbers have been increasing fast in past years.
- Headers tend to be repetitive. HTTP2 provides header compression.b 
- HTTP2 also supports better security 
- How?
    - Give up human-readable headers.
    - Multiplexing : combining multiple signals into one. Reducing 6 connections to one.
        - Connections are now perceived as `streams`. All streams share single connection.
        - Streams split up into frames and optimizes usage of the connection.
        - Uncompressed header data -> compressed with key.zip + All stremas share the compressor 
        - Compressor will recognize a header that has already been sent before and sends a reference instead.
        - ex) Cookies.

### Transition to HTTP2
- Minifying is okay, but concatenating / combining files into one should be considered carefully since it will make caching inefficient.

### Security
- Origins: JavaScripts are not allowed to access the data of any other origin than its own.
    - Data Scheme : HTTPS
    - Hostname: www.udacity.com
    - Port: 443
- do not mix HTTP and HTTPS URLs
- Cross-Origin Fetch Requests
    - Might be able to fetch responses, but won't be able to read them
- Browser-enforced
- CORS: Cross Origin Resource Sharing
    - JSONP: returns a script containing the data. JSONP APIs expect to accept **function name** as its query parameter.
    - CORS headers allow servers to specify set of allowed origins. If the request referrer header is on the allow list, it can read and use the data.
    - But by the time the server sends back the headers, reques would have already fired.
    - This can be a problem with destructive operations, since too late to ignore the request.
    - preflight Request: OPTIONS method allows to check and allow the browser to check what is allowed and what is not. 
    - image tags or forms will not be preflighted.
- CSRF : Cross-site request forgery
- XSS : Cross-site scripting
    - Make sure user inputs aren'ts destructive.