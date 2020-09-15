#*******************************************
# 自动构造测试数据试验
# 使用faker函数进行数据构造
# Author: Dong Haixia
# Date: 2020-9-15
#*******************************************

import csv
from faker import Faker
import datetime

# create a csv file.
file = open("testdata.csv", "w", newline="")
# axquire the object that to write to.
fwrite = csv.writer(file)
name = 'slt'
faker = Faker(locale='zh_CN')
start = datetime.date.today()

for i in range(1, 101):
    num = str(i).zfill(5)
    tloginname = name+num
    tname = faker.name()
    # generate password.
    passwd = faker.password()
    # generate a No with lengths=6.
    tNo = faker.random_number(digits=6)
    # generate end_date
    end = faker.date_between(start_date=start, end_date="+20d")
    # write data to a csv file.
    fwrite.writerow([tloginname, tname, passwd, tNo, start, end])
# close the file.
file.close()










#试验2：姓名：随机汉字
# faker=Faker()
# faker=Faker(locale='zh_CN')
# for i in range(1,11):
#     tname = faker.name()
#     print(tname)














#试验3：开始日期：当前系统时间
# start=datetime.date.today()
# print(start)
#
# #试验4：结束日期：开始日期之后的20天
# faker=Faker()
# end=faker.date_between(start_date=start, end_date="+20d")
# print(end)
# #试验5：保存到测试数据文件中

