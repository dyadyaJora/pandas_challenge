# Notes

## Intro

`pandas` library is an incredibly useful tool for processing and analyzing structured data in the Python programming language. It enables easy data importing, manipulation, and aggregation, making it an indispensable tool for data analysis tasks.
To get started with this library, you can find information in the [official pandas documentation](https://pandas.pydata.org/docs/). Also extremely useful pandas commands cheat sheet with images could be found by the [link](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf).
In this article I want to create an overview of [30 days of Pandas](https://leetcode.com/studyplan/30-days-of-pandas/) Leetcode's stydy plan, highlight examples of convenient data manipulation methods, and take a look how data retrieval methods in pandas correlates with SQL

![image](img/python_glass.jpg)

## Overview

Dive into the capabilities of the Pandas library with this article and uncover the most frequently used tips. Let's explore Pandas through topics such as library overview, SQL comparisons, and topics from the study plan:

* Data Filtering
* String Methods
* Data Manipulation
* Data Aggregation
* Data Integration

## What is a DataFrame

The DataFrame class in the Pandas library is a powerful two-dimensional labeled data structure with columns that can be of different types. It provides a flexible and efficient way to handle and analyze structured data. Here's a concise example of DataFrame creation:

```python 
import pandas as pd
subjects_data = {'Subject': ['Mathematics', 'Computer Science', 'Literature'],
                 'Units': [4, 3, 2],
                 'Level': ['Advanced', 'Intermediate', 'Beginner']}
subjects_df = pd.DataFrame(subjects_data)
```

Pandas `DataFrame` class implements an approach to interact with tabular data. Since it has an override for `__getitem__`, we can use brackets operator (`[]`) to get data from it.
For example, we could use string key with column name to get it `df['column']`.
Different type of objects could be placed inside the brackets: single string key, iterable, slice, etc.
And dataframe acts in different ways with it.

## Data selection and filtering

Let's take a look on rows and columns selection.  
Selecting single column using brackets operation and returns `<class 'Series'>`:

```python 
subject_column = df['Subject']
# 0         Math
# 1      Physics
# 2      History
# 3    Chemistry
# Name: Subject, dtype: object
```

Selecting multiple columns as `<class 'DataFrame'>`:

```python 
subset_data = df[['Subject', 'Units']]
#      Subject  Units
# 0       Math      4
# 1    Physics      3
# 2    History      3
# 3  Chemistry      4
```

Selecting single row as `<class 'Series'>` with `loc` function:

```python 
zero_row = df.loc[0]
# Subject       Math
# Units            4
# Difficulty    Hard
# Name: 0, dtype: object
```

Selecting single value with `at` function by indexes in row  and column:

```python 
subject = df.at[1, 'Subject']
# Physics
```

Different ways to select single value from df using `loc`, `iloc`, `at`, `iat` functions:

```python 
subject = df.at[0, 'Subject']
subject = df.iat[0, 0]

subject = df.loc[0].loc['Subject']
subject = df.loc[0].iloc[0]

subject = df.loc[0].at['Subject']
subject = df.loc[0].iat[0]

# all returns 'Math'
```

The difference between `iat` and `at` (also `loc` and `iloc`) is that the `i*` function can receive a value by the ordinal number, and the second by the index value. It is worth noting that the default index in DataFrame uses integers, so in this case the use of functions is equivalent.
And after getting row series with `df.loc[0]`, we have a series with column name as indexes, so we could not use `df.loc[0].loc[0]` here.

Also, we could use `.loc` and `.iloc` to get data using slices:

```python
# Here, we are selecting rows 1 to 3 (inclusive) and all columns
subset_df = df.loc[1:3, :]
# Selecting rows 1 to 3 and only the 'Subject' and 'Difficulty' columns
subset_df = df.loc[1:3, ['Subject', 'Difficulty']]
```

Row Selection based on condition - selecting rows where Units are greater than 3 as `<class 'DataFrame'>`
```python 
high_credit_subjects = df[df['Units'] > 3]
#      Subject  Units Difficulty
# 0       Math      4       Hard
# 3  Chemistry      4   Moderate
```

Row Selection based on multiple conditions - selecting rows where Units are greater than 3 and Difficulty is 'Hard' as `<class 'DataFrame'>`
```python 
hard_subjects = df[(df['Units'] > 3) & (df['Difficulty'] == 'Hard')]
#   Subject  Units Difficulty
# 0    Math      4       Hard
```


### Logical operations with DataFrame

Let's take a close look at usages of brackets operations. Boolean operations with dataframe's columns return a series class with result of used operation.
For example: operation `bool_series = df['Units'] > 3` returns pandas `<class pandas.core.series.Series>` with values
```python
# 0     True
# 1     True
# 2    False
# 3    False
# 4     True
# Name: age, dtype: bool
```

And after that we could get with boolean series to filter out our DataFrame.
```python 
unit_3_df = df[df['Units'] > 3]
# or
unit_3_df = df[bool_series]

#      Subject  Units Difficulty
# 0       Math      4       Hard
# 3  Chemistry      4   Moderate
```

After that we can apply boolean operations to it as to regular matrix.

Boolean series could be used as parameter to `loc`/`iloc` functions. 

In pandas, logical operators and logical functions are used for boolean operations on DataFrames and Series. Here's a brief overview of the logic operators commonly used in pandas:

* `&` (AND Operator): combines two conditions element-wise and returns True where both conditions are true. f. e.`df[(df['Column1'] > 5) & (df['Column2'] == 'Value')]`
* `|` (OR Operator): combines two conditions element-wise and returns True where at least one of the conditions is true. f. e. `df[(df['Column1'] > 5) | (df['Column2'] == 'Value')]`
* `~` (NOT Operator): inverts the boolean values, returning True where the condition is false. f. e. `df[~(df['Column1'] > 5)]`
* `^` (XOR Operator): applies xor boolean function. f. e. `df[~(df['Column1'] > 5)]`
* `isnull()`, `notnull()` functions: f. e. filtering rows where 'Difficulty' is null `null_difficulty_courses = df[df['Difficulty'].isnull()]`
* `isin()` function: 
* `any()`, `all()` functions: f. e. `filtered_df = df[df['Subject'].isin(['Math', 'Physics])]`


## String functions

In order to operate fast under text data in columns with `dtype="string"` different string function could be use instead of using `.apply` function call. 
There are some examples:

* `df['Subject'] = df['Subject'].str.capitalize()`
* `df['Subject'] = df['Subject'].str.lower()`
* `df['Subject'] = df['Subject'].str.upper()`
* `df['Subject'] = df['Subject'].str.len()`
* `df['Subject'] = df['Subject'].str.replace('$M', 'm', regex=True)`
* `df['Subject'].str.match(pattern)`
* `df['Subject'].str.contains(pattern)`
* more examples could be find in [pandas documentation](https://pandas.pydata.org/docs/user_guide/text.html)


## Data Manipulation

In Pandas, updating data in DataFrames can be achieved using various methods. Here are some commonly used methods for updating data in a DataFrame.

Updating column directly with literal and arithmetic operations on columns:

* `df['Column'] = 2`
* `df['Column'] = df['Column'] * 2`

Updating values using `.at[]`, `.iat[]`, `.loc[]` and `.iloc[]`. It is used to access and modify a single value in a DataFrame using labels or integer location:

* `df.at[0, 'Subject'] = "New Subject"`  
* `df.loc[df['Column'] > 5, 'Column'] = new_value`

Adding or modifying columns with methods `.apply()`, `.assign()`, `.insert()`:

* `df['Column'] = df['Column'].apply(lambda x: function(x))` apply a function to each element, row, or column of a DataFrame
* `df = df.assign(NewColumn=new_values)` create or modify columns based on existing ones
* `df.insert(loc=2, column='NewColumn', value=new_values)` insert a new column at a specific location

!!! note "inplace=True param"

    The inplace parameter in Pandas is used to specify whether to perform an operation in place or return a new object with the result. When inplace is set to True, the changes are made directly to the original object, and None is returned. When inplace is set to False (default), a new object with the changes is returned, leaving the original object unchanged.

Use cases for `inplace` param:

* `df.at[0, 'Column'].update(10, inplace=True)` Update a single value using inplace parameter
* `df.drop(columns='Column', inplace=True)` Drop a column
* `df['Column'].replace(to_replace=1, value=100, inplace=True)` Replace value in DataFrame
* `df['Column'].apply(lambda x: x * 2, inplace=True)` Apply a function to column

[comment]: <> (## Data aggregation)

[comment]: <> (merge)

[comment]: <> (groupby)

[comment]: <> (agg)

[comment]: <> (reset_index)

[comment]: <> (...)

[comment]: <> (## Comparation to SQL)

[comment]: <> (...)