#!/usr/bin/python
import json

string = 'Hydrogen'

for index, letter in enumerate(string):
    print(letter, index)


data = dict()

data["a"] = 3
data["b"] = 5

json.dumps(data)
