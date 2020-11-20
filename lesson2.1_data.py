import sys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import os
import selenium
from selenium import webdriver
import time
#from PIL import Image
import io
#import requests
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--profile-directory=Default')
options.add_argument("--incognito")
options.add_argument("--disable-plugins-discovery")
options.add_argument("--start-maximized")
# driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome(executable_path='/Users/aaronlee/codes/pys/selenium/chromedriver')

driver.delete_all_cookies()
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()

driver.get("https://www.etoro.com/login") #前往這個網址


username = driver.find_element_by_id("username")
#username = driver.find_element_by_class_name("input-row-ph")
#username.clear()

#print(username)
username.send_keys("goddamn90")

password = driver.find_element_by_id("password")
#password.clear()
password.send_keys("Ab159951")

driver.implicitly_wait(30) # seconds

driver.find_element_by_class_name("w-login-btn-wrapp").click()
driver.find_element_by_class_name("w-login-btn-wrapp").click()

for i in range(10):
    time.sleep(60)
    driver.find_element_by_tag_name("button").click()


#WebDriverWait wait = new WebDriverWait(driver, 20);
#wait.until(ExpectedConditions.elementToBeClickable(By.tag_name("button"))).click();


#driver.find_element_by_automatiion-id("login-sts-btn-sign-in").click()
#driver.close()