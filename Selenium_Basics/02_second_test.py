'''

In this file we code to search for elements in HTML and once 
we have access we can interact with it. 
Here we need to find the google search field, click on it, 
type something and hit enter to search it. 

By is used to access specific elements inside a webpage when 
using Selenium WebDriver. 
Keys is used to execute keyboard keys such as directional and 
Enter keys. 

'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://google.com")

'''
To access the elements inside the webpage, you start by accessing
inspect element, and right clicking on the search box will give you 
the search box's element in the code. You use this class name in the 
code below to access the search box. 
We require some kind of identifier to access the element, it can be 
the class name or the ID or the tag name, there's different ways to 
access it. But here we use CLASS_NAME.
Here we search by CLASS_NAME so we look for the first element in the 
page that has this class and we can access it and interact with it.  
'''

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
'''
The clear function might be useful because sometimes there might be
some text in the text/search box that we should remove before typing
our text, and the clear() function will do it for us. 
The send_keys function will not override the already existing text, but 
will merely append to it. 
'''
input_element.clear()
input_element.send_keys("World's Biggest Gorilla" + Keys.ENTER)

time.sleep(5)

driver.quit()

'''
Check the next file for more.
'''