# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:58:21 2019

@author: dhk13
"""

from flask import Flask, request, render_template, g, redirect, url_for

app=Flask(__name__)

@app.route('/')
def index_page():
	#info=request.form['data']
	return render_template("index.html")

@app.route('/chart', methods=['POST', 'GET'])
def chart():
    if request.method == 'POST':
      result = request.form
      return render_template("chart.html",result = result)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=1080, debug=True)
