import requests
from bs4 import BeautifulSoup
import urllib.parse

animals = ['peacock', 'rubber plant', 'elephant', 'lion', 'giraffe', 'cockroach', 'apple', 'toucan']

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

for animal in animals:
    encoded_animal = urllib.parse.quote(animal)
    link = f"https://www.google.com/search?q=scientific+name+of+{encoded_animal}"
    
    req_novo = requests.get(link, headers=headers)
    
    site_animal = BeautifulSoup(req_novo.text, 'html.parser')
    
    scientific_name = site_animal.find("div", class_="Z0LcW t2b5Cf")
    
    if not scientific_name:
        scientific_name = site_animal.find("div", class_="HwtpBd gsrt PZPZlf kTOYnf") 
    if not scientific_name:
        scientific_name = site_animal.find("div", class_="PZPZlf ssJ7i B5dxMb") 

    if scientific_name:
        sfname = scientific_name.get_text()
        print("==================================")
        print(f"Scientific name of {animal.capitalize()}: {sfname}")
        print("==================================")
    else:
        print(f"Sorry, scientific name for {animal} could not be found.")
