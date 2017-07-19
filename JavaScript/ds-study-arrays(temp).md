# DS in JavaScript (1) ARRAY

* Keywords
> simplest memory DS, same data type,

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
(working)


### JavaScript array methods

### Joining multiple arrays

### Iterator functions

### Searching and Sorting

* Custom sorting

* Sorting string

* Searching

### Outputting the array into a string
