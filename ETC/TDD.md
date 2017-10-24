### TDD Basics & Howto

> TDD is more of an approach, rather than test itself.

* TDD aims to define problem first rather than jumping right into solution. This is why TDD is also called BDD(Behavior-driven Development).
* Write test definition from user's perspectives.
* TDD workflow:
    1. Test code is written first. This is the simplest code possible.
    ```JavaScript
    $(function(){
        test(condition, function(){
            // Given - what kind of situation
            // When - how
            // Then - result
        });
    });
    ```

References:
- https://medium.com/@bethqiang/the-absolute-beginners-guide-to-test-driven-development-with-a-practical-example-c39e73a11631
- http://huns.me/development/716
