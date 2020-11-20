### Statistics related info
- [A Complete Guide to Confidence Interval, and Examples in Python](https://towardsdatascience.com/a-complete-guide-to-confidence-interval-and-examples-in-python-ff417c5cb593)


- Types of Mean
  - Trimmed Mean: eliminates the influence of extreme values
  - python: `trim_mean` in `scipy.stats`  
 ```
 example
 Find 10% trimmed mean of 2, 4, 6, 7, 11, 21, 81, 90, 105, 121
 
 (1 / 8) * (4 + 6 + 7 + 11 + 21 + 81 + 90 + 105)
 ```
 
  - Weighted Mean:  calculate by multiplying each data value xi by a user-specified weight wi and dividing their sum by the sum of the weights. Available in Numpy
```
np.average(state['Murder.Rate'], weights=state['Population'])
wquantiles.median(state['Murder.Rate'], weights=state['Population'])
```
 
- Median: Sometimes better than Mean when using for location
  - Weighted median: First sort the data, although each data value has an associated weight. Instead of the middle number, the weighted median is a value such that the sum of the weights is equal for the lower and upper halves of the sorted list. Like the median, the weighted median is robust to outliers.
