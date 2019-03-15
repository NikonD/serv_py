#!rate_system/bin/python

import os
from bs4 import BeautifulSoup

doc = open("app/templates/inds.html").read()
soup = BeautifulSoup(doc , 'lxml')

#for city in soup:
#    print(city)