import os
import json
import re
import requests
import shutil
from bs4 import BeautifulSoup
from slugify import slugify
import subprocess
import pypandoc

def create_folder(folder):
    if os.path.exists(folder):
        print("The folder for " + folder + " already exists.")
    else:
        print("Creating " + folder + " folder.")
        os.makedirs(folder)



# listing_pages = [
#     "https://wiki.basgrospoing.fr/index.php/Sp%C3%A9cial:Toutes_les_pages?from=&to=&namespace=0&hideredirects=1",
#     "https://wiki.basgrospoing.fr/index.php?title=Sp%C3%A9cial:Toutes_les_pages&from=Melty+Blood%2FAkiha+Tohno+%28Seifuku%29%2FFull+Moon&hideredirects=1",
#     "https://wiki.basgrospoing.fr/index.php?title=Sp%C3%A9cial:Toutes_les_pages&from=Trish+%28UMVC3%29&hideredirects=1"
# ]

# pagelist = []
# for page in listing_pages:
#     page = requests.get(page)
#     soup = BeautifulSoup(page.content, "html.parser")
#     links = soup.find("ul", class_='mw-allpages-chunk').find_all("a")
#     for link in links:
#         entry = {"text": link.text, "src": link['href']}
#         print(entry)
#         pagelist.append(entry)


# # Writing to sample.json
# json_object = json.dumps(pagelist, ensure_ascii=False)
# with open("base_cache2.json", "w") as outfile:
#     outfile.write(json_object)


# create_folder("site")
# create_folder("site/index.php")
# url = "https://wiki.basgrospoing.fr/index.php/"
# cache_path = "cache_finished.json"
# cache_file = open(cache_path, "r")
# cache_text = cache_file.read()
# cache_content = json.loads(cache_text)
# cache_file.close()

# for page in cache_content:
#     src = page["src"].split("/")

#     if len(src) == 2:
#         print(src)
#         create_folder("site/index.php/" + src[0])
    
#     if len(src) == 3:
#         print(src)
#         create_folder("site/index.php/" + src[0] + "/" + src[1] + "/" + src[2])

 
#     subprocess.run("monolith " + url + page['src'] + " -o site/index.php/" + page['src'] + ".html", shell=True)



# cache_path = "cache_width_redirections_ids.json"
# cache_file = open(cache_path, "r")
# cache_text = cache_file.read()
# cache_content = json.loads(cache_text)
# cache_file.close()
# print(len(cache_content))


# pages_path = "sources/pages.json"
# pages_file = open(pages_path, "r")
# pages_text = pages_file.read()
# pages_content = json.loads(pages_text   )
# pages_file.close()

# redirect_path = "sources/redirect.json"
# redirect_file = open(redirect_path, "r")
# redirect_text = redirect_file.read()
# redirect_content = json.loads(redirect_text)
# redirect_file.close()
# print(len(redirect_content))

# newCache = []
# for entry in cache_content:
#     new = entry
#     if "old_id" in entry:
#         for page_entry in pages_content:
#             if entry["old_id"] == page_entry["page_id"]:
#                 new["old_src"] = page_entry["page_title"]
#     newCache.append(new)


# # Writing to sample.json
# json_object = json.dumps(cache_width_ids, ensure_ascii=False)
# with open("cache_width_ids2.json", "w") as outfile:
#     outfile.write(json_object)


# newCache = []

# for entry in cache_content:
#     newEntry = entry
#     for red in redirect_content:
#         if entry["src"] == red["rd_title"]:
#             newEntry["old_id"] = red["rd_from"]
#     newCache.append(newEntry)

# # Writing to sample.json
# json_object = json.dumps(newCache, ensure_ascii=False)
# with open("cache_finished.json", "w") as outfile:
#     outfile.write(json_object)









# cache_path = "cache_finished.json"
# cache_file = open(cache_path, "r")
# cache_text = cache_file.read()
# cache_content = json.loads(cache_text)
# cache_file.close()

# text_path = "sources/text.json"
# text_file = open(text_path, "r")
# text_text = text_file.read()
# text_content = json.loads(text_text   )
# text_file.close()

# revision_path = "sources/revision.json"
# revision_file = open(revision_path, "r")
# revision_text = revision_file.read()
# revision_content = json.loads(revision_text)
# revision_file.close()


# newCache = []
# # for text in text_content:
# #     for revision in revision_content:
# #         if text["old_id"] == revision["rev_text_id"]:
# #             for cache in cache_content:
# #                 newEntry = cache
# #                 if cache["id"] == revision["rev_page"]:
# #                     newEntry["content"] = text["old_text"]
# #                     newCache.append(newEntry)

# for entry in cache_content:
#     newEntry = entry
#     for revision in revision_content:
#         if entry["id"] == revision["rev_page"]:
#             for text in text_content:
#                  if text["old_id"] == revision["rev_text_id"]:
#                     newEntry["content"] = text["old_text"]
#     newCache.append(newEntry)

 

# # Writing to sample.json
# json_object = json.dumps(newCache, ensure_ascii=False)
# with open("cache_with_content.json", "w") as outfile:
#     outfile.write(json_object)



cache_path = "cache_beau.json"
cache_file = open(cache_path, "r")
cache_text = cache_file.read()
cache_content = json.loads(cache_text)
cache_file.close()

create_folder("export")
for entry in cache_content:
    # # Writing to sample.json
    src = entry["src"].split("/")

    if len(src) == 2:
        print(src)
        create_folder("export/" + src[0])
    
    if len(src) == 3:
        print(src)
        create_folder("export/" + src[0] + "/" + src[1] + "/" + src[2])

    content = entry["content"].replace('\n-\n', '-')
    print(entry["src"])
    md = pypandoc.convert_text(content, 'gfm', format='mediawiki')
   
    with open("export/" + entry["src"] +".md", "w") as outfile:
        outfile.write(md)
