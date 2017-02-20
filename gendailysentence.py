#! /usr/bin/python

import os
import json

os.system('scrapy crawl dailysentence -o item.json --nolog')

json_file = 'item.json'
json_data = open(json_file)
data = json.load(json_data)
json_data.close()

print('\n\n\n' + data[0]['quote'].center(120) + '\n\n' + '--'.rjust(100) + data[0]['author'])

os.system("del item.json")

input()