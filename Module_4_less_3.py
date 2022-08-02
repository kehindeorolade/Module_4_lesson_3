import sqlite3

con = sqlite3.connect('d_students.db')


cur = con.cursor()

# Create table
#cur.execute('''CREATE TABLE s_information
            #(first_name text, last_name text, course text, age real)''')

# Insert a row of data
#cur.execute("INSERT INTO s_information VALUES ('Ade','Ola','product_design', 29)")

# Save (commit) the changes
con.commit()

print("successful")

s_data = [
   ('Ajayi', 'Bayowa', 'software development', 30,),
   ('Ademide', 'Benson', 'data science', 23,),
    ('Olawale', 'Saheed', 'UI/UX', 18,),
]


# cur.executemany('INSERT INTO s_information VALUES(?, ?, ?, ?)', s_data)

# print("execution successful")

for row in cur.execute('SELECT * FROM s_information'):
     print(row)

print(cur.fetchall())



#alter table statement 
#cur.execute("alter table s_info rename to s_information")
#con.commit()

#add a new column
# cur.execute("alter table s_information add column email")
# con.commit()

#update column
cur.execute(""" update s_information set email = 'kehindeorolade@gmail.com' """)
con.commit()
