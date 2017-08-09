# General Rules Writing HTML

reference: https://www.themelocation.com/best-html5-practices/

1) `Doctype` Declaration is required. This activates standard mode in all browsers.
```HTML5
<!DOCTYPE html>
```
2) *Closing* tag is not required, but valid for void elements.

3) *Optional* tags exist. Tags like `<html>`, `<head>`, `<body>` are implied to exist even if not declared.

4) It is good practice to always include `lang` attribute in `<html>` tag for its internationalization purpose.

5) `HTML5` *should* be backwards compatible for `HTML` and `XHTML`. So it is suggested not to use XML tags.

6) `<title>` tag should *never* be omitted. It is bad for accessibility AND tab name.

7) declare character encodings.

8) *metatags* can be important from time to time. That's what the web crawler will read.

9) Use semantic elements

>`<header>`
`<nav>`
`<section>`
`<aside>`
`<main>`
`<article>`
`<footer>`
`<figure>`
`<figcaption>`

10) Use appropriate tag for purposes.

- no decorating purposes.
Do not use tags like `<big>`, `<center>`, `<strike>` - use CSS. These are deprecated.
