import frontmatter
import os,glob
import requests
import json

def isgoodipv4(s):
    pieces = s.split('.')
    if len(pieces) != 4: return False
    try: return all(0<=int(p)<256 for p in pieces)
    except ValueError: return False


urlstart = "https://wiki.basgrospoing.fr/api.php?action=query&titles="
urlend = "&rvprop=user&prop=revisions&rvlimit=500&format=json"

folder_path = 'markdown'
for filename in glob.glob(os.path.join(folder_path, '*.md')):
  with open(filename, 'r') as f:
    newFilename = filename
    print(filename)
    file = f.read()
    post = frontmatter.loads(file)
    title = post["title"]
    pageId = post["id"]
    response = requests.get(urlstart + title + urlend)
    authors = []
    if response.status_code == 200:
        content = json.loads(response.content.decode('utf-8'))
        revisions = content["query"]["pages"][str(pageId)]["revisions"]
        
        for rev in revisions:
            user = rev["user"]
            if user == "Atomskyu690" or user == "Atomskyu698":
                user = "Atomskyu"
            if user == "Alx":
                user = "ALX"
            if user == "Dan sakazaki":
                user = "Dan Sakazaki"
            if user != "Admin" and user != "MediaWiki default" and isgoodipv4(user) is False and user not in authors:
                authors.append(user)

    authors_str = str(", ".join(authors))
    if authors_str == '':
        authors_str = "Neithan"
    print(authors_str)
    post["author"] = authors_str

    with open(filename, "w") as outfile:
        outfile.write(frontmatter.dumps(post))
