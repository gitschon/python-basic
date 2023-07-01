from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

drv = webdriver.Chrome()
drv.get('http://www.google.com/ncr')
assert 'Google' in drv.title

elm = drv.find_element("name", "q")
elm.send_keys("selenide")
elm.send_keys(Keys.RETURN)
time.sleep(2)
search_results = drv.find_elements(By.XPATH, "//*[@id='rso']//h3/a")
print(search_results[0].get_attribute('href'))
rfa1 = str(search_results[0].get_attribute('href'))
assert 'selenide.org' in search_results[0].get_attribute('href')

pic = drv.find_element(By.XPATH, '//*[@id="cnt"]/div[5]/div/div/div/div[1]/div/a[1]')
pic.click()
search_pic = drv.find_elements(By.XPATH, '//div[@class="dmeZbb"]')
time.sleep(2)
print(search_pic[0].text)
assert 'selenide.org' in search_pic[0].text
all_button = drv.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]')
all_button.click()
search_results2 = drv.find_elements(By.XPATH, "//*[@id='rso']//h3/a")
rfa2 = search_results2[0].get_attribute('href')
print(f"asserting {rfa1} and {rfa2}")
assert rfa1 == rfa2, 'Адреса не совпадают'

drv.close()
