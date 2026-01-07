
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome() #webdriver-moddule->Chrome class, driver->object
print("this is day1 code")
#driver1=webdriver. Firefox() #it will open firefox browser

#driver2=webdriver. Edge() # #it will open edge browser

driver.get("https://icma-dev.amgen.com/ADDSafety/#/login")

driver.maximize_window()
print("This is day1 code for python selenium")
driver.find_element(By.ID, "UserName").send_keys("amathu01")

#driver2.get("https://icma-dev.amgen.com/ADDSafety/#/login")

print(driver.title)

print(driver.current_url)

time.sleep(2)