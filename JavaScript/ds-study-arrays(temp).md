# DS in JavaScript (1) ARRAY

* Keywords
> **simplest memory DS**, **same data type**, **modified objects**

### Creating and Initializing

1) use `new` keyword
```
var testArray = new Array();
```

2) `[]`
```
var testArray = []; //declare
var testArray2 = ['test1', 'test2', 'test3'] //initialize
```

### Adding and removing elements
1) `push()`: add to the end

2) `unshift()`: add to the front
// add code

3) `pop()`: remove from the back

4) `shift()`: remove from the front
//manually code

5) `splice()`: remove in between / add in between
```
// remove
array.splice(1,2);
// add
array.splice(2,0,1,2,3);
```

*&ast;note:*
push & pop is an emulation of `stack`. shift & unshift is an emulation of `queue`


### Two-dimensional and multi-dimensional arrays
* We might want to use `matrix` (`Two-dimensional array`) in some cases.
* JS does not support matrices.
* Instead, we use arrays of arrays.

##### 2 x 2
```
// everyday meal
// 0 ~ 4 --> mon ~ fri
dailyMeal[0] = [];
dailyMeal[0][0] = 'milk and bread';
dailyMeal[0][1] = '김치찌개';
dailyMeal[0][1] = 'fried chicken';
dailyMeal[1] = [];
dailyMeal[1][0] = 'yogurt';
dailyMeal[1][1] = '제육볶음';
dailyMeal[1][2] = 'roasted fish';
...

// function to print this matrix
function printMeal(dailyMeal){
    for(var i = 0 ; i < dailyMeal.length < i++) {
        for(var j = 0 ; j < dailyMeal[i].length < j++) {
            console.log(dailyMeal[i][j]);
        }
    }
}
```
##### 3 x 3
```
// function to create 3x3 matrix
var matrix = [];
for (var i = 0 ; i < 3 ; i++){
    matrix[i] = [];
    for (var j = 0 ; j < 3 ; j++){
        matrix[i][j] = [];
        for (var z = 0 ; z < 3 ; z++){
            matrix[i][j][z] = i+j+z;
        }
    }
}

console.log(matrix);
// 0,1,2    1,2,3   2,3,4
// 1,2,3    2,3,4   3,4,5
// 2,3,4    3,4,5   4,5,6
```

### Joining multiple arrays
1) `concat()` : allows joining multiple arrays and objects into one aray.

*&ast;note* : works regardless types

```
var test = 'test';
var testArray1 = [1,3,5,7];
var testArray2 = [2,4,6,8];
testArray1.concat(test,testArray2);
>> [1, 3, 5, 7, "test", 2, 4, 6, 8]
```

### Iterator functions
```
//sample function
var isEight = function(x){
	console.log(x);
	return x == 8;
}
```
1) `every()` : iterates each element, passes it to a function, stops when result is false.
```
var numberArray = [1,2,3,4,5,6,7,8,9,10];
numberArray.some(isEight);
>>1
>>false
```
2) `some()` : iterates each element, passes it to a function, stops when result is true.
```
numberArray.some(isEight);
>>1
>>2
>>...
>>8
>>true
```
3) `map()` : Returns an array that stores result of every function run.
```
numberArray.map(isEight);
>> [false, false, false, false, false, false, false, true, false, false];
```
4) `filter()` : returns an array with elements of `true` value.
```
var lotsOfEight = [1,8,3,4,8,8,3,4,8];
>> [8, 8, 8, 8]
```

5) `reduce(function(prevValue, currentValue, currentIndex, arr), initialValue)` : returns a result that has been ran continuously with given function through each element.
*&ast;note*: prevValue == 전 회차에서 반환된 값.
See [here](https://www.w3schools.com/jsref/jsref_reduce.asp) for more detail.
```
numberArray.reduce(function(prevValue, currentValue, currentIndex, arr), initialValue) {
	return prevValue + current;
});
>> 55;
```

### Searching and Sorting
1) `reverse()` : literally reverses the order of elements.

2) `sort()` : sorts elements of an array. This sort is *lexicographic*, which means `by string`, not `by numbers`.

If we want our `sort()` to sort *numerically*, we need to pass another function to the `sort()` function. This is called `compareFunction`.

> array.sort(compareFunction)

To sort with ascending order:
```
numberArray.sort(function(a,b){
  return a-b;
});
>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
To sort with descending order:
```
numberArray.sort(function(a,b){
  return b-a;
});
>> [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

* Custom sorting

We can use `compareFunction` to compare any type of elements as we define.
```
var petAge = [
  {name: '치즈', weight : 2},
  {name: '봉구', weight : 1.8},
  {name: '루루', weight : 2.2},
];

function compareWeight(a,b) {
  return a.weight - b.weight;
}

console.log(petAge.sort(compareWeight));
>>봉구 - 치즈 - 루루
```

* Sorting string

`sort()` will sort strings according to `ASCII` value.

But sometimes, you would want them to be ordered with different ordering rule.

```
// ignore cases
function ignoreCase(a,b){
  a.toLowerCase() - b.toLowerCase;
}
```

* Searching

1) `indexOf()` : first match

2) `lastIndexOf()` : last match


### Outputting the array into a string

1) `toString()` : convert array to string, with `,` separator.

2) `join()` : do the same thing with `toString()`, but with given separator.
