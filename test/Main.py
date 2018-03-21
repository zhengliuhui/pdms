#coding=utf-8
import sys
sys.path.append('F:\pdms\test\base')
sys.path.append('F:\pdms\test\page')
sys.path.append('F:\pdms\test\result')
sys.path.append('F:\pdms\test\test_case')
import unittest
import HTMLTestRunner
import os ,time,datetime

from base.Email import *

listaa='D:\\Users\\Administrator\\PycharmProjects\\pdms\\test\\test_case'
def creatsuitel():
      testunit=unittest.TestSuite()
#discover 方法定义
      discover=unittest.defaultTestLoader.discover(listaa,
            pattern ='Test_*.py',
            top_level_dir=None)
#discover 方法筛选出来的用例，循环添加到测试套件中
      for test_suite in discover:
            for test_case in test_suite:
                  testunit.addTests(test_case)
                  print testunit
      return testunit

alltestnames = creatsuitel()
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
filename='D:\\Users\\Administrator\\PycharmProjects\\pdms\\test\\result\\'+now+'result.html'
fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
      stream=fp,
      title=u'PDMS系统测试报告',
      description=u'用例执行情况：')

if __name__ == "__main__":
      #执行测试用例
      runner.run(alltestnames)
      fp.close()
      #执行发邮件
      sendreport()
#fp.close()
#放在这里会先发邮件，再生成html文件，造成邮件内容空的
