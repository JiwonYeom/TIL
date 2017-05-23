# How to use class in JavaScript(2)
Refence to [this page](http://www.jisaacks.com/javascript-boxing/). Credits go to Isaaks, the writer of that article. This is for my personal study.
## Boxing with Prototype & static methods
*Boxing*: wrapping primitive non-object with a corresponding wrapper.

* Primitive data types in JS are not objects.

```
"foo".constructor === String; //true
"foo".__proto__ === String.prototype; //true
"foo" instanceof String; //false
typeof "foo"; //true
new String("foo") instanceof String; //true
type new String("foo"); //"object"
```

When attempted to access a property on primitive value, it gets automatically `boxed` by its corresponding object.

So, objects (new xxx) can have properties but primitives cannot.

When a property is attempted to set on a primitive, that particular primitive gets *boxed* into an object. The property is set, but when same value primitive is read with that property, that is not the same instance anymore since it is boxed again from primitive.

You can manually box & unbox values by casting primitives to an `Object` and then invoking `valueOf` on wrapper object.

```
// box
var primitiveStr = "foo";
var objectStr = Object(primitiveStr); //강제형변환 - primitive --> object

// unbox
var objectNum = new Number(5);
var primitiveNum = objectNum.valueOf(); //object --> primitive
```
