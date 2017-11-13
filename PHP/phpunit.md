## PHP Unit Testing with PHPUnit
reference1: https://www.youtube.com/watch?v=-9YVcssCACI
reference2: https://www.youtube.com/watch?v=84j61_aI0q8

#### Tutorial 1
- Composer is necessary for PHPUnit

1. Include PHPUnit framework in composer. Open `composer.json` & include the following
```JSON
"require-dev":{
    "phpunit/phpunit": "3.7.*"
}
```

2. run `composer update`. This generates phpunit files.

3. create folder for tests. Organize it into appropriate structure.

4. Declare class in the test file
```PHP
<?php 
class PagesTest extends PHPUnit_Framework_TestCase
{
    
}
```

5. execute it by `phpunit [file]` at commandline.

6. 
```PHP
class PagesTest extends PHPUnit_Framework_TestCase
{
    public function testRenderReturnsHelloWorld()
    {
        $pages = new \Controllers\Core\Web\Pages();
        $expected = 'Hello World';
        $this->assertEquals($expected, $pages->render());
    }   
}
```

7. Create `phpunit.xml`
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<phpunit bootstrap="./vendor/autoload.php"
         color="true"
         convertErrorsToExceptions="true"
         convertNoticesToExceptions="true"
         convertWarningsToExceptions="true"
         stopOnFailures="false"
         syntaxCheck="false"
         >
    <testsuites>
        <testsuite name="Tutorial Unit Tests">
            <!-- indicating the test directory -->
            <directory>./tests/</directory>
        </testsuite>
    </testsuites>
</phpunit>
```

8. add test for other functions
```PHP
class PagesTest extends PHPUnit_Framework_TestCase
{
    public function testRenderReturnsHelloWorld()
    {
        $pages = new \Controllers\Core\Web\Pages();
        $expected = 'Hello World';
        $this->assertEquals($expected, $pages->render());
    }   
    public function testReturnTrueReturnsTrue(){
        $pages = new \Controllers\Core\Web\Pages();
        $this->assertTrue($pages->returnTrue());
    }
    public function testReturnArrayReturnsValidArray()
    {
        $pages = new \Controllers\Core\Web\Pages();
        $this->assertTrue(is_array($pages->returnArray()));
    }
    public function testReturnArrayReturnsNonEmptyArray()
    {
        $pages = new \Controllers\Core\Web\Pages();
        $this->assertTrue((count($pates->returnArray() > 0));
    }
}
```

#### Tutorial 2
1. Create `test` directory and make testcase.
```PHP
class CalculatorTest extends PHPUnit_Framework_TestCase {
    public funtion testAddNumbers()
    {
        $calc = new Calculator;
        $this->assertEquals(4, $calc->add(2,2));
    }
}
```

2. Create `app` directory and `libraries` directory in it.

3. add `require` keyword to the test file.
```PHP
// but this means everytime we add classes & dependencies, we need to add require statement. Let's automate it with composer
require 'app/libraries/Calculator.php';

class CalculatorTest extends PHPUnit_Framework_TestCase {
    public funtion testAddNumbers()
    {
        $calc = new Calculator;
        $this->assertEquals(4, $calc->add(2,2));
    }
}
```

4. Create `composer.json`
```JSON
{
    "autoload":{
        "classmap": [
            "app/libraries"
        ]
    }
}
```

5. run `composer install`

6. Add `require 'vendor/autoload.php'` to the test file instead of the path require.

7. That works, but use `phpunit.xml` to do bootstrapping.

8. Use `namespace` by adding
```PHP
namespace App\Libraries;
```

9. regenerate `autoload_classmap.php`, so that namespace can be applied.

10. add 
```PHP
// including specific class using namespace
use App\Libraries\Calculator;

class CalculatorTest extends PHPUnit_Framework_TestCase{
    public funtion testAddNumbers()
    {
        $calc = new Calculator;
        $this->assertEquals(4, $calc->add(2,2));
    }

    public function testThrowsExceptionIfNonNumericIsPassed()
    {
        $calc = new Calculator;
        $calc->add('a', []);
    }
}
```

11. Throw exception for non-numeric input
```PHP
<?php
namespace App\Libraries;

class Calculator {
    public function add($x, $y){
        // wrong. Should be numeric instead of int
        // if ( ! is_int($x) or ! is_int($y)){
        if ( ! is_numeric($x) or ! is_numeric($y)){
            // `\` indicates this is a global exception, not a local exception.
            // if '\' is not here, it considers as local (App\Libraries\InvalidArgumentException) exception can causes error
            throw new \InvalidArgumentException;
        }
        return $x + $y;
    }
}
```

12. Make the test expect an exception
```PHP
// including specific class using namespace
use App\Libraries\Calculator;

class CalculatorTest extends PHPUnit_Framework_TestCase{
    public funtion testAddNumbers()
    {
        $calc = new Calculator;
        $values = [
            [2,2,4],
            [2.5,2.5,5],
            [-3,1,-2]
        ];

        foreach($values as $nums){
            $this->assertEquals($numbers[2], $calc->add($numbers[0], $numbers[1]));
        }
        // $this->assertEquals(4, $calc->add(2,2));
        // // add another assert
        // $this->assertEquals(5, $calc->add(2.5,2.5));
        // $this->assertEquals(-2, $calc->add(-3,1));
    }

    /**
     * @expectedException InvalidArgumentException
     */
    public function testThrowsExceptionIfNonNumericIsPassed()
    {
        $calc = new Calculator;
        $calc->add('a', []);
    }
}
```

13. Abstract out your tests using PHPUnit.

```PHP
// including specific class using namespace
use App\Libraries\Calculator;

class CalculatorTest extends PHPUnit_Framework_TestCase{
    public function setUp()
    {
        $this->calculator = new Calculator;
    }
    public function inputNumbers()
    {
        return [
            [2,2,4],
            [2.5,2.5,5],
            [-3,1,-2]
        ];
    }

    /**
     * @dataProvider inputNumbers
     */
    public funtion testAddNumbers($x, $y, $sum)
    {
        $this->assertEquals($sum, $this->calculator->add($x, $y));
    }

    /**
     * @expectedException InvalidArgumentException
     */
    public function testThrowsExceptionIfNonNumericIsPassed()
    {
        $this->calculator->add('a', []);
    }
}
```
