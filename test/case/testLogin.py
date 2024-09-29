# -*-coding:utf-8-*-
import unittest,sys
sys.path.append('../../../../')
from projectTest.chapter9.test.pages.loginPage import LoginPage

class TestLogin(unittest.TestCase):
    """登录测试"""
    '''
    将启动浏览器和关闭浏览器的操作分别放在测试的预置条件
    setUpClass和测试销毁tearDownClass中，进行测试登录的操作方法设置为test
    login01()
    '''
    @classmethod
    def setUpClass(cls):#第一个参数是cls,表示调用当前的类名
        cls.login = LoginPage()

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_driver()

    def test_login01(self):
        """登录成功"""
        self.login.login()


if __name__ == '__main__':
    unittest.main()
