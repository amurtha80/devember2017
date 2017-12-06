#2017-12-06 Goal
##Learn some Python
##Get through at least 3 lessons from the following Udemy course:
##Python for Beginners - LearnToProgram, Inc. (Alex Bowers)

#Chapter 5 Lab Exercise - Lists
##There is an algorithm that is used to sort a list of numeric values in their
##ascending order, which is called Bubble Sort.
##
##The way this algorithm works, is that it compares two values at a time, to see
##which value is larger. If the value on the left is larger then it will swap the
##two around. And after looping throughout the process it will have ordered the
##numbers properly. This starts from the left and travels right, once it reaches the
##end, it starts again.
##
##This process should be repeated until there is one complete pass through the set
##of numbers without any changes. Which means that the numbers are in the right
##order. Or until you have looped through N - 1 times, which is the maximum number
##of times needed. N is the number of numbers provided in the set.
##For this lab rearrange this number list using Bubble Sort:
##
##8, 7, 12, 4, 9, 6 and 5
##
##***Hint***: There will be a need for nested loops here, so be careful
##with indenting

##My Attempt (15 minute time limitation)
##list = [8,7,12,4,9,6,5]
##pos1 = 0
##pos2 = 1
##temp = 0
##
##for i in list:
##    if list[pos1] > list[pos2]:
##        ##
##        temp = list[pos1]
##        ##
##        list[pos1] = list[pos2]
##        ##
##        list[pos2] = temp
##    pos1 += 1
##    pos2 += 1
##print(list)
##
## ***EPIC FAIL LOL***
## Did not properly read through requirements of Lab Test, as well as picking
## up hint with nested loops. I basically built out the inner loop, to run
## through one pass, but not again. I got confused with the logic that this can
## be solved in N - 1 times, as it should be solved by the end of the first pass
## No idea why I was thinking this. >_<
## Also the variable pos2 gets an IndexError: list index out of range, because
## on the final iteration, it takes a value of 8 and there are only 7 values
## in the list.

## My modified attempt after reviewing proctor results
list = [8,7,12,4,9,6,5]
N = len(list)
while (N != 1):
    pos = 0

    while (pos < N - 1):
        if list[pos] > list[pos + 1]:
            temp = list[pos]
            list[pos] = list[pos + 1]
            list[pos + 1] = temp
        pos = pos + 1
    N = N - 1

print(list)

##Proctor Results - Answer
##Why does the proctor use the swapped boolean variable???
data = [8,7,12,4,9,6,5]
N = len(data)
swapped = True
while (swapped == True or N != 1):
    swapped = False
    position = 0
    
    while (position < N - 1):
        if (data[position] > data[position + 1]):
            temp = data[position]
            data[position] = data[position + 1]
            data[position + 1] = temp
            swapped = True
        position = position + 1
    N = N - 1
    
print(data)


#Lesson 16 - Input "Press any Key to Continue"
##With Python 3.x you can use the input function on its own to receive
##input from a user that can be incorporated into a program
print('Hello, Andy')
input('Press any key to continue')
print('Thank you')

#Lesson 17 - Data Input
##Use an escape prior to quote to include it in the quoted string
##Use a new line escape at the end so input is on a new line
data = input('What\'s your name?\n')
print('Hello, {}'.format(data))

##Here you need to make sure to use the int function to typecast the string
##we received from the input
data = input('\nWhat\'s your favorite number?\n')
data = int(data) * 20
print('Your number times 20 is {}'.format(data))
