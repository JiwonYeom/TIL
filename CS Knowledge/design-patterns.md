## Design patterns
Reference: https://www.udacity.com/course/software-development-process--ud805

### Fundamental patterns
* Delegation pattern
* Interface pattern
* Proxy pattern : surrogate controls access to an object (masks some of the functionality of the object)

### Creational patterns
* Abstract factory pattern
* Factory method pattern
    * Intent: Create objects without specifying their class
    * When class cannot anticipate the type of object to be created.(until the compile moment)
    * class wants its subclass to specify the type of object to be created
    * Class needs control over the creation of its objects
* Lazy initialization
* Singleton pattern

### Structural patterns
* Adapter pattern
* Bridge pattern
* Decorator pattern : wrapper that adds functionality to a class (stackable)

### Behavioral patterns
* Chain of responsibility
* Iterator : access elemens of a collection without knowing underlying representation
* Observer : notify dependents when object changes
* State
* Strategy
    * Intent: allow switching between different algorithms to finish certain task
    * applicable for different variants of algorithms
    * many related classes that differ only in their behavior
* Visitor : separating an algorithm from an object structure (without modifying the structure)

### Concurrency patterns
* Active Object
* Monitor object 
* Thread Pool pattern

### Pattern Format(Subset)
* **Name**
* **Intent**
* Motivation
* **Applicability**
* **Structure**
* Consequences
* Implementation
* Sample Code
* Related patterns

### Negative Design patterns (Anti-patterns / bad smells)