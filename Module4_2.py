# This program converts the dictionary Fin_status to Panda series
import numpy as np
import pandas as pd

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
revenue = [145, 760, 861, 917, 805, 810, 114, 976, 103, 143, 107, 154]
expenses = [120, 569, 123, 120, 865, 840, 328, 582, 697, 166, 100, 380]

# The list is converted to numpy array
m = months
r = revenue
e = expenses
m = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
r = np.array([145, 760, 861, 917, 805, 810, 114, 976, 103, 143, 107, 154])
e = np.array([120, 569, 123, 120, 865, 840, 328, 582, 697, 166, 100, 380])

profit = np.subtract(r, e)
Fin_status = dict(zip(m ,profit))

# Converts the dictionary to Pandas Series
P_series = pd.Series(Fin_status)
print(P_series)
