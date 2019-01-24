# This program uses data from pandas series to plot a line graph

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
P_series = pd.Series(Fin_status)

plt.plot(P_series, color='blue', marker='o', linestyle='solid')
# add title to the graph
plt.title("ABD Profit for the year")

# add label to x-axis and y-axis
plt.ylabel("Profit")
plt.xlabel("Months")
plt.show()
