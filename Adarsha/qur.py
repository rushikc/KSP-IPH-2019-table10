from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome('/home/adarsha/Projects/hackathon-IPH-master/Adarsha/chromedriver')
driver.get('https://www.quora.com/')
print("Opened facebook...")
email = driver.find_element_by_xpath("//input[@id='__w2_wqwg1o0y21_email' or @name='email']")
email.send_keys('9148960876')
print("email entered...")
password = driver.find_element_by_xpath("//input[@id='__w2_wqwg1o0y21_password']")
password.send_keys('1998stayhard')
print("Password entered...")
button = driver.find_element_by_xpath("//input[@id='__w2_wqwg1o0y21_submit_button']")
button.click()
print("facebook opened")
status = driver.find_element_by_xpath("//textarea[@name='xhpc_message']")
status.send_keys("Bot is typing here");
print("Status trying")
postbutton = driver.find_element_by_xpath("//button[contains(.,'Post')]")
postbutton.click()
print("post done")