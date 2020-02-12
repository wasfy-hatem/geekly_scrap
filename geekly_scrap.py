import secrets
import jsonpickle
#import json
import simplejson as json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome import service
import time
import csv

import urllib.request
import os


# Geekly
'''
https://geekly.co.jp/search/engineer/   
会社名
(company's name)
'''

def get_login_and_hide(filtered_by_user_results_url):
   
   site_url_login = "https://mixess.jp/com/login.html"
   print("site_url_login is: ", site_url_login)
   ###filtered_by_user_results_url = "https://mixess.jp/com/?act=admin-item&mode=form&page=&order=&csv=&title=&text02=&pref=&city=&status=&tantou_id=41" # direct link to filtered by user hatem 

   print("filtered_by_user_results_url is: ", filtered_by_user_results_url)


   #########
   # selenium
   ###############################################
   driver = webdriver.Opera(executable_path='/home/wasfy/python_progs/crawl_jobs/operadriver_linux64/operadriver')
   driver.get(site_url_login)

   #login url
   driver.find_element_by_name("email").send_keys(secrets.email)
   driver.find_element_by_name("passwd").send_keys(secrets.passwd)
   driver.find_element_by_name("submit").click()

   #add_the next URL
   driver.get(filtered_by_user_results_url)


   #wasfy example

   select_all_check_box_xpath           = "//label[@id='input_check_edit_all']/input[1]"
    
   make_selected_private_button_xpath   = "//div[1]/div[@class='box_publishing_left' and 1]/p[1]/a[@class='btn btn-danger' and 2]"
   make_selected_public_button_xpath    = "//div[1]/div[@class='box_publishing_left' and 1]/p[1]/a[@class='btn btn-warning' and 1]"



  # select all
  
   driver.find_element_by_xpath(select_all_check_box_xpath).click()
  


   # press "hide selected" button
   
   #'''
   #=====pressing private  button ===================
   time.sleep(10)
   driver.find_element_by_xpath(make_selected_private_button_xpath).click()

   #-------------------------------------------------------------------
   # --- handelling popup ------------ #

   #Switch the control to the Alert window
   obj = driver.switch_to.alert

   #Retrieve the message on the Alert window
   message=obj.text
   print ("Alert shows following message: "+ message )

   time.sleep(2)

   #Section 1
   #use the accept() method to accept the alert
   obj.accept() # equas pressing "OK" :D


   time.sleep(2)

   #refresh the webpage
   ###driver.refresh()

   #-------------------------------------------------------------------

   #'''



  #===========================================
  # time before closing selinum driver  xxxxx
  #time.sleep(60)
   time.sleep(50)

   driver.close()
   driver.quit()

   return




#  ----------------------------    main  --------------------




filtered_by_user_results_url = "https://mixess.jp/com/?act=admin-item&mode=form&page=&order=&csv=&title=&text02=&pref=&city=&status=&tantou_id=41" # direct link to filtered by user hatem 

get_login_and_hide(filtered_by_user_results_url)

