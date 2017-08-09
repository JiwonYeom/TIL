# 6 Sets

* Keywords
> **unordered**, **unique elements**, **cannot be repeated**, **array with no repeated elements**, **no concept/order**

### `Set` in ECMA6

https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Set

`Set` object allows storing unique values of any type. One can iterate through elements of a set in *insertion order*.

```JavaScript
new Set([iterable]);
```

* Each value must be unique. Value equality will be checked.
* `NaN` and `undefined` can also be stored in a `Set`.
* `NaN` is considered the same with `NaN`. (Even though `NaN` !== `NaN`)
* +0 and -0

#### Properties

1. Set.length ( == 0)
2. get Set[@@species] : constructor function that is used to create objects


```JavaScript
class MySet extends Set{
  // Overwrite Myset soecies to the parent Set constructor
  static get [Symbol.species]() { return Set; }
}
```

3. Set.prototype : represents prototype for `Set` constructor. Allows addition to all `Set` objects.


**Properties**

1.Set.prototype.constructor : Returns function that created an instance's prototype.

2.Set.prototype.size : Returns number of values in Set object.

**Methods**

1.`Set.prototype.add(value)` :  appends a new element to the `Set` object and returns it.

2.`Set.prototype.clear()` : removes all elements from the `Set` object.

3.`Set.prototype.delete(value)` : Removes the element of `value`, returns what *would* have been returned by `Set.prototype.has(value)` previously. `Set.prototype.has(value)` will return `false` afterwards.

4.`Set.prototype.entries()` : Returns iterator object that contains an array of [value, value] for each element in the Set object, in insertion order.

5.`Set.prototype.forEach(callbackFn[, thisArg])` : Calls callbackFn for each value in Set object, in insertion order. If an argument is provided, used as this value in each callback.

6.`Set.prototype.values()` : Returns new iterator object that contains values of each element in a set.

7.`Set.prototype[@@iterator]()`: same with `Set.prototype.values()`

#### Instances

All `Set` instances inherit from Set.prototype.
