# BEM

Reference to [here](https://en.bem.info/methodology/quick-start/)

* Component-based approach to web development
* divide UI into blocks
* easier interface development
* reusable code without copy & pasting

##### 1. Block

* Component
* encapsulates behaviors, templates, styles, etc.
* *Nested* structure.
* *Arbitrary* placement : blocks should be able to move around the page without modifying CSS / JavaScript
* Reuse by creating *instances*

##### 2. Element

* Forms a block. CANNOT be used outside of it. (= will not be repeated in other blocks)
* Not recommended to use element within element.

##### 3. Modifier
* Defines appearance and behavior of a block / an element.
* optional
* Similar to HTML attr
* can change during runtime

##### 4. BEM entity
* Blocks, elements, and modifiers

##### 5. Mix
* An instance of different BEM entities on a single DOM node.
* combines behaviors & styles of several entities without code duplication
* create semantically new interface component on the basis of existing entities.

##### 6. BEM tree
* DOM tree written in BEM entities

##### 7. Block implementation

##### 8. Block implementation technology
##### 9. Block redefinition
##### 10. Redefinition level
