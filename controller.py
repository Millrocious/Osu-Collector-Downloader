from pickle import APPEND
from turtle import ht
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time
import re
import requests

# Initialize
options = Options()
options.headless = True
options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"')
#driver = webdriver.Firefox(options=options)

driver = webdriver.Chrome(r"C:\Users\merda\Documents\python_pr\chromedriver.exe" )
driver.get("http://www.google.com")

# Get all url of beatmaps
beatmaps = list()
def parse_url_song(url, path):
    url_collection = url
    driver.get(url_collection)
    SCROLL_PAUSE_TIME = 1.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        
    # Storing the page source in page variable
    time.sleep(SCROLL_PAUSE_TIME)
    page = driver.page_source
    soup = BeautifulSoup(page, "html.parser")
    #print(page)

    count = 0
    for a in soup.findAll('a', href = re.compile(r'.*beatmaps.*')):
        count += 1
        time.sleep(SCROLL_PAUSE_TIME)
        #https://api.chimu.moe/v1/download/
        link = driver.get(a['href'])
        time.sleep(0.3)
        spage = driver.page_source
        sp = BeautifulSoup(spage, 'html.parser')
        song = sp.find_all('a', class_='beatmapset-header__details-text-link')
        song_id = driver.current_url.split('/')[4].split('#')[0]
        try:
            print(f"{song_id} {song[1].text} - {song[0].text}.osz")
            r = requests.get(f"https://api.chimu.moe/v1/download/{song_id}")  
            with open(f'{path}{song_id} {song[1].text} - {song[0].text}.osz', 'wb') as f:
                f.write(r.content)
        except:
            print("Doesn't exist")
    
if __name__ == "__main__":    
    #parse_url_song("https://osucollector.com/collections/4518")
    parse_url_song("https://osucollector.com/collections/4515", r"C:\Users\merda\Documents\Osu_maps" + "\\")
    driver.quit()
