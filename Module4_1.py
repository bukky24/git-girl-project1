# This program extract data from months and profit into Fin_status

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
profit = [  25,  191,  738,  797,  -60,  -30, -214,  394, -594,  -23, 7, -226]

Fin_status = dict(zip(months,profit))
print (Fin_status)
 
