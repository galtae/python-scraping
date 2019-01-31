import requests

res = requests.get('http://www.jetbrains.com/idea/img/screenshots/idea_overview_5_1.png')
# print(res.content)

with open('img.png', 'wb') as f:
    f.write(res.content)
