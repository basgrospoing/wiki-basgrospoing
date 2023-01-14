import os
import json
import pypandoc

def create_folder(folder):
    if os.path.exists(folder):
        print("The folder for " + folder + " already exists.")
    else:
        print("Creating " + folder + " folder.")
        os.makedirs(folder)


# PAGE GENERATOR

cache_path = "api_cache.json"
cache_file = open(cache_path, "r")
cache_text = cache_file.read()
cache_content = json.loads(cache_text)
cache_file.close()

create_folder("../markdown")

htaccess = "RewriteEngine On\nCheckSpelling On\nCheckCaseOnly On\n"

for entry in cache_content:
    src = entry["src"].split("/")
    date = entry["date"].split("T")
    frontmatter = '---\ntitle: "' + entry["text"] + '"\nslug:  "' + entry["src"] + '"\nid: ' + str(entry["id"]) + '\nauthor: "' + entry["author"] + '"\n' + 'permalink: "' + entry["permalink"] +  '.html"\n'  + 'layout: "' + entry["type"] +'.njk"\n' + 'tags: "' + entry["type"] +'"\n' + 'date: "' + date[0] +'"\n' 

    if "old_src" in entry:
        frontmatter += 'redirect: "'  + entry["old_src"] + '"\n'
    
    if "old_id" in entry:
        frontmatter += "old_id: "  + entry["old_id"] + "\n"
        
    frontmatter += "---\n\n"

    content = entry["content"].replace('\n-\n', '-')
    print(entry["src"])
    md = frontmatter + pypandoc.convert_text(content, 'gfm', format='mediawiki')
   
    with open("../markdown/" + entry["permalink"] +".md", "w") as outfile:
        outfile.write(md)

    if entry["type"] != "index":
        srcRedirect =  'Redirect 302 /'+ entry["src"] + ' /' + entry["permalink"] + '.html\n'
        srcRedirect2 =  'Redirect 302 /index.php/'+ entry["src"] + ' /' + entry["permalink"] + '.html\n'
        oldSrcRedirect = ""
        if "old_src" in entry:
            oldSrcRedirect =  'Redirect 302 /'+ entry["old_src"] + ' /' + entry["permalink"] + '.html\n'
            oldSrcRedirect2 =  'Redirect 302 /index.php/'+ entry["old_src"] + ' /' + entry["permalink"] + '.html\n'
        
        htaccess += srcRedirect + srcRedirect2 + oldSrcRedirect + oldSrcRedirect2

with open("../markdown/.htaccess", "w") as outfile:
    outfile.write(htaccess)

# ADD PERMALINKS

# cache_path = "api_cache.json"
# cache_file = open(cache_path, "r")
# cache_text = cache_file.read()
# cache_content = json.loads(cache_text)
# cache_file.close()

# slug_path = "slugs.json"
# slug_file = open(slug_path, "r")
# slug_text = slug_file.read()
# slug_content = json.loads(slug_text)
# slug_file.close()

# print(len(slug_content))
# new_cache = []
# for entry in cache_content:
#     newEntry = entry
#     for sl in slug_content:
#         print(sl["slug"])
#         if entry["src"] == sl["slug"]:
#             newEntry["permalink"] = sl["slugify"]
#             new_cache.append(newEntry)

# json_object = json.dumps(new_cache, ensure_ascii=False)
# with open("api_cache_permalinks.json", "w") as outfile:
#     outfile.write(json_object)
