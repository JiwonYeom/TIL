### Tips & Tricks of Data Analysis

- Call .info() to find which columns need cleanup
 - Which columns contains NaN values (less than total rows)
 - Which columns are in data types other than what they should be (ex. Object while should be Int or Float)

- Bootstrap Method
```python
# A bootstrap analysis of the reduction of deaths due to handwashing
boot_mean_diff = []
for i in range(3000):
    boot_before = before_proportion.sample(frac=1,replace=True)
    boot_after = after_proportion.sample(frac=1,replace=True)
    boot_mean_diff.append(boot_before.mean()-boot_after.mean())

# Calculating a 95% confidence interval from boot_mean_diff 
confidence_interval = pd.Series(boot_mean_diff).quantile([0.025, 0.975])
confidence_interval
```
