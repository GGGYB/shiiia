# -*- coding: utf-8 -*-
# Author： sharon
# Datetime： 2021/1/29 14:25 
# File: $ {NAME}
from selenium import webdriver
import time
from common.cfg import *

class Driver(object):
    wd = None
def open_my_browser():
    Driver.wd = webdriver.Chrome(r"D:\software\chromedriver.exe")
    Driver.wd.implicitly_wait(10)
    Driver.wd.maximize_window()
    Driver.wd.get(URL)
    time.sleep(3)

def close_my_browser():
    Driver.wd.quit()