## Python beginner stuffs

* What is `__init__.py` for?
> Required for treating the directories as packages. Prevents directories with a common name from unintentionally hiding valid modules hat occur later(deeper) on the module search path. Can be just empty but also can execute initialization code for package / set `__all__` variable.

* `__file__` : name of the file that is currently running the script.

* Python Nested Classes : can be useful when the inner class is never used outside the definition of the outer class. ex) metaclasses
ref: https://stackoverflow.com/questions/78799/is-there-a-benefit-to-defining-a-class-inside-another-class-in-python

