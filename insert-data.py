import sqlite3

db = sqlite3.connect('data/kypipe_db')
cursor = db.cursor()
cursor.execute('''SELECT name, desc, type, image FROM tbl_object''')
#obj1 = cursor.fetchone() #retrieve the first row
#print(obj1[0]) #Print the first object

all_rows = cursor.fetchall()
for row in all_rows:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

cursor.execute('''SELECT object_id, property_id FROM tbl_property_list''')
#obj1 = cursor.fetchone() #retrieve the first row
#print(obj1[0]) #Print the first object

all_rows = cursor.fetchall()
for row in all_rows:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1}'.format(row[0], row[1]))