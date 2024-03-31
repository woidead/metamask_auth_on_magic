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
wait = WebDriverWait(driver, 20)

button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/button[1]')))
button.click()

button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="08c54837-f08f-436a-9c06-336dfff54801"]/div[3]')))
button.click()
time.sleep(3)

element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]')))
driver.execute_script("arguments[0].scrollIntoView(true);", element)


link = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div[1]/a')))
link.click()

window_handles = driver.window_handles
driver.switch_to.window(window_handles[1])
try:
    first_button_xpath = '/html/body/aside/nav/div/button/span[1]'
    wait.until(EC.element_to_be_clickable((By.XPATH, first_button_xpath))).click()
except Exception as e:
    print("Error:", e)

try: 
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[12]/div/div/div/div/div[1]/button[1]"))).click()
except Exception as e:
    print("Error:", e)

time.sleep(100)

driver.quit()
