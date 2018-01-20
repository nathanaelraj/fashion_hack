import requests
from bs4 import BeautifulSoup
import shutil

base_url = "http://www.livingly.com"
r = requests.get(base_url+"/runway/")
soup = BeautifulSoup(r.text, 'html.parser')

links = soup.find_all("a", class_="designerLink")
for link in links:
    for i in range(1,4):
        r = requests.get(base_url+link["href"]+"/browse?Page="+str(i))
        soup = BeautifulSoup(r.text, 'html.parser')
        thumbnails = soup.find_all("img", height=120)
        for thumbnail in thumbnails:
            r = requests.get(thumbnail["src"], stream=True)
            with open(thumbnail["src"].split("/")[-1], 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
