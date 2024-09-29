# -*-coding:utf-8-*-
from time import sleep
from elementIsExist import ElementIsExist
from selenium import webdriver
from selenium.webdriver.common.by import By

class TabOperation(object):
    '''Tab操作'''
    def __init__(self, driver):
        self.driver = driver

    def get_all_tab(self):
        '''获取所有的tab'''
        sleep(1)
        # 获取所有的tab父元素
        # 元素定位，我们默认取css定位
        fathers_tabs = [['.tabs1', 'a2'],
                       ['.tabs', 'a'],]#使用.tabs定位,class
        # 获取画面显示父节点下所有tab
        for father_tab in fathers_tabs:
            # 使用is_exist()方法判断父节点是否存在，如果父节点不存在，则查找的tab不匹配
            father_exist = ElementIsExist(self.driver).is_exist(father_tab[0]) # class选择
            # 父节点存在，则进行操作
            if father_exist:
                father = self.driver.find_element(By.CSS_SELECTOR,father_tab[0])
                tabs = father.find_elements(By.CSS_SELECTOR,father_tab[1])#标签选择
                return tabs

    def switch_tab(self, tab_text):
        '''
        切换tab
        :param tab_text: 需要切换到的tab内容
        :return:
        '''
        tabs = self.get_all_tab()
        for tab in tabs:
            if tab.text == tab_text:
                tab.click()
                sleep(3)
                return


if __name__ == '__main__':

    driver = webdriver.Chrome()
    driver.maximize_window()
    #driver.get('http://localhost:63342/projectAutoTest/projectHtml/chapter7/period4-1/index.html')
    driver.get('file:///d:/autotest/AutoTestExample-master/projectHtml/chapter9/period4-1/index.html')
    sleep(3)
    tab = TabOperation(driver)
    tab.switch_tab('Tab2')
    #driver.quit()
