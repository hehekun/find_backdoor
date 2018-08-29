#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import re
import sys
import calls
def find(name):
    fo = open(name,'r')
    complete_file = []
    for line in fo:
            complete_file.append(line)
    content = ''.join(complete_file)
    fo.close()

    for call in calls.call_list:
        ret = content
        regex_1 = r'\W'+call+'\W'
        pattern = re.compile(regex_1,re.DOTALL)
        string=re.findall(pattern,ret)
        m = pattern.search(ret)
        if (m != None):
            print m.group()
            print m.span()     


