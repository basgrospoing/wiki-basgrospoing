import os
import json
import pypandoc

def create_folder(folder):
    if os.path.exists(folder):
        print("The folder for " + folder + " already exists.")
    else:
        print("Creating " + folder + " folder.")
        os.makedirs(folder)


## PAGE GENERATOR

cache_path = "api_cache.json"
cache_file = open(cache_path, "r")
cache_text = cache_file.read()
cache_content = json.loads(cache_text)
cache_file.close()

create_folder("../markdown")

for entry in cache_content:
    # # Writing to sample.json
    src = entry["src"].split("/")

    if len(src) == 2:
        print(src)
        create_folder("../markdown/" + src[0])
    
    if len(src) == 3:
        print(src)
        create_folder("../markdown/" + src[0] + "/" + src[1])

    date = entry["date"].split("T")
    frontmatter = '---\ntitle: "' + entry["text"] + '"\nslug:  "' + entry["src"] + '"\nid: ' + str(entry["id"]) + '\nauthor: "' + entry["author"] + '"\n' + 'permalink:  "{{ slug }}.html"\n'  + 'layout: "' + entry["type"] +'.njk"\n' + 'tags: "' + entry["type"] +'"\n' + 'date: "' + date[0] +'"\n' 

    
    if "old_src" in entry:
        frontmatter += 'redirect: "'  + entry["old_src"] + '"\n'
    
    if "old_id" in entry:
        frontmatter += "old_id: "  + entry["old_id"] + "\n"
        
    frontmatter += "---\n\n"

    content = entry["content"].replace('\n-\n', '-')
    print(entry["src"])
    md = frontmatter + pypandoc.convert_text(content, 'gfm', format='mediawiki')
   
    with open("../markdown/" + entry["src"] +".md", "w") as outfile:
        outfile.write(md)
