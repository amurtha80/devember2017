#2017-12-02 Goal
##Learn some Python
##Get through at least 3 lessons from the following Udemy Course:
##Python for Beginners - LearnToProgram, Inc. (Alex Bowers)

#Lesson 5 - Else Statements
a,b = 0,1

if a == b:
    print(True)
else:
    print(False)


#Lesson 6 - Else-if (Elif) Statments
a,b = 1,1

if a > b:
    print('a is greater than b')
elif a < b:
    print('a is less than b')
else: 
    print('a is equal to b')


#Lesson 7 - Switch Statements Workaround
##Python does not have a switch statement so this is a workaround
switch = dict(
        one = 'one',
        two = 'true',
        three = 'three'
)
var = 'four'
##This get function is a way to produce a default value when the value
##from the variable is not listed in the dictionary.
##Otherwise you could do this - print(switch[two])
print(switch.get(var,'default'))


#Lesson 8 - Inline If Statement
a,b = 0,1

if a == b:
    print(True)
else:
    print(False)
    
var = 'This is true' if a == b else 'This is not true'
print(var)


#Chapter 3 Challenge - Truth Tables
##And Truth Table
a = 1
b = 0
if (a == 1 and b == 1):
    print('1')
elif ((a == 1 and b == 0) or (a == 0 and b == 1)):
    print('0')
elif (a == 0 and b ==0):
    print('0')
else:
    print('Invalid Input')
    
##OR truth table
a = 1
b = 0
if (a == 1 and b == 1):
    print('1')
elif ((a == 1 and b == 0) or (a == 0 and b == 1)):
    print('1')
elif (a == 0 and b ==0):
    print('0')
else:
    print('Invalid Input')
    
##Not truth table
a = 0
if(a == 1):
    print('0')
elif(a == 0):
    print('1')
else:
    print('Invalid Input')
    
##Main Challenge:
a = 1
b = 0
c = 1

if(b == 1):
    bNotVar = 0
elif(b==0):
    bNotVar = 1
    
if(a == 1 and bNotVAr == 1):
    innerBracket = 1
else:
    innerBracket = 0
    
if(innerBracket == 1 or c == 1):
    print('Q = 1')
else:
    print('Q = 0')
