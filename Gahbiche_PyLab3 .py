'''

Python Lab #3

Yahya Gahbiche

'''

# 1

print("\n-1-")

var = "Excelsoir!"
print(var[1])
print(var[9])

#2 

print("\n-2-")

var = "Avengers Assemble"
i = 0
while i < len(var):
    print(var[i])
    i += 1
print("\n!")
    
#3

print("\n-3-")

school = "Hogwarts"
first = school[0:3]
second = school[3:8]
print(first)
print(second)
print(school[-1])

#4

print("\n-4-")
    
HogwartsSchool = ('Hufflepuff', 'Gryffindor', 'Ravenclaw', 'Slytherin')
for i in HogwartsSchool:
    print(i)
 
#5
    
print("\n-5-")

colorSet1 = ('Red', 'Blue')
colorSet2 = ('Green', 'Yellow')
rainbow = colorSet1 + colorSet2
print(rainbow)


#6

print("\n-6-")
 
superhero = ('Batman','Superman', 'Aquaman', 'Deadpool')
for i in range (0, len(superhero)):
    if superhero[i] == 'Deadpool':
        print("") # returning nothing
    else:
        print(superhero[i])
    i += 1
    
# 6 second method   
    
print("\n-6-\nMethod 2\n")

superhero = ('Batman','Superman', 'Aquaman', 'Deadpool')
for i in range (0, len(superhero)):
    if superhero[i] != 'Deadpool':
        print(superhero[i])
    i += 1
   

#7
    
print("\n-7-")

friends = ('Monica', 'Joey', 'Chandler')
print(friends[1])
married = friends[0] + " and " + friends[2]
print(married)

#8

print("\n-8-")

friends = ('Monica', 'Joey', 'Chandler')
mrTribbani = friends[1]
slicedName = mrTribbani[1:3]
print(slicedName)



#9

print("\n-9-")

months = ('January', 'February', 'March', 'April')
def monthDays(months):
    for i in range(0,len(months)):
        if months[i] == 'January' or months[i] == 'March':
            print(months[i] + " has 31 days.")
        if months[i] == 'February':
            print(months[i] + " has 28 days.")
        if months[i] == 'April':
            print(months[i] + " has 30 days.")
    i += 1
monthDays(months)

#9 second method: 

print("\n-9-\nMethod 2")

months = ('January','February','March','April')
def monthDays(tup):
  for i in tup:
    if i == 'January' or i == 'March':
      print(i + " has 31 days.")
    elif i == 'February':
      print(i + " has 28 days.")
    elif i == 'April':
      print(i + " has 30 days.")
monthDays(months)

#10 

print("\n-10-")

import random
def getRands(ceiling):
    for j in range(0,10):
        var = random.randint(1, ceiling)
        if var < 3:
            print (var)
getRands(10)
