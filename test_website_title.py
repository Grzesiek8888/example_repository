from selenium import webdriver

def test_onet_title():
    driver = webdriver.Chrome()
    driver.get("https://onet.pl/")
    print(driver.title)
    assert driver.title == "Onet – Jesteś na bieżąco"
    driver.quit()

def test_onet_title2():
    driver = webdriver.Chrome()
    driver.get("https://bochnia.eu/")
    print(driver.title)
    assert driver.title == 'Bochnia Miasto Soli'
    driver.quit()
