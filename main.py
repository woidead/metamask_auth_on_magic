import os
from random import uniform
import time
import shutil
import zipfile
import pyperclip
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import driver_path, delay
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


import sys
ads_id = "jg96jq6"
open_url = f"http://local.adspower.net:50325/api/v1/browser/start?user_id={ads_id}"
close_url = f"http://local.adspower.net:50325/api/v1/browser/stop?user_id={ads_id}"

resp = requests.get(open_url).json()
if resp["code"] != 0:
    print(resp["msg"])
    sys.exit()

def userdata():
    if os.path.exists('userdata'):
        shutil.rmtree("userdata")
    with zipfile.ZipFile("userdata.zip", 'r') as zip_ref:
        zip_ref.extractall("userdata")
        # print("Архив 'userdata.zip' распакован в 'userdata'")


userdata()
options = Options()
options.add_argument("start-maximized")
options.add_argument("MetaMask.crx")
options.add_argument(f"user-data-dir={os.getcwd()}/userdata")
options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])



chrome_driver = resp["data"]["webdriver"]
service = Service(executable_path=chrome_driver)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 100)

def get_magic(driver, wait):
    driver.get('https://zealy.io/cw/magicsquare-sqr-engage-to-earn/questboard/')

    button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/button[1]')))
    button.click()
    time.sleep(uniform(*delay))

    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="08c54837-f08f-436a-9c06-336dfff54801"]/div[3]')))
    button.click()
    time.sleep(uniform(*delay))
    time.sleep(uniform(*delay))

    element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]')))
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[1]/div/div[4]/div[2]/div[2]/div[1]/a'))).click()
    time.sleep(uniform(*delay))

    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[1])
    # time.sleep(uniform(*delay))
    # driver.get("https://magic.store/?utm_source=Zealy&utm_medium=referral")

    # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/aside/a"))).click()
    # time.sleep(uniform(*delay))
    # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/aside/nav/div/button/span[1]"))).click()

    # # try:
    # #     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[12]/div/div/div/div/div[1]/button[1]"))).click()
    # time.sleep(uniform(*delay))
    # # except Exception as e:
    # #     print("Error:", e)
    # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[11]/div/div/div/div/div[1]/button[1]"))).click()
    time.sleep(uniform(*delay))
    

def copy_and_write_seeds():
    seeds = pyperclip.paste()
    print(seeds)
    with open('seeds.txt', 'a') as file:
        file.write(seeds+"\n")


def create_metamask(driver, wait):
    driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#onboarding/welcome')
    # driver.close()
    window_handles = driver.window_handles
    print(window_handles)
    driver.switch_to.window(window_handles[-1])
    print(driver.title )
    # time.sleep(200)
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/ul/li[1]/div/input"))).click()
    time.sleep(uniform(*delay))
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/button"))).click()
    time.sleep(uniform(*delay))
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/button[1]"))).click()
    time.sleep(uniform(*delay))
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input"))).send_keys("password123")
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input"))).send_keys("password123")
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input"))).click()
    time.sleep(uniform(*delay))
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/button"))).click()
    time.sleep(uniform(*delay))
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button[1]'))).click()
    time.sleep(uniform(*delay))
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/section/div[1]/div/div/label/input'))).click()
    time.sleep(uniform(*delay))
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/section/div[2]/div/button[2]'))).click()
    time.sleep(uniform(*delay))
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button'))).click()
    time.sleep(uniform(*delay))
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button'))).click()
    time.sleep(uniform(*delay))
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button'))).click()
    time.sleep(uniform(*delay))

    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#seed")
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div/form/div/input"))).send_keys("password123")
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/button[2]'))).click()
    time.sleep(uniform(*delay))

    actions = ActionChains(driver)
    actions.click_and_hold(wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/section/div/button")))).perform()
    time.sleep(1)
    actions.release(wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/section/div/button")))).perform()
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/button"))).click()
    time.sleep(uniform(*delay))
    copy_and_write_seeds()

create_metamask(driver,wait)
get_magic(driver, wait)
time.sleep(200)



time.sleep(30)

driver.quit()
requests.get(close_url)