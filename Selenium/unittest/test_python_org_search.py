# ------------------------------------------------------------
# --  Title: test_python_org_search.py
# --  Description: Test an python script by unnitest.
# --  Author: Dong Haxia
# --  Date: 2020-08-19
# ------------------------------------------------------------


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # Create the istance of Chrome WebDriver
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        # Navigate to a page given by the URL
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        #elem.send_keys(Keys.RETURN)
        elem.send_keys(Keys.ENTER)
        sleep(10)
        assert "No results found." not in driver.page_source
    
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()