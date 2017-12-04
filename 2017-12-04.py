#2017-12-04 Goal
##Learn some Python
##Get through at least 3 lessons from the following Udemy course:
##Python for Beginners - LearnToProgram, Inc. (Alex Bowers)


#Lesson 9 - While Loop Statement
##While a condition remains true, continue to execute instructions
##Watch out to make sure that any instructions following code block
##Are not located within the while loop code block or you might get errors
a = 0
while a < 100:
    print(a)
    a += 1
print('This is finished')


#Lesson 10 - For Loop Statement
##For the number of times that a programmer wants the condition
##to be executed, continue to execute instructions
##For loop is a more powerful loop and is used more often than while loop

##enumerate function is used here to place a value for each position in the
##string, instead of each character of the string being printed
for key,data in enumerate('strings'):
    if key % 2 == 0:
        print('The letter {} is in an even location'.format(data))

for list in [1,2,3,4,5]:
    print(list)

#Lesson 11 - Try-Except-Finally Code
##We can throw errors if needed
tuple = (1,2,3,4,5)
try:
    tuple.append(6)
    for each in tuple:
        print(each)
##This is a more reader friendly of what the error is actually is. In this
##case we know that you cannot append to a tuple.
except AttributeError as e:
    print('Error formed: ' , e)
##This is an example for input/output for files. This will not get read
##for this example but is just another idea of what could be entered here.
except IOError as e:
    print('File not found:', e)


#Lesson 12 - Break, Continue and Else Code
##Flow control for loops - continue will keep the flow control for the
##loop going
list = [1,2,3,4,5,6,7,8,9]
for int in list:
    if int == 7:
        continue
    else:
        print(int)
else:
    print('default')

##break can stop the flow control of the loop
list = [1,2,3,4,5,6,7,8,9]
for int in list:
    if int == 7:
        break
    else:
        print(int)
