# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:58:21 2019

@author: dhk13
"""

from flask import Flask, request, render_template, g, redirect, url_for

app=Flask(__name__)

@app.route('/',  methods=['POST', 'GET'])
def index_page():
	info=request.form['data']
	return redirect(url_for('chart', getdata=info))

@app.route('/chart')
def chart():
	return render_template("chart.html")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
