# Closure in JS
This is a brief explanation for closure in js.
>Closure is a function that returns a function.

Basic Usage:
```
var saveFn = function (val) {
    return function () {
        return val;
    };
};

var retriveFn = saveFn(100);

console.log(retrieveFn());
//100
```
An argument 100 has been passed to closure, `saveFn`.

The function `retrieveFn` can now return values returned by `saveFn`, but it cannot change the entered value(100).

We can use this as the following:

```
var adder = function (a) {
    return function (b) {
        return a + b;
    };
};

var hi = adder('Hi ');
console.log(hi('Jamie')); //Hi Jamie

var calcNum = adder(100);
console.log(calcNum(50)); //150

```
same base function `adder`, used differently! :)
