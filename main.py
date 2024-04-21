import os
from random import uniform
import time
import shutil
import zipfile
import pyperclip
import requests
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import delay, password, ads_id
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import sys


def magic(driver, wait):
    driver.get('https://bit.ly/3OCtyTm')

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
    driver.switch_to.window(window_handles[-1])
    time.sleep(uniform(*delay))
    # driver.get("https://magic.store/?utm_source=Zealy&utm_medium=referral")

    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/aside/nav/div/button"))).click()
    time.sleep(uniform(*delay))
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[10]/div/div/div/div/div[1]/button[1]"))).click()

    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[12]/div/div/div/div/div[1]/button[1]"))).click()
        time.sleep(uniform(*delay))
    except Exception as e:
        print("Error:", e)
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[11]/div/div/div/div/div[1]/button[1]"))).click()
    time.sleep(uniform(*delay))

def auth(driver, wait):
    driver.get("https://bit.ly/3OCtyTm")
    time.sleep(uniform(*delay))
    pyautogui.click((32, 989))
    time.sleep(uniform(*delay))
    pyautogui.click((920, 424))
    time.sleep(uniform(*delay))
    pyautogui.click((920, 424))

def copy_and_write_seeds():
    seeds = pyperclip.paste()
    print(seeds)
    with open('seeds.txt', 'a') as file:
        file.write(seeds+"\n")


def create_metamask(driver):
    driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#onboarding/welcome')
    # driver.close()
    print(driver.title)
    pyautogui.click((1094, 1062)) 
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[-1])
    time.sleep(uniform(*delay))
    pyautogui.click((869, 10))  

    try:
        pyautogui.click((863, 717))  
    except Exception as e:
        print(e)
    time.sleep(uniform(*delay))
    pyautogui.click((944, 799))
    time.sleep(uniform(*delay))
    pyautogui.scroll(-1000)
    time.sleep(uniform(*delay))
    pyautogui.click((936, 921))
    time.sleep(uniform(*delay))

    # pyautogui.click((888, 692))
    time.sleep(uniform(*delay))
    pyautogui.typewrite(password, interval=0.1)
    time.sleep(uniform(*delay))
    # pyautogui.click((902, 884))
    pyautogui.press('tab')
    time.sleep(uniform(*delay))
    pyautogui.typewrite(password, interval=0.1)
    time.sleep(uniform(*delay))
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('space')
    time.sleep(uniform(*delay))


    pyautogui.click((823, 841))
    time.sleep(uniform(*delay))

    pyautogui.click((887, 571))
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('space')
    time.sleep(uniform(*delay))

    pyautogui.click((934, 807))
    time.sleep(uniform(*delay))
    pyautogui.click((963, 773))
    time.sleep(uniform(*delay))
    pyautogui.click((963, 773))


    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#seed")
    time.sleep(uniform(*delay))
    pyautogui.typewrite(password, interval=0.1)
    time.sleep(uniform(*delay))
    pyautogui.press('enter')
    time.sleep(uniform(*delay))
    pyautogui.moveTo((892, 426))
    pyautogui.mouseDown(button='left')
    time.sleep(1)
    pyautogui.mouseUp(button='left')
    time.sleep(uniform(*delay))
    pyautogui.click((954, 871))
    copy_and_write_seeds()

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
pyautogui.FAILSAFE = False
chrome_driver = resp["data"]["webdriver"]
service = Service(executable_path=chrome_driver)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 100)
create_metamask(driver) 
auth(driver, wait)
time.sleep(30)
driver.quit()
requests.get(close_url)