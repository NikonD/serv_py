# -*- coding: utf-8 -*-

from flask import url_for
from flask import Flask, flash, redirect, render_template, json , request, session, abort , escape
from app import app
from app.forms import LoginForm , Forms
from app.smdb import DataManage
from app.view_indicators import show_indiators
from app.UsersModel import USER , s_name , manage_persons_struct
import argon2
import os

# TODO deviate by date
#usr = USER()
# usr.value =1
# print()
# s_name['u_role'] = 11
# print(s_name)
dm = DataManage()
hs = argon2.PasswordHasher()
title = ""
manage_persons_struct={}

@app.route('/login', methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['text']
        password = request.form['pas']
        print(password)
        manage_persons_struct=dm.GetManagePersonsInfo(user)
        try:
            if hs.verify(dm.GetManagePersonsInfo(user)['manage_persons_password'] , request.form['pas']):
                session['username'] = user
                return render_template('index.html')
        except argon2.exceptions.VerifyMismatchError:
            print('wrong password\n')
            flash('wrong')
    return render_template("login.html" , rform=LoginForm() , title='login')

@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        # her = dm.ShowAll()
        return render_template('index.html' , user='Logged in as %s' % escape(session['username']))
    # return render_template('index.html' , user='You are not logged in' , title='home')
    return redirect(url_for('login'))

@app.route('/signup' , methods=['GET' , 'POST'])
def reg_m_person():
    rfrm=LoginForm()
    sfrm=Forms()
    sfrm.init()
    return render_template("signup.html" , rform=rfrm  , sform=sfrm  , title='sign up')

@app.route('/logout')
def logout():
    # remove the username from the session if its the
    return redirect(url_for('index'))

@app.route('/rate' , methods=['GET' , 'POST'])
def rate():
    iin_val =''
    record = []
    info = dm.GetIINs()
    if request.method == 'POST':
        iin_val = request.form['iin_text']
        record = dm.GetTeacherRateByIin(iin_val)
    return render_template('rate.html' , rform=LoginForm() , records = record , info = info  , title='show rate')

# @app.route('/inds')
# def inds():
#     info = dm.GetIndicators()
#     return render_template("inds.html" , info = info , title='Indicators')



@app.route('/get_len' , methods=['GET' , 'POST'])
def get_len():
    if request.method == 'POST':
        name = request.form['name']
    print(name)
    return json.dumps({'len': len(name) + len(name)})

@app.route('/get_inds' , methods=['GET' , 'POST'])
def get_inds():
    return render_template("get_data.html" , var="var_in_template")

@app.route('/get_data_for_diag' , methods=['GET' , 'POST'])
def get_data_for_diag():
    return render_template("rate.html" , inds ='dsd')

@app.route('/login_ajax' , methods=['GET' , 'POST'])
def login_ajax():
    if request.method == 'POST':
        login = request.form['text']
        password = request.form['pas']
        print(login + " " + password)
        try:
            if hs.verify(dm.GetManagePersonsInfo(login)['manage_persons_password'] , password):
                session['username'] = login
                return render_template("index.html")
        except argon2.exceptions.VerifyMismatchError:
            print('wrong password in ajax\n')
            flash('wrong')
    return render_template("login.html" , rform=LoginForm() , title='login')



