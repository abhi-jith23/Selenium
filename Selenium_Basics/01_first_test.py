'''

Selenium is used to create bots or doing web automation wtih python. 
This file will contain tips on how to automate the folling process:
navigate elements, click on elements, send keys, hit enter, etc. 

'''


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

'''

We set up our chrome driver service and use that to initialize our 
web driver. The way selenium works is, we start by create something 
called web driver, which we download and install from chrome. 

The code will be able to control Chrome for us and be able to 'act' as 
a real user as we automate the browser. 

Now we download chromedriver.exe and extract it in the same location
as the selenium python file (need not be, just give the path to the 
.exe in the code). We have added the file to the executable_path. 

'''

# service = Service(executable_path="chromedriver.exe") # we call function service and give it a path which is a string
# driver = webdriver.Chrome(service=Service) 



# driver.get("https://google.com")

# time.sleep(10) # imported time and called sleep function for 10 seconds to see how the program is working

# driver.quit()

'''
The above code doesn't work. 
https://stackoverflow.com/questions/76915486/selenium-and-python-issue-for-path
It is not needed to download chrome driver and specify a path anymore. 
The built in driver manager of Selenium will do all the work. 
'''

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

'''
Now that we have chromedriver.exe, we have the ability to grab a website. 
'''

driver.get("https://google.com")

time.sleep(5) # this will let the window stay open for 5 seconds

driver.quit() # after 5 seconds the chrome window will close automatically.

