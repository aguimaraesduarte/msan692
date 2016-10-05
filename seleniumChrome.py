import time
from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com')

# here is where some useful work would typically happen
search_box = driver.find_element_by_name('q')
search_box.send_keys('USF Analytics')
search_box.submit()

raw_input("Press Enter to quit")
driver.quit() # close browser