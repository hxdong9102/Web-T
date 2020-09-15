#**************************************************************
# 学擎云学情大数据服务平台：教师管理模块—>新增老师功能自动化测试
# url: http://boweifeng.xueqingyun.com/schadmin/user/add-thr
# Author: Dong Haixia
# Date: 2020-9-15
#**************************************************************

# import selenium library.
from selenium import webdriver
import csv
import time
from selenium.webdriver.support.select import Select

# open the test data file.
file = open("teacherdata.csv", "r")
rows = csv.reader(file)

# open Chrome browser.
driver=webdriver.Chrome()
# open the target testing page.
url="http://boweifeng.xueqingyun.com/schadmin/user/add-thr"
driver.get(url)

# login the system.
driver.find_element_by_id('loginform-identity').send_keys('xzmadmin')
driver.find_element_by_id('loginform-password').send_keys('51testing')
driver.find_element_by_name('login-button').click()
time.sleep(2)

# read testing data.
for data in rows:

    teaID = data[0]
    teaName = data[1]
    teaPass = data[2]
    teaNo = data[3]
    startDate = data[4]
    endDate = data[5]

    driver.find_element_by_id('teacherform-username').send_keys(teaID)
    driver.find_element_by_id('teacherform-fullname').send_keys(teaName)
    # 性别-下拉框定位
    sex = driver.find_element_by_id('teacherform-gender')
    Select(sex).select_by_index(2)
    # 定位并输入密码
    driver.find_element_by_id('teacherform-password').send_keys(teaPass)
    # 群组-下拉框定位
    driver.find_element_by_id('grp_sel_cmn-tree-input').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="grp_sel_cmn-tree"]/ul/li/div/div[1]/span[1]/span[1]/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="grp_sel_cmn-tree"]/ul/li/ul/li/div/div[1]/span[1]/span[1]/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="grp_sel_cmn-tree"]/ul/li/ul/li/ul/li[3]/div/div[2]/span[3]').click()

    # 校内职工编号
    driver.find_element_by_id('teacherform-school_emp_no').send_keys(teaNo)
    # 开始日期及结束日期
    driver.find_element_by_id('teacherform-start_date').send_keys(startDate)
    driver.find_element_by_id('teacherform-end_date').send_keys(endDate)

    # 角色定位
    role = driver.find_element_by_id('sel_role_id')
    time.sleep(1)
    Select(role).select_by_value('733632240705241296')
    # 科目定位
    subject = driver.find_element_by_id('sel_subject_id')
    time.sleep(1)
    Select(subject).select_by_value('753556221700778003')
    # 点击提交
    driver.find_element_by_xpath('//*[@id="w0"]/div[7]/div/button').click()
    time.sleep(3)


# close the file.
file.close()