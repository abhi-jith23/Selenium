'''

Sometimes it'll take a while to load the website so before then we can 
try to access elements that doesn't exist yet. 
Imported the last two to wait for the presence of an element before going 
forward so we don't run into any issue if the element we're searching for
doesn't exist yet. 

'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://google.com")

'''
If the internet connection is slow, this code will make the program wait 
until this element exists. Once it exists, it will find it, access it and 
won't get an error stating that element doesn't exist in the page. 
The code below will use the webdriver and wait until it locates an element
by its class name that has the ID "gLFyf"
'''

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf")) #These extra set of parantheses is needed. 
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear() 
input_element.send_keys("World's Biggest Gorilla" + Keys.ENTER)

'''
To click on another link which will redirect to another page, we use the code
below. This will search for text in the quotes within the <a></a> (anchor tag)
and click on the first element since the find_element() will search for the 
first element with the corresponding search parameters. 
And repeating the same WebDriverWait function to make sure the process finds the 
element we're looking for, in this case PARTIAL_LINK_TEXT. 
'''

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Largest Gorilla")) #These extra set of parantheses is needed. 
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Largest Gorilla")
link.click()

time.sleep(10)

driver.quit()
