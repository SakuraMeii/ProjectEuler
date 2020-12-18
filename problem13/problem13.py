import requests
import bs4

#monospace center
url = "https://projecteuler.net/problem=13"
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text,"html.parser")
targets = soup.find_all("div",class_="monospace center")
data = []
for each in targets:
    data.extend(each.text.split())
with open('data','w') as dataFile:
    for each in data:
        dataFile.write(each+"\n")

sumN = 0
for each in data:
    sumN+=int(each)
print(str(sumN)[0:10])
