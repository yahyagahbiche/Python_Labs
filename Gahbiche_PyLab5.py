'''

Python Lab #5

Yahya Gahbiche

'''

# 1

print("\n-1-")

with open ("DataSamples/DontQuit.txt", "r") as reader:
    print(reader.readline())

# 2
    
print("\n-2-")

with open ("DataSamples/DontQuit.txt", "r") as reader:
    line = reader.readline()
    while line != '':
        print(line, end = '')
        line = reader.readline()

#3
        
print("\n-3-")

with open ("DataSamples/DontQuit.txt", "r") as reader:
    for line in reader: 
        if "Life " in line:
            print(line, end = '')
    
#4
            
print("\n-4-")

mylist = ["Please excuse my dear Aunt Sally\n", "Roy G. Biv\n"]
with open ("DataSamples/famousSayings.txt", "w+") as writer:
    writer.write("My very excited mother just served us nine pies.\n") 
    writer.writelines(mylist)
with open ("DataSamples/famousSayings.txt", "r") as reader:
    for line in reader:
        print(line, end ='') 
        
#5

print("\n-5-")

seq = "Will a jolly man make a jolly visitor?"
with open ("DataSamples/famousSayings.txt", "a+") as reader:
    reader.writelines(seq)
with open ("DataSamples/famousSayings.txt", "r") as reader:
    for line in reader:
        print(line, end ='')

#6
        
print("\n-6-")

import csv
amtCollected = []
with open ("DataSamples/SalesJan2009.csv", "r+") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter = ',')
    for row in csv_reader:
        amtCollected.append(row["Price"])
    for i in range(0, len(amtCollected)): 
        amtCollected[i] = int(amtCollected[i]) 
    total = sum(amtCollected)
    avg = total / len(amtCollected)
    print(f"Total is ${total}") 
    print(f"Average price is ${round(avg,2)}")
 
       
#7
    
print("\n-7-")

import csv
with open ("DataSamples/DogWeights.csv", "w+", newline = '') as csv_file:
    fieldnames = ["Name", "Weight"]
    writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow({"Name" : "Spot", "Weight" : 53})
    writer.writerow({"Name" : "Sadie", "Weight" : 22})
    writer.writerow({"Name" : "Sammie", "Weight" : 24})
    writer.writerow({"Name" : "Jasper", "Weight" : 45})   
with open ("DataSamples/DogWeights.csv", "r", newline = '') as reader:
    for line in reader:
        print(line, end ='')
        

