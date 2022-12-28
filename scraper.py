import os
import json
import re
import requests
import shutil
from bs4 import BeautifulSoup
from slugify import slugify

cache_path = "cache.json"
cache_file = open(cache_path, "r")
cache_text = cache_file.read()
cache_content = json.loads(cache_text)
cache_file.close()

for page in cache_content:
    print(page)
    res = requests.get(page)
    soup = BeautifulSoup(res.content, "html.parser")
    title = soup.find("h1")
    title = title.contents[0]
    print(title)
    main = str(soup.find("main"))
    re.sub(r"<p><br/>[\S\s]<\/p>", "", main)
    re.sub(r"<\/ul>(.+?)<ul>", "", main)
    main = main.replace("<br/>", "")
    file = open(slugify(title) + '.html', 'w')
    file.write(main)
    file.close()