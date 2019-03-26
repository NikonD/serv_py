# -*- coding: utf-8 -*-

from flask import url_for
from flask import Flask, flash, redirect, render_template, json , request, session, abort , escape
from app import app
from app.forms import LoginForm , Forms
from app.smdb import DataManage
import argon2
import os
import bs4

dm = DataManage()
hs = argon2.PasswordHasher()
title = ""

@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        her = dm.ShowAll()
        return render_template('index.html' , user='Logged in as %s' % escape(session['username']) , rec=her)
    return render_template('index.html' , user='You are not logged in' , title='home')

@app.route('/signup' , methods=['GET' , 'POST'])
def reg_m_person():
    rfrm=LoginForm()
    sfrm=Forms()
    sfrm.init()
    return render_template("signup.html" , rform=rfrm  , sform=sfrm  , title='sign up')

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
            print('wrong password\n')
            flash('wrong')
    return render_template("login.html" , rform=LoginForm() , title='login')

@app.route('/rate' , methods=['GET' , 'POST'])
def rate():
    iin_val =''
    record = []
    info = dm.GetIINs()
    if request.method == 'POST':
        iin_val = request.form['iin_text']
        '''
            херь какая то
            нужно пилить нармальные структуры
        '''
        record = dm.GetTeacherRateByIin(iin_val)
    return render_template('rate.html' , rform=LoginForm() , records = record , info = info , title='show rate')

@app.route('/inds')
def inds():
    info = dm.GetIndicators()
    return render_template("inds.html" , info = info , title='Indicators')

@app.route('/get_len' , methods=['GET' , 'POST'])
def get_len():
    if request.method == 'POST':
        name = request.form['name']
    print(name)
    return json.dumps({'len': len(name) + len(name)})

@app.route('/get_inds' , methods=['GET' , 'POST'])
def get_inds():
    #f = os.open('templates/edit.html' , 'r')
    #html_text = f.read()
    #print(html_text)
    # soup = BeautifulSoup(open("app/templates/get_data.html"), "html.parser")

    #soup = BeautifulSoup(open("app/templates/get_data.html"), "html.parser")
    return render_template("get_data.html" , var="var_in_template")
    #return json.dumps({'content': html_text})

@app.route('/get_data_for_diag' , methods=['GET' , 'POST'])
def get_data_for_diag():
    #запилть отправку данных по преподавателю - группа индикаторов и рейтинг
    return render_template("rate.html" , inds ='dsd')