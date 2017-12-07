#2017-12-07 Goal
##Learn some Python
##Get through at least 3 lessons from the following Udemy course:
##Python for Beginners - LearnToProgram, Inc. (Alex Bowers)

##Chapter 6 Lab Exercise - Inputs
##We’ll be using loops here to check user inputs.
##We want the user to input their gender, however if it doesn’t follow the
##correct format then ask them to try again, and show the input option again.
##
##Acceptable Formats:
#### m
#### M
#### f
#### F
##
##Once they have completed the input successfully, (after either one or more
##iterations), show a message telling them the gender they chose.

##My Attempt (15 minute time limitation)
data = input('Hello, please input your gender\n')
success = False

while success == False:
    if data == 'm':
        break
    elif data == 'M':
        break
    elif data == 'f':
        break
    elif data == 'F':
        break
    else:
        print('You have entered an improper format for gender, please try again\n')
    data = input('Please input your gender again\n')

print('Thank you! The gender you entered is {}'.format(data))

##The program works, but I am unsure about how I went about it. The break
##statement exits the loop, so there is really not a need for the
##"success == False" condition of the while loop. Will take a look at the
##Proctor's solution to see how they went about it.

##Proctor Results - Answer
while True:
    gender = input('Gender: ')
    if(gender == 'M' or gender == 'm' or gender == 'f' or gender == 'F'):
        break
    else :
        print('Please try again')
    
print('You are: ',gender)


#Lesson 18 - Predefined String Functions (Using Strings as Objects)
##You can treat strings and lists as objects
string = ['s', 't', 'r', 'i', 'n', 'g']
for letter in string:
    print(letter)

string = 'string'
print(string)
print(string[:4])
print(string[:4:2])

string = 'this is a string of text, in a variable called string'
##count the number of times the letter 's' appears
print(string.count('s'))

##Capitalize the first letter of each word in the output
print(string.title())

##Capitalize the first letter of the string
print(string.capitalize())


#Lesson 19 - Predefined String Functions (Splitting and Joining Strings)
string = '-'
sequence = ['a','b','c','d','e','f']

##join the string varialbe to the sequence of the list
##this is not a concatenation to one end or another
##this will put the string object between each element of the list
print(string.join(sequence))

##split the string by defining where you want the string to be split at
string = 'a-b-c-d-e-f'
print(string.split('-'))

sequence = string.split('-')

for letter in sequence
    print(letter)
