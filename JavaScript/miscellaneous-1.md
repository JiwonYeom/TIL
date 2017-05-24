# `let` statement - basics

`let` declares block scope local variable.
It is different from `var` because `var` gets defined and can be used at its level (global or local) and be used for entire function. But `let` isn't.

Example:
```
function varTest {
  var x = 1;
  if(true){
    var x = 2;
    // x =2
  }
  console.log(x); // 2
}

function letTest(){
  let x = 1;
  if (true) {
    let x = 2;
    console.log(x); // 2
  }
  console.log(x); // 1
}
```
`let` also does not create a property on global object.

```
var x = 'x';
let y = 'y';
console.log(this.x); // 'x'
console.log(this.y) //undefined
```
