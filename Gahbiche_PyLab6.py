'''

Python Lab #6

Yahya Gahbiche

'''
import numpy as np
import pandas as pd

# 1

print("\n-1-")

planets = np.array([['Mercury', 'Venus', 'Mars'], ['Jupiter', 'Saturn', 'Uranus'], ['Pluto']])
print(planets)


#2

print("\n-2-")

planets = np.array([['Mercury', 'Venus', 'Mars'], ['Jupiter', 'Saturn', 'Uranus'], ['Pluto']])
print(planets[0][1], "is the second planet from the sun.")
print(planets[2][0], "is not a planet.")

#3

print("\n-3-")

numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
sub1 = numbers[3:8:2]
sub2 = numbers[0:5:2]
product  = sub1 * sub2
print(product)
print(np.sqrt(sub2)) 


#4

print("\n-4-")

classes = ['Algebra I', 'Intro to Business', 'Creative Writing']
students = [30, 31, 29]
att = pd.Series(students, index = classes)
print(att)
att["Programming"] = 31
print('\n')
print(att[att < 31])


#5

print("\n-5-")
myData = {'Test 1': [92,72,98],
          'Test 2': [85,83,89],
          'Test 3': [83,99,61]}
myFunction = pd.DataFrame(myData, index =['Sean', 'Claude','Laura'])
print(myFunction)
print('\n')
myFunction.loc['Claude']['Test 2'] = 81
myFunction.loc['James'] = [72,83,99]
myFunction['Test 4'] = [69,71,72,83]
print(myFunction)

#we can also add the new row and column like the following: we swap the order of the 2 lines of code.
# The main thing is to maintain a consistant dimention of the DataFrame.
myFunction['Test 4'] = [69,71,72]
myFunction.loc['James'] = [72,83,99,83]


#6

print("\n-6-")

salesDict = {'Samsung Galaxy S10': [769.34, 834.23, 900.12, 1021.12],
             'iPhone X': [983.11, 881.21, 1210.32, 1100.34],
             'Google Pixel 4': [1021.18, 1321.12, 832.14, 992.15]}

dates = ['01/01/2020', '01/02/2020', '01/03/2020', '01/04/2020']
sales = pd.DataFrame(salesDict, index = dates)
print(sales)

meanFn = sales.loc[['01/01/2020', '01/02/2020', '01/03/2020', '01/04/2020']
,salesDict ].mean(axis = 1)

medianFn = sales.loc[['01/01/2020', '01/02/2020', '01/03/2020', '01/04/2020']
,salesDict ].median(axis = 1)

stDevFn = sales.loc[['01/01/2020', '01/02/2020', '01/03/2020', '01/04/2020']
,salesDict ].std(axis = 1)

sales["Mean"] = meanFn
sales["Median"] = medianFn
sales["St Dev"] = stDevFn
sales= sales.drop(["Samsung Galaxy S10","iPhone X","Google Pixel 4"], axis = 1)

print(sales)




