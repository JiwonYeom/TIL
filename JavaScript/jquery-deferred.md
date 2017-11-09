## jQuery `deferred`

(in progress)

- What is jQuery `deferred` object?
    - works like a promise. According to official documents: can register multiple callbacks into callback queues, invoke callback queues, and relay the success or failure state of any synchronous or asynchronous function.

- Why did I need this?
    - I was working on `aws cognito` integration with JavaScript SDK. When I make API call of the Cognito method, it will usually take few seconds. I decided to assort all the functions that connect with `AWS Cognito` into a separate file, and call them in different occations when I need them.
    - The website client was written in `jQuery`, so I needed a `Promise object` in jQuery. I did not want to rely on something like `setInterval()`.

```JavaScript
// AWS Cognito API callers
function getUserData(deferred){
    
}

```


```JavaScript
// page needs user attributes


```
