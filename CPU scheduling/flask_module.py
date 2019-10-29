# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:58:21 2019

@author: dhk13
"""

from flask import Flask, request, render_template

app=Flask(__name__)

@app.route('/')
def index_page():
	return render_template("chart.html")

@app.route('/chart')
def chart():
	return "temp page"
	
if __name__=="__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
