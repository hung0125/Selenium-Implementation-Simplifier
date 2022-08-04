#'CLASS_NAME', 'CSS_SELECTOR', 'ID', 'LINK_TEXT', 'NAME', 'PARTIAL_LINK_TEXT', 'TAG_NAME', 'XPATH'
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as cserv
from selenium.webdriver.firefox.service import Service as fserv
from selenium.webdriver.common.action_chains import ActionChains
from shutil import rmtree
from time import time, sleep
from os import system
import sys
import zipfile

#public fields (can directly access)
ser = None
op = None
manage = None
act = None

def startChrome(url:str, driverPath:str):
    global ser, op, manage, act
    ser = cserv(driverPath)
    op = webdriver.ChromeOptions()
    manage = webdriver.Chrome(service = ser, options = op)
    manage.get(url)
    act = ActionChains(manage)
    try:
        rmtree("__pycache__")
    except: pass

    
#browser controls
'''def loadUrl(url):
    manage.get(url)

def goBack():
    manage.back()

def goBackUsingCache():
    manage.execute_script("history.back();")
    
def goForward():
    manage.forward()
'''

def end():
    manage.close()
    system("taskkill /im chromedriver.exe /f")

def getCurURL():
    return manage.current_url

def minimize():
    manage.minimize_window()

def switchTab(tabIndex):
    manage.switch_to.window(manage.window_handles[tabIndex])

#element interactions
def findEle(selector, description):
    return manage.find_elements(selector, description)
    
def eleExists(selector, description):
    try:
        manage.find_element(selector, description)
        return True
    except:
        return False
        
def waitForEle(selector, description, timeoutSeconds):
    start = time()
    while(not eleExists(selector, description)):
        if time() - start > timeoutSeconds:
            try:
                end()
                print("Timeout! Program ended.")
                #sys.exit("Timeout! Program ended.")
            except:
                pass
        sleep(0.1)

def f5UntilEleExists(selector, description):
    while(not eleExists(selector, description)):
        manage.refresh()

def hover(selector, description):
    act.move_to_element(manage.find_element(selector, description)).perform()
