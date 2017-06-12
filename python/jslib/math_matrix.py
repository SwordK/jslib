# -*- coding:utf-8 -*-
# Create On 20170606
# Auth: wang.yijian
# desc: 数学计算 - 矩阵

import pandas as pd
import json

_version_jason = '''
{
    "version": "0.0.1"
}
''' # END VERSION_JSON

def get_versions():
    return json.loads(_version_json)

# ------------------------------------------------------------------------
def sum_diagonal(input_matrix):
    '''
    @introduction: 计算对角线之和。输入必须为 N*N 的矩阵
    @param:
        input_matrix:   [pandas.DataFrame] N*N 矩阵
    @return:
        sum_value:      [float] 对角线之和
    '''
    rowcount = len(input_matrix)
    if rowcount <= 0:
        return None
    colcount = len(input_matrix.iloc[0])
    if colcount <= 0 or colcount != rowcount:
        return None

    sum_value = 0.0
    rowindex = 0
    while rowindex < rowcount:
        colindex = 0
        while colindex < colcount:
            if rowindex == colindex:
                sum_value += input_matrix.iloc[rowindex].iloc[colindex]
                break                
            colindex += 1
        rowindex += 1
    return sum_value
