"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

"""
- 收集-描述性统计（统计量）-探索-估计-假设检验
- Index，Series对象 numnpy

- 特征挑选，变量
-- finalwgt，调查参与者统计权重，该参与者所属分类在全美人口中的代表人数

- 数据变换
-- np.nan 空值处理

- 数据验证
-- 使用统计量检验

- 解释数据
-- defaultdict(list) 创建字典对象
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ex():
    df = nsfg.ReadFemPreg()
    print(df.pregnum.value_counts(sort=True))
    preg_map = nsfg.MakePregMap(df)
    indices = preg_map[10229]
    print(df.pregnum[indices].values)
def main(script):
    """Tests the functions in this module.
    
    script: string script name
    """    
    print('%s: All tests passed.' % script)
    

if __name__ == '__main__':
    main(*sys.argv)
    ex()