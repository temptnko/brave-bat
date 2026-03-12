import pyautogui
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from time import sleep
from random import randint
import datetime


def get_first_word(filename):
    with open(filename, 'r') as file: 
        return file.readline().strip()


words = get_first_word("search.txt")

def FakeBrowse():
    pyautogui.moveTo(randint(x, y), randint(x, y))
    pyautogui.click()
    pyautogui.move(37)
    #...


def timer():
    date = datetime.now()
    if int(date) % 2 == 0:
        return True
    else:
       return False


options = webdriver.ChromeOptions() #this shi allows me to config this mf
options.binary_location = "/usr/bin/brave-browser"
driver = webdriver.Chrome(service=ChromeDriverManager().install(), options=options) #lwk dont understand but launches brave

is_browser_open = True

while True:
    if timer():
        if not is_browser_open:
            options = webdriver.ChromeOptions()
            options.binary_location = "/usr/bin/brave-browser"
            driver = webdriver.Chrome(service=ChromeDriverManager().install(), options=options)
            is_browser_open = True

        for word in words:
            pyautogui.moveTo(x, y)
            pyautogui.click()
            pyautogui.typewrite(word)
            pyautogui.press('enter')
            sleep(randint(6, 10))
            FakeBrowse()

    else:
        if is_browser_open:  
            driver.quit()
            is_browser_open = False
           
        sleep(60) 