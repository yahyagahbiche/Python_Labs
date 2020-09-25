'''

Python Lab #2

Yahya Gahbiche

'''

# 1

print("\n-1-")

var = 31
print("August has " + str(var) + " days.")

#2

print("\n-2-")

var1 = "September"    
var2 = "April"
var3 = "June"
var4 = "November"
statement = ("Thirty days have " + var1 + ", " + var2 + ", " + var3 + ", and " + var4 + ".")
print(statement)  

#3

print("\n-3-")

month = ("October")
if month == ("October"):
    print("31 days")
else: 
    print("30 days")

#4
    
print("\n-4-")

number = 70
if number % 5 == 0 and number % 10 == 0:
    print ("Number is divisible by 5 and 10.")
if number % 7 == 0 or number % 2 == 0:
    print ("Number is divisible by 7 or by 2.")

#5
    
print("\n-5-")

for x in range (1,11):
    print (x)

#6
    
print("\n-6-")

for y in range(6,21,3):
    print(y)


#7  
    
print("\n-7-")

for x in range (1,6) :
    print("Set:", x)
    if x % 2 == 0:
        for x in range (1,6) :
            print("Student", x)
        x += 1
        
#8
        
print("\n-8-")

z = 0
while z < 10:
    z += 1
    if z % 3 == 0:
        print(z)

#9

print("\n-9-")

def doCalc(num1, num2, num3):
    return ((num1 + num2) * num3)
doCalc(10,12,40)

#10

print("\n-10-")

def creditsPerQuarter(student, numCreds, numCourses) :
    TotalCredits = numCreds * numCourses
    print(student + " is taking " + str(numCourses) + " courses and each course is " + str(numCreds) +" credits for a total of " + str(TotalCredits)) 
creditsPerQuarter("Wade", 3, 4)
creditsPerQuarter("Jane", 3, 5)
creditsPerQuarter("Evan", 5, 3)

# 10 another method
print("\n-10-")
print("This second method includes casting the arguments numCreds and numCoures:\n")

def creditsPerQuarter(student, numCreds, numCourses) :
    print(student + " is taking " + str(numCourses) + " courses and each course is " + str(numCreds) + " credits for a total of " + str(int(numCreds) * int(numCourses)))
creditsPerQuarter("Wade", 3 , 4)
creditsPerQuarter("Jane", 3 , 5)
creditsPerQuarter("Evan", 5 , 3)
