reference:http://javascript.info/

#### "use strict"

* to keep the old code working, most modification were kept off. "use strict" is needed to enable the modifications.

#### Variable
* Use `let` for variable
* `const` for constants

#### Objects
```javascript
let fruit = prompt("Which fruit to buy?", "apple");

let bag = {
  // this is possible! 가변변수 이용
  [fruit]: 5, // the name of the property is taken from the variable fruit
};

alert( bag.apple ); // now this will print 5 if fruit has the value "apple"
```

```javascript
function makeUser(name, age) {
  return {
    name: name,
    age: age
  };
}

let user = makeUser("John", 30);
alert(user.name); // John

//shorthands
function makeUser(name, age) {
  return {
    name,
    age,
  };
}

```

##### Object - Existence check