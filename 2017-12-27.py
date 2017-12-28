#2017-12-27
##Learn some Python
##Get through at least 3 lessons from the following Udemy course:
##Python for Beginners - LearnToProgram, Inc. (Alex Bowers)


#Lab Exercise 9 - Classes
##1. We will create a class that calculates a person’s payroll. 
##  Pass in their information, which includes:
##      -Name -How much they earn per hour
##      -How many hours they have worked that week.
##
##  This will then generate a value, which we will output.
##
##2. Also, create an optional method that will note whether they worked overtime.
##  If they did, they get time-and-a-half pay for the hours they worked overtime.
##3. After all of this:
##  A. Print out their name, how many normal hours they work at what wage,
##      and how much money earned for that.
##  B. Then another printout for over time.
##  C. Finally, a printout of the total for both added together.


##My Attempt - No time limit
class Payroll:
    def __init__(self, name):
        self.name = name
        self.hours = 0
        self.extraHours = 0
        self.wage = 0

    def setEarnings(self, wage):
        self.wage = wage
    
    def setHours(self, hours):
        self.hours = hours

    def setOvertime(self, hours = 0):
        self.extraHours = hours

    def payrollReport(self):
        print(self.name, ' worked:\n')
        regularPay = self.hours * self.wage
        print(self.hours, ' regular hours @', self.wage, 'for $', regularPay, '\n')
        overWage = self.wage * 1.5
        overPay = self.extraHours * (1.5 * self.wage)
        print(self.extraHours, ' overtime hours @', overWage, ' for $', overPay, '\n')
        print('Total Payroll: $', regularPay + overPay, ' for current pay period')

andy = Payroll('Andy')
andy.setEarnings(50.00)
andy.setHours(40.00)
andy.setOvertime(6.00)
andy.payrollReport()

##I tried to come up with a more elegant solution, using **kwargs (dictionary) and
##I had some problems with the various data types for the methods that I created.
##The attempt I came up with was trying to pass multiple people with their data as
##lists into objects so I could spit out a payroll report, instead of trying to
##input the information one at a time. After looking at the proctor solution,
##I decided to go back and "keep it simple stupid". Perhaps something that I might
##come back to later.


##Proctor Solution
class Payroll:
    def __init__(self, name):
        self.name = name
        self.hours = 0
        self.overHours = 0
        self.wage = 0
    def setEarnings(self, wage):
        self.wage = wage
    def setHours(self,hours):
        self.hours = hours
    def setOvertime(self,hours = 0):
        self.overHours = hours
    def calculate(self):
        print(self.name , ' worked:')
        print(self.hours , ' normal hours @ ' , self.wage , ' for $' , self.hours * self.wage)
        print(self.overHours , ' overtime hours @ ' , self.wage * 1.5 , ' for $' , self.overHours * 1.5 * self.wage)
        print('Totalling: $' , ((self.wage*1.5*self.overHours)+ (self.wage*self.hours)) , ' for One Weeks work')
        
alex = Payroll('Alex')
alex.setEarnings(14.20)
alex.setHours(4.2)
alex.setOvertime(1)
alex.calculate()


#Lesson 28 - File Handling (Opening Files)
file = open('text.txt')

for line in file:
    #to avoid spacing between lines, use the end option as the print function uses
    #character return as a default option
    print(line, end = '')


#Lesson 29 - File Handling (Reading and Writing Text Files)
##There are other option for the open 2nd option, use help to explore    
source = open('text.txt')
output = open('output.txt', "w")

for line in source:
    print(line, file = output, end = '')


buffersize = 100000
input = open('bigfile.txt')
output = open('newbigfile.txt', "w")
buffer = input.read(buffersize)
bufferlimit = 1000000

##limit the amount of text output to the new file.
while bufferlimit > 0:
    output.write(buffer)
    print('.', end = '')
    bufferlimit = bufferlimit - buffersize
print('\n')

while len(buffer):
    output.write(buffer)
    print('.', end = '')
    buffer = input.read(buffersize)
print('\n')


#Lesson 30 - File Handling (Reading and Writing Binary Files)
buffersize = 100000
input = open('keyboard_bokeh.jpg', "rb")
output = open('image2.jpg', "wb")
buffer = input.read(buffersize)

##will read jpeg file as binary and output to new file, exact same image
while len(buffer):
    output.write(buffer)
    print('.', end = '')
    buffer = input.read(buffersize)
print('\n')
