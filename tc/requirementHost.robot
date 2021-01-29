*** Settings ***
Library  SeleniumLibrary
Library  pylibs.RequirementHost
Suite Setup  to_requirement_page

*** Test Cases ***
需求类型
    ${rqmType}  get_requirement_type
    ${inData}  create list  最新需求  热门需求
    should be true  $rqmType==$inData