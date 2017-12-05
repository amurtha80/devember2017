#2017-12-05 Goal
##Learn some Python
##Get through at least 3 lessons from the following Udemy course:
##Python for Beginners - LearnToProgram, Inc. (Alex Bowers)

#Chapter 4 Lab Exercise - Loops and Flow Control
##Within math, there is something called the Fibonacci Sequence.
##It is a sequence of numbers by which you add the previous two numbers together.
##It follows this format:
##
##Fn = (Fn - 2) + (Fn - 1)
##
##with initial values of F0 = 0 and F1 = 1
##
##This sequence is truly something amazing, and is found throughout nature.
##I implore you to read up about it when you get time it really is fascinating!
##However, your task is to create a sequence of numbers for the Fibonacci
##Sequence and stop at the first number that is greater than 100.
F0, F1, Fn = 0, 1, 0
print(F0)
print(F1)

while Fn <= 100:
##    if F0 == 0 and F1 == 1:
    Fn = F0 + F1
    F0 = F1
    F1 = Fn
    print(Fn)

##Solution suggested by proctor. Did not include printing of F0 and F1 in
##sequence. Leveraged break statement from Chapter 4 lessons.
f0 = 0
f1 = 1
set = False
while True:
    fn = f0 + f1
    f0 = f1
    f1 = fn
    if (fn > 100):
        set = True
    else:
        set = False
    print(fn)
    if (set == True):
        break
        

#Lesson 13 - Lists
##Remember that the index starts with 0, and not 1, and negative index
##will start from the end of the list
list = [1,2,3,4,5,6,7,8,9,10,11]

print(list)
print(list[2])
print(list[-4])

##Another way to call print(list[-4]), although not as efficient
length = len(list)
print(list[length-4])

##[x:y] where x is the start position and y is the end position of the list
print(list[2:5])
print(list[1:8])
##[x:y:z] where z is the stepper between the start and end position of list
print(list[1:8:2])      
print(list[:4:2])


#Lesson 14 - Modifying Lists
##Append a value to the list
list = [1,2,3,4,5,6,7,8,9,10,11]
list.append(12)
print(list)

##Extend a list with another list
list = [1,2,3,4,5,6,7,8,9,10,11]
list2 = [12,13,14]
list.extend(list2)
print(list)

##insert a value into the list in a specific position(replacing original value)
list = [1,2,3,4,5,6,7,8,9,10,11]
list.insert(5,12)
print(list)

##Change a value in the list via assignment
list = [1,2,3,4,5,6,7,8,9,10,11]
list[5] = 12
print(list)

##Change a value on the list by using an expression
list = [1,2,3,4,5,6,7,8,9,10,11]
list[5] = list[5] * 2
print(list)

##delete certain values from the list based on position
list = [1,2,3,4,5,6,7,8,9,10,11]
del list[5:7]
print(list)

##removes the value from the list
list = [1,2,3,4,5,6,7,8,9,10,11]
list.remove(9)
print(list)
list = [1,2,3,4,5,6,7,8,9,10,11, 'one']
list.remove('one')
print(list)

##removes the value from the list in a specific position
list = [1,2,3,4,5,6,7,8,9,10,11]
list.remove(list[9])
print(list)

##append a 0 to the beginning of a list
list = [1,2,3,4,5,6,7,8,9,10,11]
list.reverse()
list.append(0)
list.reverse()
print(list)


#Lesson 15 - Sorting Lists
##Order an unordered list
list = [1,3,4,2,5]
list.sort()
print(list)

##Create new variable and assign the list to that variable and sort it.
list = [1,3,4,2,5]
list2 = sorted(list)
print(list2)

##Create new variable, assign list to that variable, sort it, and reverse
##the order
list = [1,3,4,2,5]
list2 = sorted(list)
list2.reverse()
print(list2)
