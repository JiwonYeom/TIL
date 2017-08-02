# DS in JavaScript (4) Linked Lists

* Keywords
> **dynamic DS**, **sequential collection of elements**, **node**

Linked Lists are different from arrays in a sense that

1) elements are not placed directly in memory.

2) Each element consists of node. This node stores element + reference.

3) No need to shift elements around when adding / removing.

4) Need pointers.

5) In order to access an element from middle, need to start from beginning (`head`) and iterate.

```JavaScript
function LinkedList(){
  var Node = function(element){
    this.element = element;
    this.next = null;
  }
  var length = 0;
  var head = null;
  this.append = function(element){};
  this.insert = function(position, element){};
  this.removeAt = function(position){};
  this.remove = function(element){};
  this.indexOf = function(element){};
  this.isEmpty = function() {};
  this.size = function() {};
  this.toString = function(){};
  this.print = function(){};
}
```
