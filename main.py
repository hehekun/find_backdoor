#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import re
import sys
import filterr
import replaces
import find
def main(name):
    string = replaces.replaces(name)
    filterr.filterr(name)
    find.find(name)
if __name__ == '__main__':
    main('./../1.c') 
