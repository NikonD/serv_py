# -*- coding: utf-8 -*-

from flask import url_for
from flask import Flask, flash, redirect, render_template, request, session, abort , escape
from app import app
from app.forms import LoginForm 
from app.smdb import DataManage
import argon2

dm = DataManage()
hs = argon2.PasswordHasher()


@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        her = dm.ShowAll()
        return render_template('index.html' , user='Logged in as %s' % escape(session['username']) , rec=her)
    return render_template('index.html' , user='You are not logged in')

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
        try:
            if hs.verify(dm.GetPassword(user) , request.form['pas']):
                session['username'] = user
                return redirect(url_for('index'))
        except argon2.exceptions.VerifyMismatchError:
            print('wrong password')
            flash('wrong')
    return render_template("login.html" , rform=LoginForm())

@app.route('/rate' , methods=['GET' , 'POST'])
def rate():
    iin_val =''
    record = []
    if request.method == 'POST':
        iin_val = request.form['iin_text']
        '''
            херь какая то
            нужно пилить нармальные структуры
        '''
        record = dm.GetTeacherRateByIin(iin_val)
    return render_template('rate.html' , rform=LoginForm() , records = record )

@app.route('/edit' , methods=['GET' , 'POST'])
def edit():
    return render_template("edit.html" , frorm=LoginForm())