#'CLASS_NAME', 'CSS_SELECTOR', 'ID', 'LINK_TEXT', 'NAME', 'PARTIAL_LINK_TEXT', 'TAG_NAME', 'XPATH'
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as cserv
from selenium.webdriver.firefox.service import Service as fserv
from shutil import rmtree
from time import time, sleep
from os import system
import sys
import zipfile

ser = None
op = None
s = None

def startChrome(url, driverPath):
    global ser, op, s
    ser = cserv(driverPath)
    op = webdriver.ChromeOptions()
    s = webdriver.Chrome(service = ser, options = op)
    s.get(url)
    rmtree("__pycache__")

#browser controls
def loadUrl(url):
    s.get(url)

def goBack():
    s.back()

def goBackUsingCache():
    s.execute_script("history.back();")
    
def goForward():
    s.forward()

def f5():
    s.refresh()

def end():
    s.close()
    system("taskkill /im chromedriver.exe /f")

def getCurURL():
    return s.current_url

def minimize():
    s.minimize_window()

def switchTab(tabIndex):
    s.switch_to.window(s.window_handles[tabIndex])

#element interactions
def findEle(selector, description):
    return s.find_elements(selector, description)
    
def eleExists(selector, description):
    try:
        s.find_element(selector, description)
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
        f5()
