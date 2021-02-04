#*******************************************
# 自动化测试平台-自动化测试
# 窗体转换技术实验
# Author: Dong Haixia
# Date: 2021-2-4
#*******************************************

#导入selenium类库
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

#S1:初始化浏览器
driver = webdriver.Chrome()
#S2:直接打开新增部署测试环境页面：http://172.31.15.79:9010/admin/test_plt/deployenv/add/
driver.get("http://172.31.15.79:9010/admin/test_plt/deployenv/add/")
#登录
driver.find_element_by_name('username').send_keys('admin')
driver.find_element_by_name('password').send_keys('woaizhongguo')
driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
print("登录后", driver.current_window_handle)

# S3：添加项目
time.sleep(2)
driver.find_element_by_xpath('//*[@id="add_id_project"]/img').click()
print("添加项目后", driver.current_window_handle)
print("共有多少窗口", driver.window_handles)
print("第二个窗口句柄", driver.window_handles[1])

# 进行窗口句柄的查找
for w in driver.window_handles:
    if w==driver.current_window_handle:
        pass
    else:
        #转入新窗口
        driver.switch_to.window(w)
        print("switch之后", driver.current_window_handle)
