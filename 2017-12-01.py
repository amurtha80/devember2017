#2017-12-01 Goal
##Learn some Python
##Get through at least 3 lessons from the following Udemy Course:
##Python for Beginners - LearnToProgram, Inc. (Alex Bowers)

#Lesson 1 - Python Hello World Code
print("Hello, World");

#Lesson 2 - Variables
number=500
print(number)
print(type(number));

text = "This is some text"
print(text)
print(type(text));


#Lesson 3 - Data Types
##Numbers
##Integers
i = 150
print(type(i),i)

##float
f = 150.0
print(type(f),f)

##string
s = 'String'
m = '''\
Multi
Line
String\
'''

print(type(s),s)
print(type(m),m)

a = 'Andy'
s2 = 'Welcome, {}'.format(a)
print(s2)

##Lists and Tuples
##Tuples - can't be modified
t = (1,2,3,4)
print(type(t),t)

##Lists - can be modified
l = [1,2,3,4,5]
l.append(6)
print(type(l),l)

##Array / Dictionary
d = {'one':1,'two':2}
d2 = dict(
          one = 1,
          two = 2)
print(type(d),d)
print(type(d2),d2)

##Boolean
t1 = True
t2 = False

if t1 == t2:
    print(t1) #True
else:
    print(t2) #False

#Lesson 4 - If Statements
a,b = 2,2

if  a == b:
    print(True);
if  a != b:
    print(True);
if  a < b:
    print(True);
if  a > b:
    print(True);
if a <= b:
    print('This is true');
if  a >= b:
    print(True); #not =>
if  a == b and b > 1:
    print(True);    
