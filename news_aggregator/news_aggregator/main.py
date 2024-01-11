import json

f = open('bbc_articles.json')

data = json.load(f)

merged_text = ''.join(data[0]['text'])

# print(data[0]['url'])
# print(data[0]['title'])
# print(data[0]['text'])
print(merged_text)