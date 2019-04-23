from  flask import render_template , request, redirect ,url_for
from app.signup import sigup_module
from app.signup.signupForm import SignupForm
from app.database.smdb import DataManager

dm = DataManager()

@sigup_module.route('/signup' , methods=['GET' , 'POST'])
def signup():
    if request.method == 'POST':
        param = request.values
        print(param)
        if dm.AddUser(param['login'] , param['password'] , param['privileges']) == False:
            return render_template('auth/errsignup.html')
    return render_template('auth/signup.html' , form=SignupForm())

