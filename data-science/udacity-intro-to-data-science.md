# Data Science Series - Udacity
## Intro to Data Science

##### 1. Tools
* **Numpy** : Python library that allows various numeric manipulation.

* **Pandas** : Stores data with *Dataframe* (Two-dimensional labeled data structure).
  * Selecting a single column will return a Series.
  * Selecting multiple columns will return a DataFrame.
  * Select rows by 1) slicing, 2) individual index, 3) boolean indexing


Pandas Syntax (simple creation of df)
```Python
from pandas import DataFrame, Series

df = DataFrame({
  'name': Series(['Harry', 'Ron', 'Hermione']),
  'age': Series([14,14,14]),
  'awards' : Series([2,2,5])
  })
```

Dataframe can be used with dot calculation with `numpy`
```Python
olympic_medals_df = DataFrame({'countries' : Series(countries), 'gold' : Series(gold), 'silver' : Series(silver), 'bronze' : Series(bronze) })
medals = olympic_medals_df[['gold', 'silver', 'bronze']] # this can be used for dot calculation with another array
counts = numpy.dot(medals,[4,2,1]) # returns an array that is list of sum of gold * 4, silver * 2, bronze * 1 for each line

```

##### 2. Concepts
* DataFrame : group of Series that share an index (I think this could be same meaning with a 'row' in a table).


##### 3. Examples & feedbacks
* heuristics - Titanic
  - change conditions (passenger's age, sex, ticket class, etc) to see if there are any affecting factors for the survival of passengers)

  - I tried sex, ticket class , age, siblings (assuming they might have helped each other to survive), and other combinations.
  - Turns out age set of < 19 rated highest survival rate (for males).
  - Generally the rich survived better.
  - Number of siblings didn't have significant effect on survival rate.
  - Since this is a 'prediction' on existing data, I learnt I'd have to come up with complex conditions and calculated assumptions to make better steps to prediction.
