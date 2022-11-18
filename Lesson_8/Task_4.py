#!/bin/bash
# !/usr/bin/python3

import random
import json

input_string = "Tim,John,Sally,Trevor,Harry".split(",")
input_tuple = (12, 34, 24, 57, 18)

my_dict = {random.randint(100000, 999999): {"Name": input_string[i]} | {"Age": input_tuple[i]} for i in range(len(input_string))}

with open('Task_4.json', 'w') as file:
    json.dump(my_dict, file, indent=4)
