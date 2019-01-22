import psycopg2
from psycopg2.extras import DictCursor
dsn = "dbname='jojo' user='postgres' host='localhost' password='0905nikon' port='5432'"
psql = psycopg2
dcurs= DictCursor

class DataManage():

    def ClearAllInfo():
        print()

    def AddRecord(self , data):
        conn = psql.connect(dsn)
        curs = conn.cursor()
        curs.execute("")
        conn.commit()
        data=""
    
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
        conn.close()
    def LoadTeacherInfoBuIin(self):
        print()

    def GetPassword(self , username):
        conn = psql.connect(dsn)
        curs = conn.cursor(cursor_factory=DictCursor)
        curs.execute("SELECT * FROM manage_persons WHERE login='"+username+"'")
        return curs.fetchall()[0][2]
    def GetSeeasonByTeacher():
        print()

    def GetRateByTeacher():
        print()

    def GetIndicatorsByTeacher():
        print()

    def UpdateInfo():
        print()