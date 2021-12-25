from selenium import webdriver
from selenium.webdriver.chrome.service import Service as cserv
from selenium.webdriver.firefox.service import Service as fserv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

#element interactions
def eleExists(inXPATH):
    try:
        s.find_element(By.XPATH, inXPATH)
        return True
    except:
        return False
        
def waitForEle(inXPATH, timeoutSeconds):
    start = time()
    while(not eleExists(inXPATH)):
        if time() - start > timeoutSeconds:
            end()
            #sys.exit("Timeout! Program ended.")
        sleep(0.1)

def f5UntilEleExists(inXPATH):
    while(not eleExists(inXPATH)):
        f5()

def getEleText(inXPATH):
    return s.find_element(By.XPATH, inXPATH).text

def clickEle(inXPATH):
    s.find_element(By.XPATH, inXPATH).click()

def sendTextAndEnter(inXPATH, txt):
    s.find_element(By.XPATH, inXPATH).send_keys(txt, Keys.ENTER)

def sendText(inXPATH, txt):
    s.find_element(By.XPATH, inXPATH).send_keys(txt)

def screenshot(inXPATH, outPath):
    s.find_element(By.XPATH, inXPATH).screenshot(outPath)
    

