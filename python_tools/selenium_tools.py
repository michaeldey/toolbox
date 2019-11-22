from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def login():
	''' this function logs into staging and goes to account dashboard '''
	driver.get('https://staging.zagg.com/en_us/customer/account/login/')

	driver.find_element_by_xpath("/html//input[@id='email']").send_keys('mdey@zagg.com')
	driver.find_element_by_xpath("/html//input[@id='password']").send_keys('Password1978!')
	driver.find_element_by_xpath("/html//button[@id='login-send']").click()
	logged_in = True

def go_to_account_dashboard():
	if logged_in:
		driver.get('https://staging.zagg.com/en_us/customer/account/')
	else:
		login()

driver = webdriver.Firefox()
logged_in = False

go_to_account_dashboard()