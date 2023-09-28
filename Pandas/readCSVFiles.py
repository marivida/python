# https://www.w3schools.com/python/pandas/pandas_csv.asp


# # Load the CSV into a DataFrame:
# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df.to_string()) # printa todo o csv
# # print(df) # printa apenas as primeiras 5 linhas e ultimas 5 linhas 


# # The number of rows returned is defined in Pandas option settings.
# # You can check your system's maximum rows with the pd.options.display.max_rows statement.
# # Example: Check the number of maximum returned rows:
# import pandas as pd
# print(pd.options.display.max_rows) 


# In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.
# You can change the maximum rows number with the same statement.
# Example: Increase the maximum number of rows to display the entire DataFrame:
import pandas as pd
print(pd.options.display.max_rows)
pd.options.display.max_rows = 9999
print(pd.options.display.max_rows)
df = pd.read_csv('data.csv')
print(df)


