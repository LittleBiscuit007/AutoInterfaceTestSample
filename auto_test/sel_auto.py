import time

from selenium import webdriver


driver = webdriver.Firefox()

driver.get('http://www.baidu.com/')

time.sleep(3)

driver.close()

print(1111)


