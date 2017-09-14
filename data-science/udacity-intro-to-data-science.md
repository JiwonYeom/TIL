# Data Science Series - Udacity
## Intro to Data Science

##### 1. Tools
* **Numpy** : Python library that allows various numeric manipulation.

* **Pandas** : Stores data with *Dataframe* (Two-dimensional labeled data structure).

Pandas Syntax (simple creation of d)
```Python2
from pandas import DataFrame, Series

df = DataFrame({
  'name': Series(['Harry', 'Ron', 'Hermione']),
  'age': Series([14,14,14]),
  'awards' : Series([2,2,5])
  })
```
