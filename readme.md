# **Welcome to Selenium Implementation Simplifier**
## *Must know*
1. The libraries support Chrome driver only
2. The libraries are only tested on Windows
3. For simplicity, the libraries locate elemets by XPATH only

## *Installation*
1. pip install selenium
2. Get a copy of chromedriver.exe from [here](https://chromedriver.chromium.org/)

## *Setting up in your scripts*
```
import seleniumMain
import seleniumLogin (optional and depends on seleniumMain.py)
```

## *Available functions*<br>
seleniumMain:
1. startChrome(url, driverPath): start automation
  - driverPath = the path of chormedriver.exe
  - This function **must** be called first in your scripts

Browser controls<br>
2. loadUrl(url): load a url<br>
3. goBack(): load the previous page<br>
4. goBackUsingCache(): load the previous page faster but at the cost of not updating the page content<br>
5. goForward(): load the next page from browsing history<br>
6. f5(): reload page<br>
7. end(): terminate the automation process, but not the entire program<br>
8. getCurURL() --> string: get current URL

Element interactions<br>
9. eleExists(inXPATH) --> boolean: check if element exists, return True if so<br>
10. waitForEle(inXPATH, timeoutSeconds): wait until the element can be located, end the automation when time is up<br>
11. f5UntilEleExists(inXPATH): keep refreshing until the element can be located<br>
12. getEleText(inXPATH): return the text of an element<br>
13. clickEle(inXPATH): click an element<br>
14. sendTextAndEnter(inXPATH, txt): input text in a textbox/textarea and press enter key<br>
15. sendText(inXPATH, txt): input text in a textbox/textarea<br>
16. screenshot(inXPATH, outPath): screenshot an element<br>
 - outPath = output path with file name

seleniumLogin:
1. login(userXPATH, pwdXPATH, loginBtnXPATH, user, pwd): perform login process
 - userXPATH = input element that asks for userID/email
 - pwdXPATH = input element that asks for password
 - loginBtnXPATH = the login button
 - user = your userID/email
 - pwd = your password

## *Running in IDLE*
In your IDLE, type the following code:
```
import sys
sys.path.append(r"the path that stores the libraries")
import seleniumMain as sm
#do your things here
```
