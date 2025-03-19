from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
button_login = driver.find_element(By.ID, "login-button")

def detected(element = None):
    if element == None:
        print(f"Элемент не найден")
    else:
        print(f"Элемент найден")

detected(username)
detected(password)
detected(button_login)