* transition-duration : Literally duration.
* transition-property : what should be transitioned? (background, opacity, transform, all, color, opacity)
* transition-delay : delay certain animation
* transition-timing-functio : ease-in, ease-out, linear, cubic-bezier (easings.net)

#### Performance
* what should be transitioned? : translate, scale, rotate, opacity. (If you are concerned with performance)
* Why? Browser rendering process (html5rocks.com). Certain properties are rendered in different steps of rendering - those four are at the very last.
