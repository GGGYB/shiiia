# -*- coding: utf-8 -*-
# Author： sharon
# Datetime： 2021/1/29 14:32 
# File: $ {NAME}
from pylibs.MyDriver import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class BasePage():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def get_element(self,locator):
        WebDriverWait(driver=Driver.wd,timeout=10,poll_frequency=0.5).until(
            EC.visibility_of_element_located(locator)
        )
        return Driver.wd.find_element(*locator)
    def get_elements(self,locator):
        WebDriverWait(driver=Driver.wd,timeout=10,poll_frequency=0.5).until(
            EC.visibility_of_element_located(locator)
        )
        return Driver.wd.find_elements(*locator)
    def get_element_text(self,locators):
        eleText = []
        for ele in self.get_elements(locators):
            eleText.append(ele.text)
        print(eleText)
        return eleText
    def scroll_to_window(self,step,scrollSize):
        for i in range(step):
            Driver.wd.execute_script(f'window.scrollBy(0,{scrollSize})')
    def to_page(self,url):
        Driver.wd.get(url)

    # 可以修改scrollTop的值来定位右侧滚动条的位置，0是最最顶部，10000是最底部。
    def scroll_to_extreme(self,num):
        js = f"var q=document.documentElement.scrollTop={num}"
        Driver.wd.execute_script(js)