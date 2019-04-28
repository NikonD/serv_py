from flask import render_template, redirect
from flask import url_for, request
from app import app, session
from app.auth.forms import LoginForm
from app.database.smdb import DataManager
from app.roles.getpage import manage_persons_page
from app.roles.usermodel import manage_persons

dm = DataManager()

@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        print(session['username'])
        return redirect(url_for('roles' , user=session['username']))
    else:
        session['guest'] = True
    if request.method == 'POST':
        manage_persons.clear()
        p = request.values
        print(p['login']+'\n'+p['password']+'\n'+p['ckey'])
        if dm.VerifyPassword(p['login'] , p['password']):
            session['username'] = p['login']
            session['guest'] = False
            # print(session.values())
            # TODO goto in gen_functions by privileges
            return redirect(url_for('roles' , user=session['username']))
        else:
            print('wrong')
            return render_template('auth/index.html' , form=LoginForm() , err="wrong password")
    return render_template('auth/index.html' , form=LoginForm() , warnning="not in session")

@app.route('/roles/<user>')
def roles(user):
    session.pop('error_view' , None)
    print(session)
    if session['guest']:
        session['error_view']= 'Вы не авторизованы'
        return redirect(url_for('errors.error'))
    else:
        if user != session['username']:
            session['error_view']= 'переход по урлу'
            return redirect(url_for('errors.error'))
    return render_template(manage_persons_page(manage_persons['privileges']) , user=user)
