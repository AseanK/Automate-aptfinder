from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome('PATH TO YOUR DRIVER')

apt_form = "https://www.apartmentfinder.com/***YOUR PARAMENTS***"

driver.get(apt_form)

# Get address
addresses = driver.find_elements(By.TAG_NAME, "address")

list_add = []
for address in addresses:
    list_add.append(address.text)
print(list_add)

# Get price
prices = driver.find_elements(By.CLASS_NAME, "altRentDisplay.layout-hidden-xs")

list_price = []
for price in prices:
    list_price.append(price.text)
print(list_price)

# Get url
web_a = driver.find_elements(By.CSS_SELECTOR, ".flex-12.desktop-title a")

list_url = []
for i in web_a:
    if i.get_attribute("href").startswith("http"):
        list_url.append(i.get_attribute("href"))
print(list_url)



google_form = "https://docs.google.com/forms/***YOUR GOOGLE FORM LINK***"

for i in range(len(list_add)):
    driver.get(google_form)

    sleep(2)
    
    # ADJUST XPATH IF AN ERROR
    add_inp = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    pri_inp = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    web_inp = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    add_inp.send_keys(list_add[i])
    pri_inp.send_keys(list_price[i])
    web_inp.send_keys(list_url[i])
    btn.click()
