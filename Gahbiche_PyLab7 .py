'''

Python Lab #7

Yahya Gahbiche

'''

# 1

print("\n-1-")

import pyodbc
conn= pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                     'Server=LAPTOP-M8HE6O54\SQLEXPRESS;'
                     'Database=ExcelsiorMobile;'
                     'Trusted_Connection=yes;')
cursor= conn.cursor()

cursor.execute('SELECT * FROM DirNums')
row = cursor.fetchone()
if row:
    print(row)

#2
    
print("\n-2-")

cursor= conn.cursor()

cursor.execute('SELECT * FROM LastMonthsUsage ')
row = cursor.fetchone()
if row:
    print(row)
    
#3

print("\n-3-")

cursor.execute('SELECT SUM(Total) FROM Bill')
row = cursor.fetchone()
if row:
    val = row 
    print(val)

#4 


    



'''
Save the sum of the Total column in the Bill table to the cursor.
 Save only the value of the result of that query into a variable called val.
 Now print val.
'''













