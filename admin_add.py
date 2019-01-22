
import argon2
import psycopg2
from psycopg2.extras import DictCursor
arg = argon2.PasswordHasher()

username = "admin"
password = "jojo1234"
privileges = 0

h = arg.hash('')
print(h)

# conn = psycopg2.connect("dbname='jojo'"
#                         "user='postgres'"
#                         "host='localhost'"
#                         "password='0905nikon'"
#                         "port='5432'"
#                         )
# curs = conn.cursor()
# curs.execute("INSERT INTO manage_person (login , password , priv_value) VALUES ( '" + username +"' , '" + password +"' , " + str(privileges) + ")")
# conn.commit()
# coon.close()
