# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 13:38:55 2019

@author: hp
"""
from flask import Flask,render_template


app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return "now your website is developing!!"

@app.route('/about/')
def about():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug = True)
    

