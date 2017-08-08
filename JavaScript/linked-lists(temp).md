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

append:
```JavaScript
this.append = function(element){
    //node has element and next
    var node = new Node(element),
    current;  // what kind of expression is this?
    if (head === null){   // if head was never reassigned
        head = node;    // assign node to head
    } else {  // if head was already assigned
        current = head;
        while(current.next){  //iterate until current.next is null
            current = current.next;   //move pointer to next
        }
        current.next = node;  //assign node to next
    }
    length++;
};
```

remove:
```JavaScript
this.removeAt = function(position){
  if (position > -1 && position < length){
    var current = head,
    previous,
    index = 0;
  if (position === 0){
    head = current.next;
  } else {
    while (index++ < position){
      previous = current;
      current = current.next;
    }
    previous.next = current.next;
  }
    length--;
    return current.element;
  } else {
    return null;
  }
};
```
