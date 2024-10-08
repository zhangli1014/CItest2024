# -*-coding:utf-8-*-
from time import sleep
import sys
sys.path.append('..')
from test.common.elementIsExist import ElementIsExist
from selenium import webdriver
from selenium.webdriver.common.by import By
'''
通过header行中的姓名查找姓名列中的【严寒】，然后单击【严寒】元素选中【严寒】所在的行。
(1）获取姓名在header 中的index。
(2）然后遍历数据中每一行，通过姓名的index 获取每一行中姓名列的内容，如果获取的的内容值是【严寒】则返回该行，达到对【严寒】所在的行进行操作的目的。
'''
class TableOperation(object):
    """表格操作"""
    def __init__(self, driver):
        self.driver = driver

    def get_table(self):
        """获取table
            返回table的headers、body_rows和body_rows_column
        """
        sleep(1)
        # 列表顺序：table、header、body_rows、body_rows_columns
        tables_header_body = [['#dataArea>table',
                              '#dataArea>table>.header>td',
                              "#dataArea>table>tr:not(.header)",
                              "#dataArea>table>tr:not(.header)>td"], ]
        # 获取画面显示的table
        for table_header_body in tables_header_body:
            # 如果找到的父节点为空，则父节点不存在，则查找的table不匹配,在页面中不存在
            if ElementIsExist(self.driver).is_exist(table_header_body[0]):#dataArea>table
                    table = self.driver.find_element(By.CSS_SELECTOR,table_header_body[0])
                    headers = table.find_elements(By.CSS_SELECTOR,table_header_body[1])#dataArea>table>.header>td
                    body_rows = table.find_elements(By.CSS_SELECTOR,table_header_body[2])#dataArea>table>tr:not(.header)
                    rows = []
                    for body_row in body_rows:
                        body_row_column = body_row.find_elements(By.CSS_SELECTOR,table_header_body[3])#dataArea>table>tr:not(.header)>td
                        rows.append(body_row_column)
                    return headers, rows
            else:
                print("table定位失败")
                return

    def select_row(self, header_text, row_text):
        """
        根据header中的列获取对应的body中的行
        :param header_text: header 中列内容
        :param body_text: leader列对应的body列内容
        :return: 返回body中的行
        """
        headers, rows = self.get_table()
        #print(headers)
        #print(rows)

        # 获取传入的header的index
        idx = int()
        for header in headers:
            if header.text == header_text:
                idx = headers.index(header)

        # 通过index在body中寻找相应index的内容
        for row in rows:
            if row[idx].text == row_text:
                return row #返回了一行内容

    def row_click(self, header_text, row_text):
        """选择表格中行并且点击"""
        row = self.select_row(header_text, row_text)
        # 返回的row是一个list，driver不能进行点击操作，所有需要给具体的值
        # 如果返回的row中有button，可以给出button的index实现row中button点击
        print(row)
        print(type(row))
        return row[0].click()
        sleep(3)


if __name__ == '__main__':

    #driver = webdriver.Chrome('/Users/ydj/Desktop/ydj/projectAutoTest/chromedriver')
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8081/#/')
    sleep(1)
    driver.find_element(By.CLASS_NAME, "email").send_keys('admin@tynam.com')
    driver.find_element(By.CLASS_NAME, "password").send_keys('tynam123')
    driver.find_element(By.CSS_SELECTOR, ".login-btn>input[value='登  录']").click()
    sleep(1)
    table = TableOperation(driver)
    table.row_click("姓 名", "严寒")
    sleep(4)
