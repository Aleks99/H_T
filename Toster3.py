#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://toster.ru/")
#print(driver.title)
elem1 = driver.find_element_by_name("q")
elem1.send_keys("как парсить в facebook")
elem1.send_keys(Keys.RETURN)
elem2 = driver.find_elements_by_class_name("question__title-link")
elem2[0].click()
elem3 = driver.find_element_by_class_name("question__text")
print(elem3.text)
csv_file = open('1 question .csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow([elem3.text])
#driver.close()


