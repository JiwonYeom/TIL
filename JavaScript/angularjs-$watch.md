# How to use $watch in AngularJS

When using `AngularJS`, it is super convenient that it would update the view if you change the `$scope`.
BUT, `$scope`s are not automatically updated. You hold responsibility to meticulously update related `$scopes` that you want to change.
But if this is happening as a common act for numerous times in your code, you can use the `$watch` function for convenience.
`$watch` will literally 'watch' the `$scope` that you set, and allow you to define common action for that.
Following's my code for using the `$watch` function:
```
$scope.$watch('allData.usd_total', function(newValue, oldValue){
        if(typeof $scope.allData != 'undefined'){
            ...
            $scope.allData.krw_total = krwTotal.substring(0, krwTotal.length-1) + 0;
        }
    });
```
