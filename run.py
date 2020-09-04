# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:framework
# File_name:run.py.py
# Author: liyage
# Time:2020年09月02日
import unittest
import os
import time
from config.HTMLTestRunner import *
from config.ding import *
#用例路径
case_path=r'F:\bw_2004\framework\Test_Case'
#报告存储路径
repart_path=r'F:\bw_2004\framework\report'
#过滤出测试用例文件
discover=unittest.defaultTestLoader.discover(case_path,pattern="log*.py")

if __name__=="__main__":
    now = time.strftime('%Y%m%d%H%M%S')                       #时间
    report_name = os.path.join(repart_path, f'{now}.html')
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner(
            stream=f,
            title=u'测试报告',    #u 方便识别中文
            description='测试报告结果如下',
            verbosity=2,
            tester=u'李雅格'
        )
        runner.run(discover)
        message()