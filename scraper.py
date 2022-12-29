import os
import json
import re
import requests
import shutil
from bs4 import BeautifulSoup
from slugify import slugify
import subprocess




# listing_pages = [
#     "https://wiki.basgrospoing.fr/index.php/Sp%C3%A9cial:Toutes_les_pages?from=&to=&namespace=0&hideredirects=1",
#     "https://wiki.basgrospoing.fr/index.php?title=Sp%C3%A9cial:Toutes_les_pages&from=Melty+Blood%2FAkiha+Tohno+%28Seifuku%29%2FFull+Moon&hideredirects=1",
#     "https://wiki.basgrospoing.fr/index.php?title=Sp%C3%A9cial:Toutes_les_pages&from=Trish+%28UMVC3%29&hideredirects=1"
# ]

# for page in listing_pages:
#     page = requests.get(page)
#     soup = BeautifulSoup(page.content, "html.parser")
#     links = soup.find("ul", class_='mw-allpages-chunk').find_all("a")
#     for link in links:
#         entry = {"text": link.text, "src": link['href']}
#         print(entry)
# Copy from terminal and clean the json


def create_folder(folder):
    if os.path.exists(folder):
        print("The folder for " + folder + " already exists.")
    else:
        print("Creating " + folder + " folder.")
        os.makedirs(folder)

create_folder("site")
create_folder("site/index.php")
url = "https://wiki.basgrospoing.fr/index.php/"
cache_path = "cache.json"
cache_file = open(cache_path, "r")
cache_text = cache_file.read()
cache_content = json.loads(cache_text)
cache_file.close()

for page in cache_content:
    src = page["src"].split("/")

    if len(src) > 1:
        create_folder("site/index.php/" + src[0])

    subprocess.run("monolith " + url + page['src'] + " -o site/index.php/" + page['src'] + ".html", shell=True)


