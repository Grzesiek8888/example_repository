from selenium import webdriver

def get_website_title(url):
    driver = webdriver.Chrome()
    driver.get (url)
    title = driver.title
    driver.quit()
    return title

def test_onet_title():
    title = get_website_title("https://onet.pl/")
    assert title ==  "Onet – Jesteś na bieżąco"
    

# def test_onet_title2():
# #   driver = webdriver.Chrome()
# driver.get("https://bochnia.eu/")
#   print(driver.title)
#  assert driver.title == "Bochnia Miasto Soli"
# driver.quit()
