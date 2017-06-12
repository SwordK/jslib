# -*- coding:utf-8 -*-
# Create On 20161221
# Auth: wang.yijian
# desc: 日期时间相关

'''
date 支持三种类型
     1) datetime.date 类型
     2) Iso 类型 (YYYYMMDD)
     3) IsoExt 类型 (YYYY-MM-DD)
time 支持两种类型
     1) datetime.time 类型
     2) str 类型 (hh:mm:ss)
'''

import datetime
import json

_version_json = '''
{
    "version": "0.0.1"
}
''' # END VERSION_JSON

def get_versions():
    return json.loads(_version_json)

# ------------------------------------------------------------------------
def is_valid_date_isoext(input_date):
    '''
    @param:  input_date: [isoext] YYYY-MM-DD
    @return: BOOL, date
    '''
    if isinstance(input_date, str) == False:
        return False, input_date

    if (len(input_date) != 10):
        return False, input_date
    try:
        rtn_datetime = datetime.datetime.strptime(input_date, "%Y-%m-%d")
        return True, rtn_datetime.date()
    except:
        return False, input_date

def is_valid_date_iso(input_date):
    '''
    @param: input_date: [iso] YYYYMMDD
    @return: BOOL, datetime
    '''
    if isinstance(input_date, str) == False:
        return False, input_date
        
    if len(input_date) != 8:
        return False, input_date
    try:
        rtn_datetime = datetime.datetime.strptime(input_date, "%Y%m%d")
        return True, rtn_datetime.date()
    except:
        return False, input_date

def is_valid_time_str(input_time):
    '''
    @param: input_time: hh:mm:ss
    @return: BOOL, datetime.time
    '''
    if isinstance(input_time, str) == False:
        return False, input_time
    if len(input_time) != 8:
        return False, input_time
    try:
        rtn_datetime = datetime.datetime.strptime(input_time, "%H:%M:%S")
        return True, rtn_datetime.time()
    except:
        return False, input_time

def is_valid_date(input_date):
    if isinstance(input_date, datetime.datetime) == True:
        return True, input_date.date()
    if isinstance(input_date, datetime.date) == True:
        return True, input_date
    if isinstance(input_date, str) == False:
        return False, input_date
    
    input_date_fix = input_date.split(' ')[0]
    bCheck, rtn_date = is_valid_date_iso(input_date_fix)
    if bCheck == False or rtn_date == None:
        bCheck, rtn_date = is_valid_date_isoext(input_date_fix)
        if bCheck == False or rtn_date == None:
            return False, None
    return True, rtn_date

def is_valid_datetime(input_datetime):
    if isinstance(input_datetime, datetime.datetime) == True:
        return True, input_datetime
    if isinstance(input_datetime, str) == False:
        return False, input_datetime
    
    list_split = input_datetime.split(' ')
    if len(list_split) > 2:
        return False, input_datetime
    bCheck, rtn_date = is_valid_date(list_split[0])
    if bCheck == True:
        if len(list_split) == 1:
            return True, datetime.datetime.combine(rtn_date, datetime.time())
        bCheck, rtn_time = is_valid_time_str(list_split[1])
        if bCheck == True:
            return True, datetime.datetime.combine(rtn_date, rtn_time)
    return False, input_datetime

# ------------------------------------------------------------------------
# def dateformat_iso2isoext(strIso):
#     '''
#     @param: strIso: [iso]
#     '''
#     bCheck, rtn_date = is_valid_date_iso(strIso)
#     if (bCheck == False or rtn_date == None):
#         return False, None
#     rtn_str = "%04d-%02d-%02d" % (rtn_date.date().year, rtn_date.date().month, rtn_date.date().day)
#     return True, rtn_str
# 
# def dateformat_isoext2iso(strIsoExt):
#     '''
#     @param: strIsoExt: [isoext]
#     '''
#     bCheck, rtn_date = is_valid_date_isoext(strIsoExt)
#     if (bCheck == False or rtn_date == None):
#         return False, None
#     rtn_str = "%04d-%02d-%02d" % (rtn_date.date().year, rtn_date.date().month, rtn_date.date().day)
#     return True, rtn_str

# ------------------------------------------------------------------------
def to_datetime(input_date):
    '''
    @param: input_date: [datetime.date/iso/isoext]
    '''
    if isinstance(input_date, datetime.datetime) == True:
        return True, input_date
    elif isinstance(input_date, datetime.date) == True:
        return True, datetime.datetime.combine(input_date, datetime.time())
    elif isinstance(input_date, str) == True:
        bCheck, rtn_date = is_valid_datetime(input_date)
        if (bCheck == False or rtn_date == None):
            return False, input_date
        else:
            return True, rtn_date
    else:
        return False, input_date

def to_date(input_date):
    '''
    @param: input_date: [datetime.date/iso/isoext]
    '''
    b_Check, rtn_datetime = to_datetime(input_date)
    if (b_Check == False):
        return False, input_date
    return True, rtn_datetime.date()

def to_iso(input_date):
    '''
    @param: input_date: [datetime.date/iso/isoext]
    '''
    b_Check, rtn_date = to_date(input_date)
    if (b_Check == False):
        return False, input_date
    rtn_str = "%04d%02d%02d" % (rtn_date.year, rtn_date.month, rtn_date.day)
    return rtn_str

def to_isoext(input_date):
    '''
    @param: input_date: [datetime.date/iso/isoext]
    '''
    b_Check, rtn_date = to_date(input_date)
    if (b_Check == False):
        return False, input_date
    rtn_str = "%04d-%02d-%02d" % (rtn_date.year, rtn_date.month, rtn_date.day)
    return rtn_str

# ------------------------------------------------------------------------
def day_delta_by_days(input_date, nDeltaDays):
    '''
    @param:  input_date: [iso/isoext]
             nDeltaDays: 
    @return: Bool, delta_date[datetime.date]
    '''
    b_Check, input_date_fix = to_date(input_date)
    if (b_Check == False):
        return False, input_date
    delta_date = input_date_fix + datetime.timedelta(days=nDeltaDays)
    return True, delta_date

def tomorrow(input_date):
    return day_delta_by_days(input_date, 1)

def yestoday(input_date):
    return day_delta_by_days(input_date, -1)

def today_in_next_year(input_date):
    '''
    # 明年的今天
    '''
    b_Check, input_date_fix = to_date(input_date)
    if (b_Check == False):
        return False, input_date
    if (input_date_fix.month == 2 and input_date_fix.day == 29):
        return True, datetime.datetime(input_date_fix.year+1, 3, 1)
    else:
        return True, datetime.datetime(input_date_fix.year+1, input_date_fix.month, input_date_fix.day)

def date_delta(input_date1, input_date2):
    b_Check1, dtDate1 = to_datetime(input_date1)
    b_Check2, dtDate2 = to_datetime(input_date2)
    if (b_Check1 == False or b_Check2 == False):
        return False, 0
    return True, (dtDate2 - dtDate1).days
