# $ in console
If a `$` is not overriden by jQuery(which usually uses `$` for its alias), `$()` can be used as an alias of `document.querySelector`.

Which means:

```
$('p');
// <p>"text"</p>
```
Also, Chrome provides convenient function which will return all matches for that css selector. It seems like both `$` and `$$` work, in case jQuery has already overriden `$`.
The return result is same with `document.querySelectorAll`.
