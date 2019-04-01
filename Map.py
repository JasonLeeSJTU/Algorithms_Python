#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: Map.py

@time: 2019/4/1 20:00

@desc:

'''

from pyecharts import Map, GeoLines, Style
import pandas as pd
value = [95.1, 23.2]
attr= ["China", "France"]
map = Map("世界地图示例", width=1200, height=600)
map.add("", attr, value, maptype="world", is_visualmap=True, visual_text_color='#000')
style = Style(title_top="#fff",title_pos = "center",width=1200,height=600,background_color="#404a59")

data_Lyon = [
    ["Lyon", "上海"],
]
geolines = GeoLines("", **style.init_style)
geolines.add("", data_Lyon, maptype='world', geo_cities_coords={'Lyon': [4.8357, 45.764]}, is_legend_show=False)

geolines.render(path=r'C:\Users\JasonLee\Desktop\map.png')