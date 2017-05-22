# How to use class in JavaScript(1)
(This is my personal practice on [this page](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Classes). May use some similar codes.)

## Declare a class
```
class Page {
  constructor(words, lines){
    this.words = words;
    this.lines = lines;
  }
}
```
This code declares a class `Page`, with two inputs for its members.
> Important: Classes are NOT hoisted, oppose to methods.

## Class body and method definitions
* Strict Mode is used for class definitions and class expressions.
* Constructor can be used for creating and initializing instances.
* Prototype methods
```
class Page {
  constructor(words, lines){
    this.words = words;
    this.lines = lines;
  }

  // let's pretend this is real lol
  get wordCount(){
    return this.calcCount();
  }

  calcCount() {
    return this.words * this.lines;
  }
}

const page = new Page(25, 20);
console.log(page.wordCount);
```
* Static methods
The word `static` defined static method. They are called without instantiating class and CANNOT be called through class instance.
```
class Point {
  constructor(x,y){
    this.x = x;
    this.y = y;
  }

  static distance(a,b){
    const dx = a.x - b.x;
    const dy = a.y - b.y;

    return Math.sqrt(dx*dx + dy*dy);
  }
}

const p1 = new Point(5,5);
const p2 = new Point(10,10);

console.log(Point.distance(p1,p2));

```
