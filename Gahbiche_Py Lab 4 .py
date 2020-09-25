'''

Python Lab #4

Yahya Gahbiche

'''

# 1

print("\n-1-")

WestCoast = ["Washington", "Oregon", "California", "Nevada"]
WestCoast[3] = "Idaho"
print(WestCoast)
print(len(WestCoast))

#2

print("\n-2-")

chars = ["Leslie", "Tom", "Ron"]
for i in chars:
    print(i, "is a character on Parks and Rec.")

#3

print("\n-3-")

import random;
randomList = []
for i in range (1,11):
    randomList.append(random.randint(1,10))
j = 0
while j < 10:
    if randomList[j] % 3 == 0:
        print(randomList[j])
    j += 1
    
#4

print("\n-4-")

list1 = ["New Years Day", "Easter", "Fourth of July"]
list2 = ["Halloween", "Thanksgiving", "Black Friday", "Christmas"]
def holList(list1, list2):
    holidays = list1 + list2
    newHolidays = []
    for i in range(len(holidays)):
        if holidays[i] != "Black Friday":
            newHolidays.append(holidays[i])
    print(newHolidays)
holList(list1,list2)

#5

print("\n-5-")

cities = ["New York", "Los Angeles"]
cities.append("Miami")
cities.append("Houston")
cities.insert(0,"Seattle")
cities.insert(2,"Boise")
del cities[0]
print(cities)

#6

print("\n-6-")

months = [["January", "31"],["February", "28"], ["March", "31"], ["April", "30"], ["May", "31"], ["June", "30"]]
for i in range(0,len(months)):
    print(months[i][0], "has", months[i][1], "days.")
        
#7

print("\n-7-")

dog = {"Breed":"Corgi","Age Exp.": 13,"Type": "Cattle herding"}
print(dog)
print(dog["Breed"])
print("The", dog["Breed"], "is expected to live about", dog["Age Exp."], "years.")

#8

print("\n-8-")

scores = {"Jeff":90,"Chris":59,"Hannah": 88,"Michelle": 99}
def addChangeScore (name, score):
    scores[name] = score
addChangeScore("Joel",78)
addChangeScore("Jeff",79)
def delScore (name):
    del scores[name]
delScore("Hannah")
for k,v in scores.items():
    print(k,v)
#9
    
print("\n-9-")

names = ["Jasper", "Sam", "Meredith", "Chris"] 
age = [23, 28, 20, 30]
myDictionairy = {}
zippingLists = list(zip(names,age))
for i in zippingLists:
    myDictionairy = dict(zippingLists)
print(myDictionairy)

#10

print("\n-10-")

scores = {"Jeff":90,"Chris":59,"Hannah": 88,"Michelle": 99}
for k,v in scores.items():
    if v > 60:
        print(k,"passed the test.")
    else:
        print(k,"did not pass the test.")
        

