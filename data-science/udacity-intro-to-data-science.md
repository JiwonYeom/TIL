# Data Science Series - Udacity
## Intro to Data Science

##### 1. Tools
* **Numpy** : Python library that allows various numeric manipulation.

* **Pandas** : Stores data with *Dataframe* (Two-dimensional labeled data structure).
  * Selecting a single column will return a Series.
  * Selecting multiple columns will return a DataFrame.
  * Select rows by 1) slicing, 2) individual index, 3) boolean indexing


Pandas Syntax (simple creation of df)
```Python2
from pandas import DataFrame, Series

df = DataFrame({
  'name': Series(['Harry', 'Ron', 'Hermione']),
  'age': Series([14,14,14]),
  'awards' : Series([2,2,5])
  })
```

##### 2. Concepts
* DataFrame : group of Series that share an index (I think this could be same meaning with a 'row' in a table).
