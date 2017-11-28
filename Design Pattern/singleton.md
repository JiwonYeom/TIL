### Singleton Pattern
* ensure one and only one object of the class gets created
* Provide access point for object as global scope
* Control concurrent access to the resources that are shared

> How to Implement?
> - Make the constructor private
> - Create static method that does initialization
> - Object gets created on the first call. Class returns the same object aftwerwards.

##### Classic Singleton
```python
class Singleton(object):
    # __new__ is Python's method to instantiate object.
    # Overriding __new__ method to control object creation.
    def __new__(cls):   
        # checks whether object already exists. hasattr method checks cls object has the instance property. == class already has an object
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s = Singleton()
print("Object created", s)

s1 = Singleton()
print("Object created", s1)
```
##### Lazy instantiation in Singleton
* Prevent exidental creation of object that is not needed
* Make sure object gets created when it's actually needed
* work with reduced resources and create them only when needed.

```python
class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called..")
        else:
            print("Instance already created:", self.getInstance())
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s = Singleton()
print("Object created", Singleton.getInstance())
s1 = Singleton() # instance alreay created
```