from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
sleep(3)
# print(driver)
driver.get("https://onet.pl/")
site_title = driver.title
sleep(3)
driver.quit()
expected_title = "Onet – Jesteś na bieżąco"
assert expected_title == site_title 

# print(driver)
# driver.get("https://onet.pl/")
# sleep(5)
# site_title = driver.title
# print(site_title)
# assert site_title == "Onet – Jesteś na bieżąco"
# sleep(5) # Czekaj 5 sekund