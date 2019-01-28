import psycopg2
from psycopg2.extras import DictCursor
dsn = "dbname='jojo' user='postgres' host='localhost' password='0905nikon' port='5432'"
psql = psycopg2
dcurs= DictCursor

class DataManage():

    def ShowAll(self):
        conn = psql.connect(dsn)
        curs = conn.cursor()
        curs.execute("SELECT * FROM select_all")
        return curs.fetchall()


    def AddRecord(self , data):
        conn = psql.connect(dsn)
        curs = conn.cursor()
        curs.execute("")
        conn.commit()
    
    def GetIDTeacherByIIN(self , iin):
        conn =psql.connect(dsn)
        curs = conn.cursor(cursor_factory=DictCursor)
        curs.execute("SELECT id_teacher FROM teachers WHERE iin_teacher = %s " , (iin,))
        return curs.fetchall()[0][0]
    
    def GetAllRecordsByTable(self , table ):
        conn = psql.connect(dsn)
        curs = conn.cursor(cursor_factory=DictCursor)
        curs.execute("SELECT * FROM "+table)
        return curs.fetchall()

    def EditRecord(self , table , index):
        conn = psql.connect(dsn)
        curs = conn.cursor()
        curs.execute("UPDATE ")
        conn.commit()

    def LoadTeacherInfoBuIin(self):
        print()

    def GetPassword(self , username):
        conn = psql.connect(dsn)
        curs = conn.cursor(cursor_factory=DictCursor)
        curs.execute("SELECT password FROM manage_persons WHERE login= %s" , (username,))
        return curs.fetchall()[0][0].strip()

    def GetSeeasonByTeacher():
        print()

    def GetRateByTeacher(self , id_teach):
        conn = psql.connect(dsn)
        curs = conn.cursor(cursor_factory=DictCursor)
        curs.execute("SELECT val_rate , id_indicator FROM rate WHERE id_teacher = %s" ,(id_teach,))
        return curs.fetchall()

    def GetIndicators(self):
        conn = psql.connect(dsn)
        curs = conn.cursor()
        curs.execute("SELECT * From indicator")
        return curs.fetchall() 