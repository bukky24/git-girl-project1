#This program ask the user to enter their name and age
#It also tell them the year they will turn 100 years old
name = input ("What is your name? \n")# Ask the user to enter his/her name
age = input ("How old are you? \n")# Ask the user to enter his/her age
def age100 (age):
    year = 100 - int(age) + 2019
    return year
year = age100(age)
message = "Hello %s, your age is %s and you will turn 100 in the year %d" %(name, int(age), year)

print(message)








#This program tell whether a number is even or odd 
num = int(input('Enter any number: '))#Ask the user to enter a number
mod = num % 2
if mod > 0:
    print('This is an odd number')
else:
    print('This is an even number')






