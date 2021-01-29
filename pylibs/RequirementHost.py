# -*- coding: utf-8 -*-
# Author： sharon
# Datetime： 2021/1/29 15:16 
# File: $ {NAME}
from pylibs.BasePage import BasePage
import yaml
from common.cfg import *

class RequirementHost(BasePage):
    def __init__(self):
        file = open("webElement/requirementHost.yaml")
        self.webElement = yaml.load(file,Loader=yaml.FullLoader)
        self.url = requirementUrl
        print(self.webElement)
        self.rqmTypeLocators = self.webElement["rqmTypeLocators"]

    def to_requirement_page(self):
        self.to_page(self.url)

    def get_requirement_type(self):
        return self.get_element_text(self.rqmTypeLocators)
