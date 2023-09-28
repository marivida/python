# https://www.w3schools.com/python/pandas/pandas_series.asp


# # Pandas Series is like a column in a table.
# # It is a one-dimensional array holding data of any type.
# # Example: Create a simple Pandas Series from a list:
# import pandas as pd
# a = [1, 7, 2]
# myvar = pd.Series(a)
# print(myvar)


# # Labels: If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
# # This label can be used to access a specified value.
# # Example: Return the first value of the Series:
# import pandas as pd
# a = [1, 7, 2]
# myvar = pd.Series(a)
# print(myvar[0])


# # With the index argument, you can name your own labels.
# # Example: Create your own labels:
# import pandas as pd
# a = [1, 7, 2]
# myvar = pd.Series(a, index = ["x", "y", "z"])
# # print(myvar)
# # When you have created labels, you can access an item by referring to the label.
# # Example: Return the value of "y":
# print(myvar["y"])


# # You can also use a key/value object, like a dictionary, when creating a Series.
# # Example: Create a simple Pandas Series from a dictionary:
# import pandas as pd
# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories)
# print(myvar)
# # Note: The keys of the dictionary become the labels.


# # To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.
# # Example: Create a Series using only data from "day1" and "day2":
# import pandas as pd
# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories, index = ["day1", "day2"])
# print(myvar)


# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.
# Example: Create a DataFrame from two Series:
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data, index=['day 1', 'day 2', 'day 3'])
print(myvar)

