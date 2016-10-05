import time
from selenium import webdriver
from loginAndPassword import login

driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://twitter.com/login')

# here is where some useful work would typically happen
userfield = driver.find_element_by_css_selector('.js-username-field.email-input.js-initial-focus')
passwordfield = driver.find_element_by_css_selector('.js-password-field')
username, password = login()
userfield.send_keys(username)
passwordfield.send_keys(password)
passwordfield.submit()

driver.get('https://twitter.com/DataInstituteSF')
following = driver.find_element_by_xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[2]/a')
following.click()

time.sleep(5)

driver.execute_script("window.scrollTo(0, 10000);")
driver.execute_script("window.scrollTo(0, 10000);")

links = driver.find_elements_by_css_selector('a.ProfileNameTruncated-link')
for link in links:
	print "%s\t%s" % (link.get_attribute('href'), link.text)

raw_input("Press Enter to quit")
driver.quit() # close browser