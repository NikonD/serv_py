import psycopg2
from psycopg2.extras import DictCursor
from app.QueryFactory import QF
dsn = "dbname='jojo' user='postgres' host='localhost' password='0905nikon' port='5432'"
psql = psycopg2
dcurs= DictCursor
qf=QF()
class DataManage():

    def ShowAll(self):
        conn = psql.connect(dsn)
        curs = conn.cursor()
        curs.execute(qf.select_all())
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

    def GetTeacherRateByIin(self , IIN):
        conn = psql.connect(dsn)
        curs = conn.cursor()
        curs.execute(qf.get_teacher_rate_by_iin(IIN))
        return curs.fetchall()

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