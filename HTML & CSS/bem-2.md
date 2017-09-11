# BEM - File Structure, naming conventions and CSS

##### 1. File Structure
* Single block = single directory.
* Block and directory shares name.
* block's implementation is divided into separate technology files (css & js)
* block directory is root for subdirectories of elements & modifiers (ex. button, input, text.. etc)
* Element directory names begin with double underscore(\__)
* Names of modifier directories begin with single underscore.
* implementation of elements & modifiers are divided into different technology files.


#### 2. CSS
* Making HTML wrapper
    - HTML wrapper? used for 1) *Relatively* positioning HTML elements 2) Position element within a section
    - use mixes.
    - create additional block element
    - no additional abstract wrapper.

```HTML5
<!-- 'profile' block -->
<section class="profile">
    <div class="organization profile__organization"></div>
    <div class="photobox profile__photobox"></div>
</div>
```
```CSS3
.profile__organization {
    padding-top: 20px;
}
.profile__photobox {
    padding-top: 10px;
}
```

> +Paddings/margins to top / to bottom is often defined since it is not affected by responsiveness to a great degree, but horizontal padding / margin should be rethought before use.
