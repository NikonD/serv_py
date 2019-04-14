#!rate_system/Scripts/python.exe
import argon2
import psycopg2

arg = argon2.PasswordHasher(hash_len=256 ,time_cost=10 ,memory_cost=100000)
str = "sagitov"
s = arg.hash(str)
print(s)
# dsn_web = "dbname='d9mcvnqqvv6qhr' user='dbdhjqxibocegm' host='ec2-176-34-113-195.eu-west-1.compute.amazonaws.com' password='a775c39e8b11b8b3a0c28a18a7b48aa2ba843588c0f754eadc75207cb626e7c8' port='5432'"
# conn = psycopg2.connect(dsn_web)
# curs = conn.cursor()
# curs.execute("INSERT INTO manage_person (login , password , priv_value) VALUES ( '" + username +"' , '" + password +"' , " + str(privileges) + ")")
# conn.commit()
# conn.close()



