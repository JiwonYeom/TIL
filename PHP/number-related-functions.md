# Commonly used number-related functions
* `strtotime()`

converts string to time. Some examples:
```
// $custom_date in timestamp
$new_date = strtotime('last day of', $custom_date); //sets last day of month in timestamp
$new_date = strtotime('+1 month', $custom_date); //sets date to the next month
$new_date = strtotime('-1 month', $custom_date); //sets date to the previous month
```

* `number_format()`

converts number into **string** with thousand `,` markers.
One trick with this fuction is that you can keep decimal points (if you pass the right `float` type numbers) as an end result.
Example:
```
echo number_format(6.0005); // 6
echo number_format(6.0005, 2, '.', ''); // will print 6.00, not 6
echo number_format(524000); // 524,000
echo number_format(524000, 2, '.', ''); // will print 524,000.00
```
`number_format` can be handy when used with `round()` for cases when you have to output cost into dollar formats
