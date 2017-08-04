# Using `new Date()` in IE/Safari

It came across to me today that the `new Date()` worked differently in chrome and other browsers, namely IE and Safari.

This is what happened:
```JavaScript
var date = new Date('2017-08-01 00:00');

// in chrome => successfully converted to date

// in IE / safari => invalid date

```
According to [this](https://stackoverflow.com/questions/13091523/javascript-invalid-date-error-in-internet-explorer) page here, string given to date constructor must be RFC2822 or ISO8601 format.
Chrome converted it for me, but These two browsers didn't, so this is what I did to solve it:

```JavaScript
var input = '2017-08-01 00:00';
var date = new Date(moment(input).format());
```
And this will make it work. I had `moment.js` library loaded for other uses anyways, so I decided to simply use it.
