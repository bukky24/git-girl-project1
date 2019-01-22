# This program calculates the profit for ABD company for a year
import numpy as np
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

# Profit is calculated as Revenue minus Expenses
profit = np.subtract(r, e)
print ("The Profit is", profit)
