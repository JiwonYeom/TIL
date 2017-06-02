# Regular Expression in JS (1)
### How to create regex object in js

#### Using regex literal

This type of regex is compiled when the script is loaded, so it should be used when regex will **remain constant**.
```
var regex = /word/;
//pattern must be enclosed between slashes
```
#### Calling the `constructor` of RegExp object

This can be compiled during runtime, so if the regex pattern is going to change or getting the pattern from somewhere else, use this.
```
var regex = new RegExp('word');
```

### How to write one
#### Simple pattern

When you are looking for a direct match
```
var ex1 = /test/;
var ex2 = /tes t/;
//these two are different because there is a space between
```

#### Use special characters

When there is certain pattern that you are looking for and it is insufficient to use simple, fixed pattern. Check more [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)

examples:
1) `\` : If before `non-special character`, makes a special case of the character following(ex.\\b, \\d, \\f... ). If before a `special character`, removes the 'specialness' of the character following (ex. \*, \+ ...).

2) `*`: match preceding expression 0 or more times. Ex) /hi*/ will match both in 'hiii Ronnnn' and 'has been a while', the latter twice(h in 'has' and 'while').

(to be updated)

#### Use parentheses

(to be updated)
