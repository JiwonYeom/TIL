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
3. Set.prototype : represents prototype for `Set` constructor. Allows addition to all `Set` objects.

#### Instances

All `Set` instances inherit from Set.prototype.
