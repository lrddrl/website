from selenium import webdriver

wd = webdriver.Chrome(r'D:\selenium\chromedriver.exe')

wd.get('http://127.0.0.1:8000/')


element = wd.find_element_by_id('kw')

element.send_keys('你好\n')


element = wd.find_element_by_id('kw')

pass