from flask import render_template, redirect, url_for, request

# from app.auth.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm
# from app.models import User
# from app.auth.email import send_password_reset_email
from app import session
from app.auth import auth_module
from app.auth.forms import LoginForm
from app.database.smdb import DataManager
from app.roles.usermodel import manage_persons, list_user

dm = DataManager()


@auth_module.route('/get_inds', methods=['GET', 'POST'])
def get_inds():
    return render_template("get_data.html", var="var_in_template")


@auth_module.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        p = request.values
        print(p['login'] + '\n' + p['password'] + '\n' + p['ckey'])
        if dm.VerifyPassword(p['login'], p['password']):
            session['guest'] = False
            # session.pop('error_view' , None)
            manage_persons['login'] = p['login']
            manage_persons['ckey'] = p['ckey']
            manage_persons['privileges'] = dm.GetManagePersonsPrivileges(p['login'])
            session['username'] = p['login']
            print(session.values())
            list_user.append(manage_persons)
            for row in list_user:
                print(row)
            # print(manage_persons['login'])
            # TODO goto in gen_functions by privileges
            return redirect(url_for('index', user=session['username']))
        else:
            return render_template('auth/index.html', form=LoginForm(), err="wrong password")
    else:
        return render_template('auth/index.html', form=LoginForm())


@auth_module.route('/exit', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        manage_persons.clear()
        session['guest'] = True
    return render_template('auth/index.html', form=LoginForm(), warnning="not in session")

