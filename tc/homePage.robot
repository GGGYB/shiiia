*** Settings ***
Library  pylibs.HomePage

*** Test Cases ***
百度一下
    ${getText}  get_navigate
    ${inData}  create list  首页  需求大厅  入驻企业  产品与案例  支持与服务  登录
    should be true  $getText==$inData
