import seleniumMain as sm

def login(userXPATH, pwdXPATH, loginBtnXPATH, user, pwd):
    sm.sendText(userXPATH, user)
    sm.sendText(pwdXPATH, pwd)
    sm.clickEle(loginBtnXPATH)
    
