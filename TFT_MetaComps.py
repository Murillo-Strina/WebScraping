from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import re

link = 'https://www.metatft.com/comps'

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
browser.get(link)

html_content = browser.page_source
site = BeautifulSoup(html_content, 'html.parser')

def search_comps(composition):
    comp_name = composition.find('div', class_='CompRowName').text.strip()
    comp_name = re.sub(r'lvl.*', '', comp_name).strip() 
    comp_name = re.sub(r'(Easy|Medium|Fast|Hard|Standard)', '', comp_name).strip() 
    comp_name = re.sub(r'[0-9]', '', comp_name).strip() 

    pieces = [piece.text.strip() for piece in composition.find_all('div', class_='UnitNames')][:9]
    avg_place = composition.find('div', id=re.compile('stat_1_')).get_text(strip=True) if composition.find('div', id=re.compile('stat_1_')) else "N/A"
    pick_rate = composition.find('div', id=re.compile('stat_2_')).get_text(strip=True) if composition.find('div', id=re.compile('stat_2_')) else "N/A"
    win_rate = composition.find('div', id=re.compile('stat_3_')).get_text(strip=True) if composition.find('div', id=re.compile('stat_3_')) else "N/A"
    top_4_rate = composition.find('div', id=re.compile('stat_4_')).get_text(strip=True) if composition.find('div', id=re.compile('stat_4_')) else "N/A"

    return {
        'name': comp_name,
        'pieces': pieces,
        'avg_place': avg_place,
        'pick_rate': pick_rate,
        'win_rate': win_rate,
        'top_4_rate': top_4_rate
    }

def first_piece_items(composition):
    first_piece = composition.find('div', class_='ItemsContainer_Inline')  
    items = first_piece.find_all('img', alt=True) 
    return [item['alt'] for item in items[:3]]  

compositions = site.find_all('div', class_=re.compile('CompRowWrapper.*'))
comps = [search_comps(comp) for comp in compositions][:3] 


with open('CompsMetaTFT.txt', 'w', encoding='utf-8') as f:
    f.write(f"Top compositions of this Patch:\n")
    for i, comp in enumerate(comps, 1):
        f.write(f"\nComposition {i}:\n")
        f.write(f"Name: {comp['name']}\n")
        f.write(f"Pieces: {', '.join(comp['pieces'])}\n")
        f.write(f"First piece items: {', '.join(first_piece_items(compositions[i-1]))}\n")
        f.write(f"Avg Place: {comp['avg_place']}\n")
        f.write(f"Pick Rate: {comp['pick_rate']}\n")
        f.write(f"Win Rate: {comp['win_rate']}\n")
        f.write(f"Top 4 Rate: {comp['top_4_rate']}\n")
        f.write('-' * 50 + '\n')

browser.quit()
