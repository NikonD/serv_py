class QF():
    def select_all(self):
        return '''
                SELECT
                    *
                FROM
                    select_all
                '''

    # TODO fix query get_teacher_rate_by_iin() add condition for date
    def get_teacher_rate_by_iin(self,iin):
        return '''SELECT
                        rate.rate_value ,
                        rate.rate_teacher_id ,
                        teachers.teachers_second_name  ,teachers.teachers_first_name ,
                        season.season_date ,
                        indicator.indicator_name ,
                        indicator_group.indicator_group_name
                     FROM  
                        rate ,
                        teachers , 
                        season , 
                        indicator , 
                        indicator_group    
                    WHERE 
                        teachers.teachers_iin='{0:s}'
                    AND
                        rate.rate_season_id=season.season_id
                    AND
                        rate.rate_teacher_id = teachers.teachers_id
                    AND
                        rate.rate_indicator_id = indicator.indicator_id
                    AND
                        indicator.indicator_group_id = indicator_group.indicator_group_id'''.format(iin)

    def get_teachers_and_rate_value_by_manager_teachers(self , id_mp  ,id_season):
    	return '''
    			SELECT
				  teachers.teachers_second_name , teachers.teachers_id , rate.rate_value , rate.rate_indicator_id , indicator.indicator_name
				FROM
				  teachers
				INNER JOIN
				  manage_persons
				ON
				  manage_persons.manage_persons_id='%s'
				  AND
				  teachers.teachers_group_id = manage_persons.manage_persons_id
				INNER JOIN
				  rate
				ON
				  rate.rate_season_id='%s'
				  AND
				  rate.rate_teacher_id=teachers.teachers_id
				INNER JOIN
				  indicator
				ON
				  indicator.indicator_id = rate.rate_indicator_id
    			''' % (id_mp , id_season)