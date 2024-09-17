from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()

# Sets up ChromeDriver service using webdriver manager
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)

# Opens the Google Forms link
browser.get('https://docs.google.com/forms/d/e/1FAIpQLSeqAyJkf3FnfwxnChqINt-XpmYl1FE7u9x2QQqboPRi5Yk_GA/viewform')

# Fills in the text input field for the first question (Name)
browser.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('Name')

# Fills in the text input field for the second question (Age)
browser.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('35')

# Selects an option for a multiple-choice question (e.g., gender or another radio question)
browser.find_element('xpath', '//*[@id="i16"]/div[3]/div').click()

# Clicks on a response for a special input type question
browser.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[1]/span').click()

# Waits briefly to ensure the next element is loaded
time.sleep(3)

# Clicks a button to submit or confirm an answer for another question
browser.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[3]').click()

# Waits for another second before proceeding
time.sleep(1)

# Submits the form by clicking the final submit button
browser.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
