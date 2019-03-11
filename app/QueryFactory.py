class QF():
    
    def select_all(self):
        return '''
                SELECT
                    *
                FROM
                    select_all
                '''

    def get_teacher_rate_by_iin(self,iin):
        return '''SELECT 
                        val_rate ,
                        rate.id_teacher , 
                        sname_t  ,fname_t , 
                        season.date_season , 
                        indicator.name_ind ,
                        indicator_group.name_group_ind 
                     FROM  
                        rate ,
                        teachers , 
                        season , 
                        indicator , 
                        indicator_group    
                    WHERE 
                        teachers.iin_teacher='%s'   
                    AND   
                        rate.id_teacher = teachers.id_teacher  
                    AND 
                        rate.id_indicator = indicator.id_indicator  
                    AND  
                        indicator.id_group_ind = indicator_group.id_group_ind''' % iin

    def set_password_for_man_person(self , password):
        return '''

        '''

    def add_man_person(self , group , login , password , privileges):
        print("hello\n")