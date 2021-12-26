import seleniumMain as sm
from selenium.webdriver.common.keys import Keys

def login(userXPATH, pwdXPATH, loginBtnXPATH, user, pwd):
    sm.findEle('xpath', userXPATH)[0].send_keys(user)
    sm.findEle('xpath', pwdXPATH)[0].send_keys(pwd)
    sm.findEle('xpath', loginBtnXPATH)[0].click()
    
def loginNoBtn(userXPATH, pwdXPATH, user, pwd):
    sm.findEle('xpath', userXPATH)[0].send_keys(user)
    sm.findEle('xpath', pwdXPATH)[0].send_keys(pwd, Keys.ENTER)
    
