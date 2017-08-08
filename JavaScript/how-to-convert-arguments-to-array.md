# How to convert arguments into array

Use `Array.prototype`.
```JavaScript
function testFn(arg0, arg1, arg2, arg3){
    var args = Array.prototype.slice.call(arguments);
    // this will put all arguments into an array.
    console.log(args); //[arg0, arg1, arg2, arg3]
}
```
