## pandas cheatsheet

- sort_values

`df.sort_values(by='col1', ascending=False, na_position='first')`

- value_counts

`Series.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)`

- pivot_table()

`pandas.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All', observed=False)`

`sales.pivot_table(values='weekly_sales',index='type')`

`sales.pivot_table(values="weekly_sales", index="type", columns="is_holiday")`

- group_by

`df.groupby(by=["b"], dropna=False).sum()`

`sales.groupby("type")["weekly_sales"].agg([np.min,np.max, np.mean, np.median])`

- `loc` and `iloc`
    - `loc`: Label based, have to specify name of the rows and columns that we need to filter out
    - `iloc`: Integer index based. specify rows/columns by integer index.

reference: https://stackoverflow.com/a/43968774

- Time Series slicing

```python
# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]
print(temperatures_bool)

# Set date as an index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind["2010-08":"2011-02"])
```