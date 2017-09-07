# BEM - File Structure, naming conventions and CSS

##### 1. File Structure
* Single block = single directory.
* Block and directory shares name.
* block's implementation is divided into separate technology files (css & js)
* block directory is root for subdirectories of elements & modifiers (ex. button, input, text.. etc)
* Element directory names begin with double underscore(\__)
* Names of modifier directories begin with single underscore.
* implementation of elements & modifiers are divided into different technology files.

##### 2. CSS
* HTML for CSS - Making HTML modifier
  - use `mixes`
  - create additional block elements

```
<body class="page">
    <!-- header and navigation-->
    <header class="header page__header">...</header>

    <!-- footer -->
    <footer class="footer page__footer">...</footer>
</body>

// CSS

.page__header {
    padding: 20px;
}

.page__footer {
    padding: 50px;
}
```

* Position elements in a block

```
<body class="page">
    <div class="page__inner">
      <!-- header and navigation-->
      <header class="header">...</header>

      <!-- footer -->
      <footer class="footer">...</footer>
    </div>
</body>

// CSS

.page__inner {
    margin-right: auto;
    margin-left: auto;
    width: 960px;
}

```
