from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time
import re
import requests

def get_filename_from_cd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]

# Initialize
options = Options()
options.headless = True
options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"')
driver = webdriver.Firefox(options=options)

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

    for a in soup.findAll('div', class_="mb-4"):
        song = a.find('a', href = re.compile(r'.*beatmaps.*'))
        time.sleep(0.1)
        if song != None:
            song_id = requests.get(song['href']).url.split('/')[4].split('#')[0];
            print(f"{song_id}")
            r = requests.get(f"https://kitsu.moe/api/d/{song_id}", allow_redirects=True)  
            filename = get_filename_from_cd(r.headers.get('content-disposition')).replace('"', '')
            with open(f'{path}{filename}', 'wb') as f:
                f.write(r.content)
    
if __name__ == "__main__":    
    parse_url_song("https://osucollector.com/collections/4515", r"C:\Users\merda\Documents\Osu_maps" + "\\")
    driver.quit()
