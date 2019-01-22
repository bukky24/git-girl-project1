# This program uses data from pandas series to plot a line graph

import pandas as pd
import matplotlib.pyplot as plt
Fin_status = {'Jan': 25, 'Feb': 191, 'Mar': 738, 'Apr': 797, 'May': -60, 'Jun': -30, 'Jul': -214, 'Aug': 394, 'Sep': -594, 'Oct': -23, 'Nov': 7, 'Dec': -226}
P_series = pd.Series(Fin_status)

plt.plot(P_series, color='blue', marker='o', linestyle='solid')
# add a title
plt.title("ABD Profit for the year")

# add label to x-axis and y-axis
plt.ylabel("Profit")
plt.xlabel("Months")
plt.show()
