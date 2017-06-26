#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def find_friends(person_url):
	driver.get(person_url + "/friends")
	elem4 = driver.find_elements_by_xpath('//div')
	my_friends_list = []
	my_friends_list_clear = []
	for d in elem4:		
		try:
			if d.get_attribute('data-testid') != None:
				#print("attribute['data-testid'] = ", d.get_attribute('data-testid'))   # =="friend_list_item"  
				# //div[@data-testid="friend_list_item"]				
				a = d.find_element_by_xpath('.//a')
				my_friends_list.append(a.get_attribute('href'))
				#print (my_friends_list)	
		except Exception as e:		
			print('--->', e)			
	for f in my_friends_list:
		if 'profile.php?id' in f:
			my_friends_list_clear.append(f[:f.find('&')])
		else:
			my_friends_list_clear.append(f[:f.find('?')])
	return my_friends_list_clear

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/login")
print(driver.title)
elem1 = driver.find_element_by_id("email")
elem1.send_keys("aleksandrslesar@gmail.com")
elem2 = driver.find_element_by_id("pass")
elem2.send_keys("aleks77vika89")
elem2.send_keys(Keys.RETURN)
print('end')
##print (list1)
#driver.close()
time.sleep(5)

try:
  elem3 = driver.find_element_by_xpath("//a[@class='_2s25']")
  elem3.click()
  #elem4 = driver.find_element_by_xpath("//a[@class='_6-6']")
  elem4 = driver.find_element_by_xpath("//a[@data-tab-key='friends']")
  elem4.click()
  elem5 = driver.find_element_by_xpath("//input[@class='inputtext']")
  
  for i in range(30):
    elem5.send_keys(Keys.PAGE_DOWN)
  
  
  elem6 = driver.find_elements_by_xpath("//div[@class='fsl fwb fcb']")
  print(len(elem6))
  for f in elem6:
    url_object = f.find_element_by_xpath('.//a')
    print(url_object.get_attribute('href'))

except Exception as e:		
			print('--->', e)	

  