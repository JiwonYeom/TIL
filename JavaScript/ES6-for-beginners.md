## [ES6 for beginners](https://hackernoon.com/es6-for-beginners-f98120b57414) try out
(Covering only the parts that I didn't know)

* `const`
`const` declares constants, which are fixed values. But one thing to note, const has to do with *refernces*. Which means as long as refered address stays the same, it's considered same.
```
const CLASSMATES = ['James', 'David', 'Sophia'];
CLASSMATES = "Nina"; // throws error
CLASSMATES.push("Nina"); // okay, because it still refers to same reference
```

* Arrow Function
```
function iUsedToBe(){
    console.log("I'm the old one");
}

var newMe = () => {
    console.log("new me!");
}

let newMeWithArgs = (a,b) => {
    console.log("Hi " + a + "and " + b + "!");
}
newMeWithArgs("Jennifer","Robin");

//default param
let defaultParams = (a = 10) => {
    console.log(a + 20);
}
defaultParams();
```
Here, `var newMe = ()` means assigning the function to a variable.
And, `{}` part is the body of the function.


* New `for` loop
works like forEach!
```
let arr =[9,8,7,6];
for (let val of arr){
    console.log(arr);
}

// works for string too
let hello = "Hello";
for (let char of hello){
    console.log(char);
}

```

* Spread
help to spread the expression - converts list of elements to an array. Expressed by `...`

```
let arr = [10,20,30,40];
Math.max(arr);  //error
Math.max(...arr);   //works
```