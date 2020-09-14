# ------------------------------------------------------------
# --  Title: test_baidu_search.py
# --  Description: test baidu search function.
# --  Author: Dong Haxia
# --  Date: 2020-9-6
# ------------------------------------------------------------


import unittest
import time
from ddt import ddt, data
from selenium import webdriver


@ddt
class TestDemo(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")

    @data('软件测试', 'ISTQB')
    def test_search(self, text):
        self.driver.find_element_by_id("kw").send_keys(text)
        time.sleep(6)
        self.driver.find_element_by_id('su').click()

    def tearDown(self) -> None:
        self.driver.quit()
        time.sleep(6)


if __name__ == '__main__':
    unittest.main()