from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.headless = True
driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')


driver.get("https://www.daraz.com.bd/")
time.sleep(0.1)

search = driver.find_element_by_id("q")
search.click()



time.sleep(0.1)
search.send_keys("Walton 64GB")
time.sleep(5)


searchbuttonclick = driver.find_element_by_class_name("search-box__button--1oH7")
searchbuttonclick.click()



clicksdcard=driver.find_element_by_link_text("Walton 64GB Class 10/U3 Micro SDHC/SDXC Memory Card with Adapter")
clicksdcard.click()



price = driver.find_element_by_css_selector(".pdp-price.pdp-price_type_normal.pdp-price_color_orange.pdp-price_size_xl")

print(price.text)



