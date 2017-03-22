# -*- coding:utf-8 -*-
import pygal
import os
from datetime import datetime, timedelta
from pygal.maps.world import World as wd
def draw_chart():
    line_chart = pygal.StackedLine(fill=True)
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
    return line_chart.render()

def draw_line():
    date_chart = pygal.Line(x_label_rotation=20)
    date_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), [
        datetime(2013, 1, 2),
        datetime(2013, 1, 12),
        datetime(2013, 2, 2),
        datetime(2013, 2, 22)])
    date_chart.add("Visits", [300, 412, 823, 672])
    return date_chart.render()

def draw_bar():
    line_chart = pygal.Bar()
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
    return line_chart.render()

def draw_stackedbar():
    line_chart = pygal.HorizontalStackedBar()
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
    return line_chart.render()

def draw_pie():
    pie_chart = pygal.Pie()
    pie_chart.title = 'Browser usage in February 2012 (in %)'
    pie_chart.add('IE', 19.5)
    pie_chart.add('Firefox', 36.6)
    pie_chart.add('Chrome', 36.3)
    pie_chart.add('Safari', 4.5)
    pie_chart.add('Opera', 2.3)
    return pie_chart.render()


def draw_radar():
    radar_chart = pygal.Radar(fill=True)
    radar_chart.title = 'V8 benchmark results'
    radar_chart.x_labels = ['Richards', 'DeltaBlue', 'Crypto', 'RayTrace', 'EarleyBoyer', 'RegExp', 'Splay',
                            'NavierStokes']
    radar_chart.add('Chrome', [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607])
    radar_chart.add('Firefox', [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450])
    radar_chart.add('Opera', [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669])
    radar_chart.add('IE', [43, 41, 59, 79, 144, 136, 34, 102])
    return radar_chart.render()

def draw_map():
    supra = wd()
    supra.add('Asia', [('asia', 1)])
    supra.add('Europe', [('europe', 1)])
    supra.add('Africa', [('africa', 1)])
    supra.add('North america', [('north_america', 1)])
    supra.add('South america', [('south_america', 1)])
    supra.add('Oceania', [('oceania', 1)])
    supra.add('Antartica', [('antartica', 1)])
    supra.render_to_file('map.svg')

def draw_smap():
    supra = pygal.maps.world.SupranationalWorld()
    supra.add('Asia', [('asia', 1)])
    supra.add('Europe', [('europe', 1)])
    supra.add('Africa', [('africa', 1)])
    supra.add('North america', [('north_america', 1)])
    supra.add('South america', [('south_america', 1)])
    supra.add('Oceania', [('oceania', 1)])
    supra.add('Antartica', [('antartica', 1)])
    supra.render_to_file('smap.svg')

def save_file():
    with open('test.html','w') as f:
        f.write(draw_map())

if __name__ == "__main__":
    #save_file()
    draw_smap()