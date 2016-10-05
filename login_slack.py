from loginAndPassword import login
import time
from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')

def login_and_show_channel(channel):
    driver.get('https://msan-usf.slack.com')
    userfield = driver.find_element_by_id('email')
    passwordfield = driver.find_element_by_id('password')
    user, password = login()
    userfield.send_keys(user)
    passwordfield.send_keys(password)
    passwordfield.submit()

    driver.get('https://msan-usf.slack.com/messages/%s/' % channel)

def parse_slack():
	time.sleep(5)
	msgs = driver.find_elements_by_tag_name('ts-message')

	res = []
	for elem in msgs:
		msg = elem.find_element_by_class_name('message_body').text
		usr_content = elem.find_element_by_class_name('message_content')
		usr = usr_content.find_element_by_tag_name('a').text
		res.append((usr, msg))

	return res

login_and_show_channel("general")
msgs = parse_slack()
for user, msg in msgs:
    print "%s: %s" % (user, msg)

raw_input("Press Enter to quit")
driver.quit() # close browser