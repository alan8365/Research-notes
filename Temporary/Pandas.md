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
```