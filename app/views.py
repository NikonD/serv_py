from flask import url_for
from flask import Flask, flash, redirect, render_template, request, session, abort , escape
from app import app
from app.forms import LoginForm 
from app.smdb import DataManage
#from app.hasher import PasswordManager
import argon2
# from hashlib import sha256

# pas = "jojo1234"
# log = "admin"
# h_str = a.hash(pas + log)
# print('hashed')

# bool_ = a.verify(h_str , pas+log)
# print(bool_)

lst = ''

dm = DataManage()
hs = argon2.PasswordHasher()

lst = dm.GetPassword('admin')


@app.route('/')
@app.route('/index')
def index():
    #pas = dm.GetPassword('admin')
    #print(pas)
    if 'username' in session:
        return render_template('index.html' , user='Logged in as %s' % escape(session['username']))
    return render_template('index.html' , user='You are not logged in' , p=dm.GetPassword('admin'))
        #return 'Logged in as %s' % escape(session['username'])
    #return 'You are not logged in'
    

@app.route('/signup' , methods=['GET' , 'POST'])
def reg_m_person():
    rfrm=LoginForm()
    return render_template("signup.html" , rform=rfrm )


@app.route('/logout')
def logout():
    # remove the username from the session if its there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/login', methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['text']
        #if  hs.verify(dm.GetPassword(user) , request.form['pas']):
        if request.form['pas'] == 'jojo1234':
            session['username'] = user
            return redirect(url_for('index'))
        else:
            flash('wrong')
    return render_template("login.html" , rform=LoginForm())