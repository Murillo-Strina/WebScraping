from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re
import time

link = 'https://www.imdb.com/list/ls002206094/?sort=popularity%2Casc'

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
browser.get(link)

html_content = browser.page_source
site = BeautifulSoup(html_content, "html.parser")

movies = site.find_all('h3', class_='ipc-title__text')

movie_list_popular = []

for title in movies:
    if re.match(r'^\d+\..*', title.text.lstrip()):
        movie_list_popular.append(title.text.lstrip())

browser.find_element(By.XPATH, '//*[@id="sort-by-selector"]').click()
time.sleep(2)

browser.find_element(By.XPATH, '//*[@id="sort-by-selector"]/option[3]').click()
time.sleep(3)

html_content_imdb = browser.page_source
site_imdb = BeautifulSoup(html_content_imdb, "html.parser")

movies_imdb = site_imdb.find_all('h3', class_='ipc-title__text')

movie_list_imdb = []

for title_imdb in movies_imdb:
    if re.match(r'^\d+\..*', title_imdb.text.lstrip()):
        movie_list_imdb.append(title_imdb.text.lstrip())

with open('movies.txt', 'w', encoding='utf-8') as f:
    f.write("Popular Movies\n")
    f.write("="*30 + "\n")
    for movie in movie_list_popular:
        f.write(f"{movie}\n")
    
    f.write("\n" + "-"*30 + "\n\n")
    
    f.write("IMDb Sorted Movies\n")
    f.write("="*30 + "\n")
    for movie in movie_list_imdb:
        f.write(f"{movie}\n")

print("The list was successfully saved in 'movies.txt'.")

browser.quit()
