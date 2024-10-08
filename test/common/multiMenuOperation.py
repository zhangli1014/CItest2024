# -*-coding:utf-8-*-
from time import sleep
from elementIsExist import ElementIsExist
from selenium import webdriver
from selenium.webdriver.common.by import By

class MultiMenuOperation(object):
    """多级菜单操作"""
    def __init__(self, driver):
        self.driver = driver

    def get_all_menu(self):
        """获取所有的菜单"""
        driver = self.driver
        sleep(1)
        # 获取所有的tab父元素
        fathers_menus = [['#nav', '#nav>ul>li>a', '#nav>ul>li ul>li>a']]

        # 获取画面显示父下的所有菜单
        menu_level = []
        for father_menu in fathers_menus:
            #  使用is_exist()方法确定一级菜单的父元素在页面中出现
            father_exist = ElementIsExist(driver).is_exist(father_menu[0])#id #nav
            if father_exist:
                # 将第一级菜单添加到list中的第一个元素
                if ElementIsExist(driver).is_exist(father_menu[1]):#nav>ul>li>a
                    menu_level_1 = driver.find_elements(By.CSS_SELECTOR,father_menu[1])
                    menu_level.append(menu_level_1)

                    # 将第二级菜单添加到list中的第二个元素
                    if ElementIsExist(driver).is_exist(father_menu[2]):#nav>ul>li ul>li>a
                        menu_level_2 = driver.find_elements(By.CSS_SELECTOR,father_menu[2])
                        menu_level.append(menu_level_2)

                        return menu_level
                return menu_level

    def select_menu(self, menu_text=[]):
        """
        选择菜单
        :param menu_text: 必须是list
        :return:
        """
        menu_levels = self.get_all_menu()
        i = 0
        print(menu_levels)
        for menus in menu_levels:
            for menu in menus:
                if menu.text == menu_text[i]:
                    sleep(3)
                    menu.click()
                    i += 1
                    break


if __name__ == '__main__':

    driver = webdriver.Chrome()
    driver.maximize_window()
    #driver.get('http://localhost:63342/projectAutoTest/projectHtml/chapter7/period4-2/index.html')
    driver.get('file:///D:/autotest/AutoTestExample-master/projectHtml/chapter9/period4-2/index.html')
    sleep(1)
    menu = MultiMenuOperation(driver)
    menu.select_menu(["链接", "百度"])
    sleep(5)
    #driver.quit()