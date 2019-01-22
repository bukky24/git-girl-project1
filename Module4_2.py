# This program convert the dictionary Fin_status to Panda series
import pandas as pd
Fin_status = {'Jan': 25, 'Feb': 191, 'Mar': 738, 'Apr': 797, 'May': -60, 'Jun': -30, 'Jul': -214, 'Aug': 394, 'Sep': -594, 'Oct': -23, 'Nov': 7, 'Dec': -226}

P_series = pd.Series(Fin_status)
print(P_series)
