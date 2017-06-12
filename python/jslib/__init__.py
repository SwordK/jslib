# -*- coding:utf-8 -*-

import json
import jslib.dateTime

def get_versions():
    dict_versions = {}
    dict_versions['dateTime'] = jslib.dateTime.get_versions()
    return dict_versions
