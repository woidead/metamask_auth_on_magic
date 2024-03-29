import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import driver_path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)


driver.get('https://zealy.io/cw/magicsquare-sqr-engage-to-earn/questboard/')
button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/button[1]')))
button.click()
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="08c54837-f08f-436a-9c06-336dfff54801"]/div[3]')))
button.click()
time.sleep(3)
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]')))


driver.execute_script("arguments[0].scrollIntoView(true);", element)
link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div[1]/a')))

link.click()

driver.quit()
