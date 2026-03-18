import pyautogui
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from time import sleep
import random
import datetime

missclick = random.choice('abcdefghijklmnopqrstuvwxyz')

def get_first_word(filename):
    with open(filename, 'r') as file: 
        return file.readline().strip()


words = get_first_word("search.txt")

def FakeBrowse():
    pyautogui.moveTo(random.randint(x, y), random.randint(x, y))
    sleep(0.5)
    pyautogui.click()
    pyautogui.move(37)
    pyautogui.moveTo(x, y) #click random website link
    sleep(1)
    pyautogui.click()
    pyautogui.move(random.randint(x, y), random.randint(x, y))
    sleep(2)
    pyautogui.typewrite(missclick) # simulate accidental click
    sleep(3)
    pyautogui.move(43)
    sleep(2)
    pyautogui.moveTo(x, y) #navigate to the braves back arrow
    pyautogui.click()


def timer():
    current_time = datetime.datetime.now()
    return current_time.hour % 2 == 0 


def OpenBrowser():
    options = webdriver.ChromeOptions() #this shi allows me to config this mf
    options.binary_location = "/usr/bin/brave-browser"
    driver = webdriver.Chrome(service=ChromeDriverManager().install(), options=options) #lwk dont understand but launches brave
    is_browser_open = True
    return driver


is_browser_open = False


while True:
    if timer():
        if not is_browser_open:
            try:
                driver = OpenBrowser()
                is_browser_open = True
            except Exception as e:
                print("Error ur shit doesnt work:", e)
    else:
        if is_browser_open:
            driver.quit() 
            is_browser_open = False

    if is_browser_open: 
        for word in words:
            pyautogui.moveTo(random.randint(0, x), random.randint(0, y))  
            pyautogui.click()
            pyautogui.typewrite(word)
            pyautogui.press('enter')
            sleep(random.randint(6, 10))
            FakeBrowse()

    sleep(60)