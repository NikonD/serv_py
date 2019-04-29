import psycopg2
from psycopg2.extras import DictCursor
from app.database.QueryFactory import QF
from argon2 import PasswordHasher , exceptions

dsn_web = "dbname='d9mcvnqqvv6qhr' user='dbdhjqxibocegm' host='ec2-176-34-113-195.eu-west-1.compute.amazonaws.com' password='a775c39e8b11b8b3a0c28a18a7b48aa2ba843588c0f754eadc75207cb626e7c8' port='5432'"
dsn = "dbname='rate_system' user='postgres' host='localhost' password='jojodio' port='5432'"
psql = psycopg2
dcurs= DictCursor
qf  =   QF()
ph  =   PasswordHasher(time_cost=5,hash_len=100)

class DataManager():

    def Connect(self):
        conn = psql.connect(dsn_web)
        curs = conn.cursor()
        return  curs

    def CheckUser(self , username):
        curs = self.Connect()
        curs.execute("SELECT * FROM manage_persons WHERE manage_persons_login = '%s'" %(username,))
        if curs.fetchall():
            return True
        else:
            return False

    def GetDate(self):
        curs = self.Connect()
        curs.execute("select * from season")
        return curs.fetchall()

    def ShowAll(self):
        curs = self.Connect()
        curs.execute(qf.select_all())
        return curs.fetchall()

    def user_is_exist(self , log):
        is_user = False
        curs = self.Connect()
        curs.execute("SELECT manage_persons_login FROM manage_persons WHERE manage_persons_login = '%s'" % (log,) )
        if curs.fetchall():
            return True
        else:
            return False


    def AddUser(self ,login , password , privileges):
        conn = psql.connect(dsn_web)
        curs = conn.cursor()
        if  self.user_is_exist(login):
            print('user is exist')
            return False
        #     not add user
        else:
            print('user is not exist')
        #     add user
            h_password = ph.hash(password)
            curs.execute(qf.add_user_in_manage_persons(login,h_password,privileges))
            conn.commit()

    def GetIDTeacherByIIN(self , iin):
        curs = self.Connect()
        curs.execute("SELECT id_teacher FROM teachers WHERE iin_teacher = %s " , (iin,))
        return curs.fetchall()[0]

    def GetAllRecordsByTable(self , table ):
        curs = self.Connect()
        curs.execute("SELECT * FROM "+table)
        return curs.fetchall()

    def VerifyPassword(self , login , password):
        curs = self.Connect()
        curs.execute("SELECT manage_persons.manage_persons_password FROM manage_persons WHERE manage_persons.manage_persons_login=%s" , (login,))
        data = curs.fetchone()[0]
        try:
            if ph.verify(data,password):
                return True
        except exceptions.VerifyMismatchError:
            print('wrong password in ajax\n')
            return False

    def EditRecord(self , table , index):
        conn = psql.connect(dsn_web)
        curs = conn.cursor()
        curs.execute("UPDATE ")
        conn.commit()

    def GetTeacherRateByIin(self , IIN):
        curs = self.Connect()
        curs.execute(qf.get_teacher_rate_by_iin(IIN))
        return curs.fetchall()

    def GetManagePersonsPrivileges(self , username):
        curs = self.Connect()
        curs.execute("SELECT manage_persons.manage_persons_priv_value FROM manage_persons WHERE manage_persons_login= %s" , (username,))
        return curs.fetchone()[0]

    def GetSeasonByTeacher(self):
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
    def GetTeachersByManagePerson(self , id_mp , id_season):
        curs = self.Connect()
        curs.execute(QF.get_teachers_and_rate_value_by_manager_teachers(self ,id_mp , id_season))
        return curs.fetchall()
    #dev
    def JOIN(self):
        curs = self.Connect()
        curs.execute('''
					SELECT
					  teachers.sname_t , login
					FROM
					  teachers
					INNER JOIN
					  manage_persons
					ON
					  manage_persons.id_user=1
						AND
					  teachers."Id_teacher_group" = manage_persons.id_user;
					''')
        # curs.execute("SELECT * FROM teachers")
        return curs.fetchall()

    #dev
    def GetIINs(self):
        curs = self.Connect()
        curs.execute("SELECT * From teachers")
        return curs.fetchall()
