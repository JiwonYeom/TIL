## Walkthrough of `Between two Sets` from HackerRank
https://www.hackerrank.com/challenges/between-two-sets
```
// Condition
if x mod element of A == 0 && elements of B mod x == 0
  x is between A and B
```

> Find possible x's

input
```
// [number of elements in A] [number of elements in A]
// set A
// set B
```

* LCM is needed! 

Set A's elements must be factors of number x. This means x is a LCM of elements in Set A.

Here's set of code that I found on StackOverFlow, since I also have very little memory of math:
reference [here](https://stackoverflow.com/questions/147515/least-common-multiple-for-3-or-more-numbers)

```Python
def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b) # // operator : integer division

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)
```

Using these functions, we can try and find x's that meets the given conditon.
Here's code that I wrote

```Python
def getTotalX(a, b):
    # x must be bigger / equal to biggest of a & x must be smaller / equal to smallest of b
    totalCount = 0
    lowerLimit = max(a)
    upperLimit = min(b)
    # find LCM of a's & find if results can be factors of B
    lcmResult = lcmm(*a)
    for i in range(1, upperLimit+1):
        # check if it is a factor of all B elements
        flag = True
        for elem in b:
            if elem % (lcmResult * i) != 0:
                flag = False
        if(flag == True):
            totalCount+=1
        # check if it has reached the end
        if lcmResult * i == upperLimit:
            break
    return totalCount
```



##### Things to learn
> The `*` expression(https://mingrammer.com/understanding-the-asterisk-of-python)