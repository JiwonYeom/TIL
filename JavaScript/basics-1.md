# `You Don't Know JS` Notes - The Basics I

Short summary on things that I didn't know or just good to review on.

#### 1.Conversion of Types

1) In JavaScript, conversion is called `coercion`.

* Explicit & Implicit

```JavaScript
var a = "6";
var b = Number(a); // explicit coercion

console.log("6" == 6); //true. Implicit coercion

var number = 5;
number = 5 + 'apples'; // implicit coercion

```

2) Use `const` keyword to protect constants(fixed values);

3) Use of `Block`

```JavaScript
// general block. Valid but not common.
{
    var test;
}
//commonly used in if, for... etc
```

4) `Scope`

* In JavaScript, each function gets its own scope.
* Only code inside that function can access the scoped variables (includes inner functions)


~ values & types
