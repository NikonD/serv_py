class QF():

    def get_teachers_by_manager_teachers_id(self , manager_teacgers_id):
        return '''
                SELECT
				teachers_second_name,
				manage_persons_login
			FROM
				teachers,
				manage_persons
			WHERE
				manage_persons_id='%s'
				AND
				teachers_group_id=manage_persons_id 
                ''' % manager_teachers_id

    def select_all(self):
        return '''
                
                '''

    def get_teacher_rate_by_iin(self,iin):
        return   '''SELECT 
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