# -*- coding:utf-8 -*-
import json
from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

filename = 'population_data.json'
with open(filename, 'r') as f:
    pop_data = json.load(f)

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = pop_dict['Value']
        if get_country_code(country_name):
            print get_country_code(country_name), ':',population


