from selenium import webdriver

chrome_browser = webdriver.Chrome("./autotesting/chromedriver")

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
title_exist = 'Selenium Easy Demo - Simple Form to Automate using Selenium' in chrome_browser.title
assert title_exist

show_message_botton = chrome_browser.find_element_by_class_name("btn-default")

user_message = chrome_browser.find_element_by_id("user-message")
user_message.clear()
user_message.send_keys('This is so cool')

show_message_botton.click()

output_message = chrome_browser.find_element_by_id("display")

assert 'This is so cool' in output_message.text

chrome_browser.close()

#print(botton)
