# Using AngularJS and jQuery together - $apply

There would be some occasions where your view wouldn't update, even though the `$scope` values have already been changed.
This is not a common thing in `AngularJS`, if you are using strictly *Angular context* - which is necessary for updating bindings.
In order to make that happen, I had to do this:
```
$scope.$apply(function(){
        ...
        $scope.allData.krw_total = krwTotal.substring(0, krwTotal.length-1) + 0;
    });
```
I found out this was because I called `$scope` value within a `jQuery` function. It will still change the `$scope`, but it WON'T update the view. This `$apply` function includes `$digest`, which holds the magic of binding within `AngularJS`.
So if you need the view bindings to instantly update but you are triggering it within `jQuery` context, you need to intentionally do it with `$apply` function.
