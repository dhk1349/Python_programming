# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:58:21 2019

@author: dhk13
"""

from flask import Flask, request, render_template, g, redirect, url_for
from scheduler_module import module, InputGenerator
app=Flask(__name__)
@app.route('/')
def index_page():
	#info=request.form['data']
	return render_template("index.html")

@app.route('/chart', methods=['POST', 'GET'])
def chart():
    if request.method == 'POST':
      result = request.form
      #lst1=["DeferrableService", [[4,10],[8,20]],[[2,5],[1,12]]]
      #result1=module(lst1)
      list3=InputGenerator()
      list3.insert(0, result['Scheduler'])
      g.input=list3
      g.result, g.TotalResult = module(list3)
      return render_template("chart.html",result = result)

if __name__=="__main__":
    #lst1=["DeferrableService", [[4,10],[8,20]],[[1,5],[1,12]]]
    #result1=module(lst1)
    #print(result1)
    app.run(host="0.0.0.0", port=1080, debug=True)