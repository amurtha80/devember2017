#2017-12-10 Goal
##Learn some Python
##Get through at least 3 lessons from the following Udemy course:
##Python for Beginners - LearnToProgram, Inc. (Alex Bowers)


#Lab Exercise 7 - Pre-defined string functions
##Within API’s (Application Programming Interface) you usually have to provide a
##Username or ID and a Secret Key, and have them provided to you. Most of these
##are provided together with a separator.
##
##I want you to check this as follows:
##
##  82914656273523:a4edFea2786DGex
##
##You should separate this into two separate variables, and then we will do
##some validation on these.
##The format is id:key
##The ID should always contain only digits (number 0-9) and be of length 14
##The Key can contain characters. It can also be any length over 10 characters
##and but less than 20 characters.
##If all the credentials are okay, then just print out: ‘All is good’, if they
##aren’t okay, display an appropriate message.

##My Attempt - limited myself to 30 minutes
apiAcct = '82914656273523:a4edFea2786DGex'

#Split out ID and Key
apiList = apiAcct.split(":")
username = apiList[0]
print(username)
key = apiList[1]
print(key)

##Determine if the criteria for the ID and key are met, or not, and display
##the appropriate output.
if (len(username) != 14):
    print('ID does not contain the corret number of digits, \n \
please check to make sure you have the right ID')
##This elif statement was the only part of the code I got stuck on
elif (not username.isdigit()):
    print('ID is not a numeric value, \n \
please check to make sure you have the right ID')
elif (10 >= len(key) or 20 <= len(key)):
    print('Key does not contain the correct range of characters \n \
please check to make sure you have the right key')
else:
    print("All is good")

#Solution Suggested by Proctor
passed = '82914656273523:a4edFea2786DGex'

data = passed.split(':')

id = data[0]
key = data[1]
if(id.isdigit()):
    # Number is numeric.
    if(len(id) == 14):
        #Length of 14
        if(len(key) > 10 and len(key) < 20):
            print('ID and Key are valid')
        else:
            print('Key Length isn\'t valid')
    else:
        print('ID wrong length')
else:
    print('ID isn\'t a digit')

##Commentary - I went bck into the lessons I am studying, and there is nothing
##regarding any pre-defined string functions that are in his suggested solution.
##This does not mean I am not resourceful, however, I had expectations that
##I would be able to use what I learned from the lessons to help me problem
##solve for the lab exercises. If I knew I would need to have to google or
##comb through documentation, would have been happy to do that, just would
##rather have exercises that allow me to apply what I learn, not have to visit
##Google/Stackoverflow to help me solve problems.


#Lesson 20 - Custom Functions (Syntax Overview)
def function_name(
    ## just a comment to state you can enter parameters here
    ):
    "This is a tagline"

    return "Hello"

print(function_name())


#Lesson 21 - Custom Functions (More Parameters)
list1 = [1,2,3,4]

def function_name(lists):
    "This will simply demonstrate by reference"
    lists.append([5,6,7,8]);
    print("This is the value: ",lists)
    return

print("The values are: ",list1)
function_name(list1)
print("The values are: ",list1)


#Lesson 22 - Custom Functions (More on Returns)
def function():
    return "Hello";

print(function())

def function():
    return ;

##Will provide a value of None
##You need to have a return statement in all of your functions
print(function())
var = function()
print(var)
if var == None:
    print("True")
