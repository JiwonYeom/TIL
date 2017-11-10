## jQuery `deferred`

(in progress)

- What is jQuery `deferred` object?
    - works like a promise. According to official documents: can register multiple callbacks into callback queues, invoke callback queues, and relay the success or failure state of any synchronous or asynchronous function.

- Why did I need this?
    - I was working on `aws cognito` integration with JavaScript SDK. When I make API call of the Cognito method, it will usually take few seconds. I decided to assort all the functions that connect with `AWS Cognito` into a separate file, and call them in different occations when I need them.
    - The website client was written in `jQuery`, so I needed a `Promise object` in jQuery. I did not want to rely on something like `setInterval()`.

```JavaScript
// create user pool
function createUserPool(){
    var poolData = {
        UserPoolId : 'ap-northeast-2_VtEfTuELM',
        ClientId : '6h3v1q779m5lpgr2m1cnt2vvhi'
    };
    var userPool = new AWSCognito.CognitoIdentityServiceProvider.CognitoUserPool(poolData);
    return userPool;
}

// AWS Cognito API callers
function getUserData(deferred){
    var userPool = createUserPool();
    var cognitoUser = userPool.getCurrentUser();
    // getSesssion() lets you confirm authorization
    cognitoUser.getSession(function(err, result){
        if(result){
            console.log('session available');
            // actual function call
            cognitoUser.getUserAttributes(function(err, result) {
                if (err) {
                    // fail if error
                    deferred.reject(err);
                }else{
                    // success if no error
                    deferred.resolve(result);
                }
                // return deferred
                return deferred.promise();
            });
        }
    });
}

```

```JavaScript
// page needs user attributes

// declare jQuery deferred object
var userDataPromise = $.Deferred();
// pass it to the function
getUserData(userDataPromise);
// when data is ready
$.when(userDataPromise).then(function(data){
    data.forEach(function(val,key){
        if(val.Name == 'name'){
            $('.name').text(val.Value);
        }
    })
});
```

- Since two functions are in different file & curretly the deferred object is not a global variable, I decided to pass it as a parameter to the function that calls aws cognito APIs. 
I tried different methods too where I declare deferred object within the `getUserData()` or allocate return value from `getUserData()` into a variable then pass it to `$.when()`, but most of them did not work because `$.when()` or `done()` would fire before the aws cognito APIs have returned their result values.