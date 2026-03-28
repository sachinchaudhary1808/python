# data cleaning
```python
read_csv("file")
df.dropna() # cleans values

```

### understanding dataset before applying statsical or machine learning techqniues to understand how data is spread

# analyzing
```python
df_clean.dtypes # lists data types and columns
df_clean.describe() # data description
```
#### slandered derivation

### using and graphical representation
-> boxplot ( homo and hetero genius)
-> histogram
#### outlier analysis

### correlation
-> how the change of one value make change in other values
#### positive
#### nothing
#### negative
```python
df_clean.corr(numeric_only = True)
```

# data Pre-processing

### features ( collected data)
-> independent variable ( variable under study) write 'X'
### target  (something u want to predict) 
-> dependent variable ( something u want to predict) write 'y'

### feature selection
-> relevant features
-> irrelevant features
-> redundant features

```python
age,marks,etc -> feature
makrs -> target
```

Marks is function of (Age,Attendance, Gender)

# introduction to Machine learning
y = f(X) + e # unexplained term or error

### two types
#### Supervised
-> prediction via training on the labeled data
classification regression
##### regression
#### Unsupervised
##### clustering
##### pca analysis
-> prediction via training on the unlabeled data
    -> grouping

### overfit
### optimum
### underfit

# also in r ...
