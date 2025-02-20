#!/bin/python
from functions import *

feature = load_data(url)
property = find_properties(feature, city)
output(property)
