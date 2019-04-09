#!rate_system/Scripts/python.exe
# import argon2
import psycopg2
dsn_web = "dbname='d9mcvnqqvv6qhr' user='dbdhjqxibocegm' host='ec2-176-34-113-195.eu-west-1.compute.amazonaws.com' password='a775c39e8b11b8b3a0c28a18a7b48aa2ba843588c0f754eadc75207cb626e7c8' port='5432'"

# from psycopg2.extras import DictCursor
# arg = argon2.PasswordHasher()
conn = psycopg2.connect(dsn_web)
curs = conn.cursor()
curs.execute("SELECT * FROM teachers CROSS JOIN rate")
curs.fetchall()
conn.commit()


