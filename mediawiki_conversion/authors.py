import json

cache_path = "cleaned_data/formated_data.json"
cache_file = open(cache_path, "r")
cache_text = cache_file.read()
cache_content = json.loads(cache_text)
cache_file.close()

revision_path = "bdd_exports/revision.json"
revision_file = open(revision_path, "r")
revision_text = revision_file.read()
revision_content = json.loads(revision_text)
revision_file.close()


newCache = []
for entry in cache_content:
    newEntry = entry
    for revision in revision_content:
        if entry["id"] == revision["rev_page"]:
            newEntry["author"] = revision["rev_user_text"]
    newCache.append(newEntry)

# Writing to sample.json
json_object = json.dumps(newCache, ensure_ascii=False)
with open("test.json", "w") as outfile:
    outfile.write(json_object)

