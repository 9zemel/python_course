import pandas as pd

arr = [12,12345334,100,8]
my_series = pd.Series(arr, index = ['id', 'Stock_Articule', 'Price', 'Amount'])

print(my_series.index)
print(my_series.values)
print(my_series['Stock_Articule'])

print(my_series['id':'Price'])
