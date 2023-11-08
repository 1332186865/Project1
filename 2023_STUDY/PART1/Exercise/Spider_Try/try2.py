#  Copyright (c) 2023. Generated by Gu.
#  -*- coding=utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建 WebDriver 实例对象，指明使用chrome浏览器驱动
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\Admin\AppData\Local\Google\Chrome\User Data\Default")
wd = webdriver.Chrome(options=options)

# WebDriver 实例对象的get方法 可以让浏览器打开指定网址
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

# 根据 class name 选择元素，返回的是 一个列表
# 里面 都是class 属性值为 animal的元素对应的 WebElement对象
elements1 = wd.find_elements(By.CLASS_NAME, 'plant')
# 取出列表中的每个 WebElement对象，打印出其text属性的值
# text属性就是该 WebElement对象对应的元素在网页中的文本内容
for element in elements1:
    print(element.text)
print()

elements2 = wd.find_elements(By.CSS_SELECTOR, '[class="animal"]')
# elements2 = wd.find_elements(By.CSS_SELECTOR, '.animal')
# elements2 = wd.find_elements(By.CLASS_NAME, 'animal')
for element in elements2:
    print(element.text)
print()

element3 = wd.find_element(By.CSS_SELECTOR, '#searchtext')
element3.send_keys('你好')

# elements4 = wd.find_elements(By.CSS_SELECTOR, 'div')
elements4 = wd.find_elements(By.TAG_NAME, 'div')
for element in elements4:
    print(element.text)
print()

element5 = wd.find_element(By.CSS_SELECTOR, '[href="http://www.miitbeian.gov.cn"]')
print(element5.get_attribute('outerHTML'))


