# -*- coding:utf-8 -*-

import json
import jslib.date_time
import jslib.math_matrix

def get_versions():
    dict_versions = {}
    dict_versions['date_time'] = jslib.date_time.get_versions()
    dict_versions['math_matrix'] = jslib.math_matrix.get_versions()
    return dict_versions
