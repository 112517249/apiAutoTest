# 导包
import os
import time
import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner
from script.test_login import TestLogin
# 创建测试套件
suite = unittest.TestSuite()
# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestLogin))
# 定义生成测试报告的名称
report_path = os.path.dirname(os.path.abspath(__file__))+"/report/fbc{}.html".format(time.strftime('%Y%m%d %H%M%S'))
# 打开测试报告,以写入模式打开,然后用HTMLTestRunner_PY3生成测试报告
with open(report_path,mode='wb') as f:
    # 实例化HTMLTestRunner_PY3
    runner = HTMLTestRunner(f,verbosity=2,title='fbc登录接口测试',description="HTMLTestRunner_PY3生成的测试报告")
# 运行测试套件,生成测试报告
    runner.run(suite)