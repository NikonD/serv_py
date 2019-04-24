from flask import url_for
from flask import Flask, flash, redirect, render_template, json , request, session, abort , escape
from app import app
from app.database.smdb import DataManager

dm = DataManager()

@app.route('/inds')
def show_indiators():
    info = dm.GetIndicators()
    return render_template("inds.html" , info = info , title='Indicators')

