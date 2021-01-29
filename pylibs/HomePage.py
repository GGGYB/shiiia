# -*- coding: utf-8 -*-
# Author： sharon
# Datetime： 2021/1/29 14:55 
# File: $ {NAME}
import yaml
from pylibs.BasePage import BasePage
from pylibs.MyDriver import Driver,open_my_browser,close_my_browser
import time
class HomePage(BasePage):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self):
        fileDir = r"webElement/homePage.yaml"
        file = open(fileDir,mode="r",encoding="utf-8")
        self.webElement = yaml.load(file,Loader=yaml.FullLoader)
        print(self.webElement)
        self.navigateListLocators = self.webElement["navigateListLocators"]
    def get_navigate(self):
        return self.get_element_text(self.navigateListLocators)



if __name__ == '__main__':
    b = HomePage()
    open_my_browser()

    close_my_browser()