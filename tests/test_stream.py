#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright 2011 timger
#    +Author timger
#    +Gtalk&Email yishenggudou@gmail.com
#    +Msn yishenggudou@msn.cn
#    +Weibo @timger http://t.sina.com/zhanghaibo
#    +twitter @yishenggudou http://twitter.com/yishenggudou
#    Licensed under the MIT License, Version 2.0 (the "License");

import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.getcwd()))
import bearcart

html_path = r'index.html'
data_path = r'data.json'
js_path = r'rickshaw.min.js'
css_path = r'rickshaw.min.css'


#All of the following import code comes from Wes McKinney's book, Python
#for Data Analysis

import pandas.io.data as web

all_data = {}

for ticker in ['AAPL', 'GOOG']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2010', '1/1/2013')

price = pd.DataFrame({tic: data['Adj Close']
                      for tic, data in all_data.iteritems()})

vis = bearcart.Chart(price)
print vis.create_chart(html_path=html_path, data_path=data_path,
                       js_path=js_path, css_path=css_path, use_stream=True)
