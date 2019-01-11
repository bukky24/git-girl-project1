#This program takes a list and makes a new list that has only even elements
a = [1,4,9,16,25,36,49,64,81,100]
b = [i for i in a if i % 2 == 0]
print ("The new list which consists of even elements are: " +str(b))
