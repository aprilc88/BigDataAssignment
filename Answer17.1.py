'''
Answer to 17.1
Student: April Carchedi
'''
import pandas as pd
import sqlite3

connection = sqlite3.connect('books.db')
pd.options.display.max_columns = 10

# Display authors last name in descending order.
# Added first names due to different authors with same last name.
print(pd.read_sql('SELECT last, first FROM authors ORDER by last DESC', connection))

# Display titles in ascending order.
print(pd.read_sql('SELECT title FROM titles ORDER by title ASC', connection))


# Use INNER JOIN to select all of the books for a specific author. Include the title, copyright year and ISBN.
# Order the information alphabetically by title.
print(pd.read_sql("""SELECT title, copyright
                     FROM titles INNER JOIN author_ISBN
                     ON titles.isbn = author_ISBN.isbn
                     ORDER BY title ASC""", connection).head())

print("Inserting new author and novel: ")

# Insert new author into the table.
cursor = connection.cursor()

cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Sue', 'Red')""")
print(pd.read_sql('SELECT last, first FROM authors ORDER by last DESC', connection))

# Insert new title for the author. 

cursor = cursor.execute("""INSERT INTO titles (title, isbn, edition, copyright) VALUES ('Book by Sue Red', '11111111', '1', '2020')""")
print(pd.read_sql('SELECT title FROM titles ORDER by title ASC', connection))

# Close the database.
connection.close()
'''
SAMPLE OUTPUT:

     last      first
0    Wald  Alexander
1   Quirk        Dan
2  Deitel       Paul
3  Deitel     Harvey
4  Deitel      Abbey
                              title
0         Android 6 for Programmers
1            Android How to Program
2                  C How to Program
3                C++ How to Program
4     Internet & WWW How to Program
5     Intro to Python for CS and DS
6               Java How to Program
7  Visual Basic 2012 How to Program
8          Visual C# How to Program
9         Visual C++ How to Program
                       title copyright
0  Android 6 for Programmers      2016
1  Android 6 for Programmers      2016
2  Android 6 for Programmers      2016
3     Android How to Program      2017
4     Android How to Program      2017
Inserting new author and novel: 
     last      first
0    Wald  Alexander
1     Red        Sue
2   Quirk        Dan
3  Deitel       Paul
4  Deitel     Harvey
5  Deitel      Abbey
                               title
0          Android 6 for Programmers
1             Android How to Program
2                    Book by Sue Red
3                   C How to Program
4                 C++ How to Program
5      Internet & WWW How to Program
6      Intro to Python for CS and DS
7                Java How to Program
8   Visual Basic 2012 How to Program
9           Visual C# How to Program
10         Visual C++ How to Program


'''
