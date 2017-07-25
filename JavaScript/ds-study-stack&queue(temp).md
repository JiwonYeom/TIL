# DS in JavaScript (2) STACK
* Keywords
> **LIFO**

#### Stack class implementation

```JavaScript
function Stack(){
  var items = [];

  // push - add item to the top of the stack
  this.push = function(element){
      items.push(element);
  }

  // pop - remove item from the top of the stack
  this.pop = function(){
      items.pop();
  }

  // returns the topmost element for information purpose
  this.peek = function(){
      return items[items.length-1];  
  }

  // check if the stack is empty
  this.isEmpty = function(){
      return items.length == 0;
  }

  // return the size of stack
  this.size = function(){
      return items.length;
  }

  this.clear = function(){
      items = [];
  }

  this.print = function(){
      console.log(items.toString());
  }
};

// use the Stack class
var stack = new Stack();
stack.push(1);
stack.push(3);
stack.pop();
stack.push(5);
stack.peek();
stack.isEmpty();
//...
```
#### Using Stack to convert decimal to binary
```JavaScript
function baseConverter(decNumber, base){
    var remStack = new Stack(),
    rem,
    baseString = '',
    digits = '0123456789ABCDEF';

    while(decNumber > 0){
        rem = Math.floor(decNumber % base);
        remStack.push(rem);
        decNumber = Math.floor(decNumber / base);
    }

    while(!remStack.isEmpty()){
        baseString += digits[remStack.pop()];
    }

    return baseString;
}

```

# DS in JavaScript (3) QUEUE
* Keywords
> **FIFO**

#### Queue class implementation

```JavaScript
function Queue(){
    var items = [];

    // add item to the back
    this.enqueue = function(elements){

    }

    // remove item from the front. returns the item.
    this.dequeue = function(){

    }

    // return the first item from the queue -- similar to peek
    this.front = function(){

    }

    this.isEmpty = function(){

    }

    this.size() = function(){

    }
}
```
