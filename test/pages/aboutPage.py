# -*-coding:utf-8-*-
from selenium.webdriver.common.by import By
import sys
sys.path.append('../../../../')
from projectTest.chapter9.test.pages.loginPage import LoginPage

class AboutPage(LoginPage):
    """关于我们页面"""

    def about_element(self):
        """关于我们页面判断元素"""
        return self.find_element(By.CSS_SELECTOR, "#about h1")#id选择

