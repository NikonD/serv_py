import psycopg2
from psycopg2.extras import DictCursor
from app.QueryFactory import QF

dsn_web = "dbname='d9mcvnqqvv6qhr' user='dbdhjqxibocegm' host='ec2-176-34-113-195.eu-west-1.compute.amazonaws.com' password='a775c39e8b11b8b3a0c28a18a7b48aa2ba843588c0f754eadc75207cb626e7c8' port='5432'"
dsn = "dbname='rate_system' user='postgres' host='localhost' password='jojodio' port='5432'"
psql = psycopg2
dcurs= DictCursor
qf=QF()
class DataManage():

    def Connect(self):
        conn = psql.connect(dsn_web)
        curs = conn.cursor(cursor_factory=DictCursor)
        return  curs

    def ShowAll(self):
        curs = self.Connect()
        curs.execute(qf.select_all())
        return curs.fetchall()
                                                          
    def AddRecord(self , data):
        conn = psql.connect(dsn_web)
        curs = conn.cursor()
        curs.execute("")
        conn.commit()
    
    def GetIDTeacherByIIN(self , iin):
        curs = self.Connect()
        curs.execute("SELECT id_teacher FROM teachers WHERE iin_teacher = %s " , (iin,))
        return curs.fetchall()[0][0]
    
    def GetAllRecordsByTable(self , table ):
        curs = self.Connect()
        curs.execute("SELECT * FROM "+table)
        return curs.fetchall()

    def EditRecord(self , table , index):
        conn = psql.connect(dsn_web)
        curs = conn.cursor()
        curs.execute("UPDATE ")
        conn.commit()

    def GetTeacherRateByIin(self , IIN):
        curs = self.Connect()
        curs.execute(qf.get_teacher_rate_by_iin(IIN))
        return curs.fetchall()

    def GetPassword(self , username):
        curs = self.Connect()
        curs.execute("SELECT password FROM manage_persons WHERE login= %s" , (username,))
        return curs.fetchall()[0][0].strip()

    def GetSeeasonByTeacher(self):
        print()

    def GetRateByTeacher(self , id_teach):
        curs = self.Connect()
        curs.execute("SELECT val_rate , id_indicator FROM rate WHERE id_teacher = %s" ,(id_teach,))
        return curs.fetchall()

    #dev
    def GetIndicators(self):
        curs = self.Connect()
        curs.execute("SELECT * From indicator")
        return curs.fetchall()
    #dev
    def GetIINs(self):
        curs = self.Connect()
        curs.execute("SELECT * From teachers")
        return curs.fetchall()