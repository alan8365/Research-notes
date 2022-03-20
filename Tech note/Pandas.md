progress: [Summary Functions and Maps | Kaggle](https://www.kaggle.com/code/residentmario/summary-functions-and-maps/tutorial)

## Data io

### Data creating
```python
import pandas as pd

# df creating
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

# series creating
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
```

### Data reading

```python
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
wine_reviews.head()
```

### Data writing

```python
wine_reviews.to_json('test.json')
```

## Data checking

```python
# First row of data
reviews.iloc[0]
# First colum of data
reviews.iloc[:, 0]
# 0, 1, 2 row in colum 0 of data
reviews.iloc[[0, 1, 2], 0]
reviews.loc[[0,1,10,100], ['country', 'province', 'region_1', 'region_2']]
```

#### Choosing between loc and iloc
`iloc` uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. So `0:10` will select entries `0,...,9`. `loc`, meanwhile, indexes inclusively. So `0:10` will select entries `0,...,10`.

### Conditional selection

```python
# Normal condition
reviews.loc[reveiws.country == 'Italy']
# In condition
reviews.loc[reviews.country.isin(['Italy', 'France'])]
# Null exclude condition
reviews.loc[reviews.price.notnull()]
# Multi-condition
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]
```


## Data parse

