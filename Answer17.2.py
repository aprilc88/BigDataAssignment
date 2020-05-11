'''
Answer to 17.1
Student: April Carchedi
use cursor method execute to select all the data in the titles table,
then use description and fetchall to display the data in tabular format.
'''
import pandas as pd
import sqlite3

connection = sqlite3.connect('books.db')

# Call cursor method
cursor = connection.cursor()

# Select all data from titles
row = cursor.execute("""SELECT isbn, title, edition, copyright FROM titles""")

# Display description
print("Description: ")
print(cursor.description)

# Display fetchall
print("Fetchall: ")
fetch = cursor.fetchall()
print(fetch)

# Close the connection
connection.close()
'''
SAMPLE OUTPUT:
Description: 
(('isbn', None, None, None, None, None, None),
('title', None, None, None, None, None, None),
('edition', None, None, None, None, None, None),
('copyright', None, None, None, None, None, None))
Fetchall: 
[('0135404673', 'Intro to Python for CS and DS', 1, '2020'),
('0132151006', 'Internet & WWW How to Program', 5, '2012'),
('0134743350', 'Java How to Program', 11, '2018'),
('0133976890', 'C How to Program', 8, '2016'),
('0133406954', 'Visual Basic 2012 How to Program', 6, '2014'),
('0134601548', 'Visual C# How to Program', 6, '2017'),
('0136151574', 'Visual C++ How to Program', 2, '2008'),
('0134448235', 'C++ How to Program', 10, '2017'),
('0134444302', 'Android How to Program', 3, '2017'),
('0134289366', 'Android 6 for Programmers', 3, '2016')]

'''
