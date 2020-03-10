
#let's obtain the linkes from the following websiite
#https://www.whitehouse.gov/briefings-statements/

#one of the things this website consists of is records of presidential
#briefings and statements

#Goal : Extract all of the links on the page that points to the briefings and statements

import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefings-statements/")
src = result.content
soup = BeautifulSoup(src, 'lxml')
#looping through the links


urls = []
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find('a')
    urls.append(a_tag.attrs['href'])

print(urls)
