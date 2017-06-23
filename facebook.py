#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/login")
print(driver.title)
elem1 = driver.find_element_by_id("email")
elem1.send_keys("aleksandrslesar@gmail.com")
elem2 = driver.find_element_by_id("pass")
elem2.send_keys("")
elem2.send_keys(Keys.RETURN)
print('end')
#driver.close()