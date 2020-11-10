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
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]
print(temperatures_bool)

temperatures_ind = temperatures.set_index("date").sort_index()

print(temperatures_ind.loc["2010":"2011"])

print(temperatures_ind["2010-08":"2011-02"])
```

- Random Sampling

`df.sample(n)`

- merges (table join)

`.merge(on='id', how='left'/'right'/'outer', right_on / left_on, suffixes = ['left_suffix','right_suffix]`

    - Left Join/ Right Join returns same or more rows for one-to-many relationship than from one-to-one relationship
    - Self Join can be used when:
        - Hierarchical Relationships
        - Sequential Relationships
        - Graph Data (Network of people/friends/nodes..)

- How to do Anti-join

```python
empl_cust = employees.merge(top_cust, on='srid', 
                                 how='left', indicator=True)

srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

print(employees[employees['srid'].isin(srid_list)])
```

- How to add keys when concat

```python
inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep], 
                            keys=['7Jul','8Aug','9Sep'])

avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'mean'})
```

- Verifying Integrity when concat/merge

`artists.merge(albums, on='artid', validate='one_to_many)`

    - Can check if data is clean & will be combined the way we expect them to be

- `merge_ordered` method
    - When mergin ordered data / time series
    - When missing values need to be filled up (ex.machine learning)

- `merge_ordered` and ffill

```python
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left',  fill_method='ffill')
```

- When want to find correlation with pandas

```python

gdp_returns = gdp_sp500[['gdp','returns']]

print(gdp_returns.corr())
```
