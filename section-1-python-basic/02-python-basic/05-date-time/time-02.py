#!/user/bin/python3
# -*- coding:utf-8 -*-
from datetime import timedelta, datetime, date
import calendar
"""
    需求1：
        将字符串转换为日期
"""
text = '2017-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)

