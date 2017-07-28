#working

import os, sys
import psycopg2  # database connection
# Data base connection
#conn = psycopg2.connect(dbname="SOD_local_28_02", user="10SOD", host="localhost", password="10sod")
try:
    conn = psycopg2.connect(dbname="SOD_local_28_02", user="10SOD", host="localhost", password="10sod")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()
try:
    query = "SELECT * from res_partner limit 20";
    if query:
        print "Query executed"
except:
    print "Values false, check table_name name or field name"
cur.execute(query)
rows = cur.fetchall()
print len(rows)
print sorted(rows)
print max(sorted(rows))
for val,row in enumerate(rows):
    print "Id--> {} and name is --> {}".format( val,row[1])
conn.close()
