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