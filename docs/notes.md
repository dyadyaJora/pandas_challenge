# Notes

## Intro

`pandas` library is an incredibly useful tool for processing and analyzing structured data in the Python programming language. It enables easy data importing, manipulation, and aggregation, making it an indispensable tool for data analysis tasks.
To get started with this library, you can find information in the [official pandas documentation](https://pandas.pydata.org/docs/). Also extremely useful pandas commands cheat sheet with images could be found by the [link](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf).
In this article I want to create an overview of [30 days of Pandas](https://leetcode.com/studyplan/30-days-of-pandas/) Leetcode's stydy plan, highlight examples of convenient data manipulation methods, and take a look how data retrieval methods in pandas correlates with SQL

![image](img/python_glass.jpg)

## Overview

...

## DataFrame

### Common info

Pandas `DataFrame` class implements an approach to interact with tabular data. Since it has an override for `__getitem__`, we can use brackets operator (`[]`) to get data from it.
For example, we could use string key with column name to get it `df['column']`.
Different type of objects could be placed inside the brackets: single string key, iterable, slice, etc.
And dataframe acts in different ways with it.
Let's take a close look at usages of brackets operations

### Logical operations with DataFrame

Boolean operations with dataframe's columns return a series class with result of used operation.
For example: operation `df['age'] > 20` returns pandas `<class pandas.core.series.Series>` with values
`'0 True
1     True
2    False
3     True
4    False
Name: age, dtype: bool'`