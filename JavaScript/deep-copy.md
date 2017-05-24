# Deep copy of an Object in JS
When an object is put into another variable, it is copied by `reference`. This means if the original object changes, the referenced values will change too.

```
var originalArr = [
    {first:'John', last:'Smith'},
    {first:'Charles', last:'Black'}
  ];
var array1 = [];
var array2 = [];

// shallow copy
array1 = originalArr;
array2 = originalArr;

array1 = array1.splice(0,1);

console.log(array1); // [{first:'Charles', last:'Black'}]
console.log(array2); // [{first:'Charles', last:'Black'}]

```
As shown in example above, if copied by `reference`, removing an element in one array will result in removal in another variable.
So these values must be **deeply copied**, which means values must be copied by value not reference.
There are several ways to do this, but I solved this with a simple solution (This is not the most efficient one. It only shows how to make a deeply copied array)

```
for(var i = 0 ; i < originalArr.length ; i++)
{
  array1.push(originalArr[i]);
  array2.push(originalArr[i]);
}
```
I did this and somehow it worked, but I'm not sure it this is right way to do it.
Many people suggests usng the JSON method:
```
var clonedArray = JSON.parse(JSON.stringify(originalArray));
```
[Here](https://stackoverflow.com/questions/597588/how-do-you-clone-an-array-of-objects-in-javascript) are more discussions about it.
