# Basics of HTTP Header and Body
### HTTP basics
HTTP allows two types of messages to be transferred between `client` and `server`. Both HTTP Request and HTTP Response have common format, and contains `HTTP Header` and `HTTP Body`.

### HTTP Header
* Contains info about **HTTP Body** and **Request/Response**.
* In name-value pair.

### Types of HTTP Headers
3 parts.
1. General Header
2. Request/Response Header
3. Entity Header

#### 1.General Header
General info - date, time of the message generated, etc. This header is common to both Request and Response.

> Cache-Control, Connection, Date, Pragma, Trailer, Transfer-Enco, Upgrade, Via, Warning

#### 2.Request/Response Headers
Presents when you make a request to the server or server sends a response back to the client.
> Request Header : Accept, Accept-Charset, Accept-Encoding, Accept-Language, Authorization, Expect, From, Host, If-Match, If-Modified-Since, If-None-Match, If-Range, If-Unmodified-Since, Max-Forwards, Proxy-Authorization, Range, Referer, TE, User-Agent

#### 3.Entity Header
Contains info about actual message or HTTP body being sent. Content length, language of content, encoding, expiration date...
>Allow, Content-Encoding, Content-Language, Content-Length, Content-Location, Content-MD5, Content-Range, Content-Type, Expires, Last-Modified, extension-header

*Note: Since entity header is related with the body message, body formats, specifications, length and others must fit with what is defiend with entity header (I experienced a full hour jam because of this)
