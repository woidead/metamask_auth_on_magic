import os
import time
import shutil
import zipfile
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import driver_path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

def userdata():
    if os.path.exists('userdata'):
        shutil.rmtree("userdata")
    with zipfile.ZipFile("userdata.zip", 'r') as zip_ref:
        zip_ref.extractall("userdata")
        print("Архив 'userdata.zip' распакован в 'userdata'")
userdata()

options = Options()
options.add_argument("start-maximized")
options.add_argument("MetaMask.crx")
options.add_argument(f"user-data-dir={os.getcwd()}/userdata")


service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 100)


# driver.get('https://zealy.io/cw/magicsquare-sqr-engage-to-earn/questboard/')

# button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/button[1]')))
# button.click()

# button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="08c54837-f08f-436a-9c06-336dfff54801"]/div[3]')))
# button.click()
# time.sleep(3)

# element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]')))
# driver.execute_script("arguments[0].scrollIntoView(true);", element)


# link = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div[1]/a')))
# link.click()

# window_handles = driver.window_handles
# driver.switch_to.window(window_handles[1])
# try:
#     first_button_xpath = '/html/body/aside/nav/div/button/span[1]'
#     wait.until(EC.element_to_be_clickable((By.XPATH, first_button_xpath))).click()
# except Exception as e:
#     print("Error:", e)

# try: 
#     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[12]/div/div/div/div/div[1]/button[1]"))).click()
# except Exception as e:
#     print("Error:", e)

def create_metamask():
    driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#onboarding/welcome')
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/ul/li[1]/div/input"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/button"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/button[1]"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input"))).send_keys("password123")
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input"))).send_keys("password123")
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/button"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button[1]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/section/div[1]/div/div/label/input'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/section/div[2]/div/button[2]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button'))).click()

    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#seed")
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div/form/div/input"))).send_keys("password123")
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/button[2]'))).click()

    actions = ActionChains(driver)
    actions.click_and_hold(wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/section/div/button")))).perform()
    time.sleep(1)
    actions.release(wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/section/div/button")))).perform()
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/button"))).click()


def copy_and_write_seeds():
    seeds = pyperclip.paste()
    print(seeds)
    with open('seeds.txt', 'a') as file:
        file.write(seeds+"\n")

time.sleep(3)

driver.quit()
