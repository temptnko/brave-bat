#unusable yet: timer variable not defined, fake browsing function not done, scheduled breaks arent done, searching words function isnt done


from humancursor import WebCursor
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from radnom import randint
from time import sleep
import datetime

#NOT DONE!!
#simulating browsing and looking around
def fake_browsing(cursor):
    cursor.move(randint(20-300), randint(50-200))
    sleep 2
    cursor.move(randint(20-300), randint(50-200))
    sleep 1
    cursor.move(randint(20-300), randint(50-200))
    sleep 10
    cursor.move(randint(20-300), randint(50-200))
    
def get_words(filename):
    with open(filename, 'r') as file:  #ts should read a search.txt file and write it in a list tht ill specify later
        return file.readline().strip()

words = get_words(search.txt)

options = webdriver.ChromeOptions() #this shi allows me to config this mf
options.binary_location = "/usr/bin/brave-browser"
driver = webdriver.Chrome(service=ChromeDriverManager().install(), options=options) #lwk dont understand but launches brave

cursor = WebCursor(driver)

#NOT DONE!!!  
def search_words(cursor, words):
    for word in words:
        search_bar_position = (100, 50)  # not done but coordinates of the search bar
        cursor.move(*search_bar_position)  #move to the search bar
        cursor.click()
        time.sleep(0.5) 
        cursor.type(word)  # Typing the word in the search bar (idk if it looks human)
        cursor.type('\n')
        sleep 5
        fake_browsing(cursor) 
        
session = 0

while timer == True:
    session += 1
    search_words(cursor, words)
    print(f"session {session} completed")