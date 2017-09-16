# BEM - Key Concepts

Reference to [here](https://en.bem.info/methodology/quick-start/)

* Component-based approach to web development
* divide UI into blocks
* easier interface development
* reusable code without copy & pasting

##### 1. Block

* **Represented by CLASS attribute**
* **name describes its PURPOSE**
* Component
* encapsulates behaviors, templates, styles, etc.
* Should NOT influence the environment. **Do not set margin, padding, postion, etc.**
* **No CSS tag / ID selectors.**
* *Nested* structure.
* *Arbitrary* placement : blocks should be able to move around the page without modifying CSS / JavaScript
* Reuse by creating *instances*

##### 2. Element

* **name describes its PURPOSE**
* **naming rule: `block-name__element-name`.**

* NESTING : Even if they are nested, they are all **part of a BLOCK**, not an ELEMENT. (`block-name_elment-name__element-name` <= not allowed). If this is needed (elements under element), use service block instead.
* MEMBERSHIP : element is ALWAYS a part of a block.
* Optional

##### 3. Modifier
* Describes its **APPEARANCE**, **STATE**, and **BEHAVIOR**.
* **Separated from block / element name by a single _.**
* **Cannot be used alone. Use it alongside block / element class**
* **Types:**
  * Boolean: when presence / absence of modifier is important & value unimportant.
  * Key-value: when modifier value is important.

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
```HTML5
<div class="header">
  <!-- mix of block 'search-form' and element 'header__search-form' -->
  <div class="search-form header__search-form"></div>
</div>
```

##### 6. BEM tree
* DOM tree written in BEM entities
