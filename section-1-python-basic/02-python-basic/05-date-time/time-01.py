#!/user/bin/python3
# -*- coding:utf-8 -*-
from datetime import timedelta, datetime, date
import calendar
"""
    需求1：
        需要执行简单的时间转换，比如天到秒，小时到分钟等的转换
"""
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)
print(c.seconds/3600)
print(c.total_seconds()/3600)
# 如果想表示指定的时间和日期，先创建一个datetime实例然后使用标准的数学运算来操作它们
t1 = datetime(2017, 2, 27)
print(t1 + timedelta(days=10))
t2 = datetime.now()
t3 = t2 - t1
print(t3.days)
print(t2+timedelta(minutes=10))
print('*'*50)
# 在计算的时候，需要注意的是datetime会自动处理闰年
t4 = datetime(2012, 3, 1)
t5 = datetime(2012, 2, 28)
print(t4 - t5)
print((t4 - t5).days)
print('*'*50)
t6 = datetime(2013, 3, 1)
t7 = datetime(2013, 2, 28)
print(t6 - t7)
print((t6 - t7).days)
print("------------------我是分割线------------------")

"""
    需求2：
        你要查找星期中某一天最后出现的日期，比如星期五
"""
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date

print(datetime.today())
print(datetime.now().weekday())
print(datetime.now().isoweekday())

print(get_previous_byday('Monday'))
print(get_previous_byday('Wednesday'))
print(get_previous_byday('Wednesday', datetime(2012, 12, 21)))
print("------------------我是分割线------------------")

"""
    需求3：
        计算当前月份的日期范围
"""


def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return start_date, end_date

a_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day
