import argon2
import psycopg2
from psycopg2.extras import DictCursor
arg = argon2.PasswordHasher()

username = "Erich"
password = "hartmann"
privileges = 1

h = arg.hash(password)
print(h)

conn = psycopg2.connect("dbname='jojo'"
                        "user='postgres'"
                        "host='localhost'"
                        "password='0905nikon'"
                        "port='5432'"
                        )
curs = conn.cursor()
curs.execute("INSERT INTO manage_persons (login , password , priv_value) VALUES ( %s , %s ,%s )" , (username , h , privileges))
conn.commit()

