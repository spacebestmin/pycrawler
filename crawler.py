import requests
from bs4 import BeautifulSoup
#stable source from whitehouse : https://www.whitehouse.gov/briefings-statements/
result = requests.get("https://www.google.co.uk/webhp?hl=en")

# to make sure that the website is accesible
# print(result.status_code)

# http header
# print(result.headers)

# storing the page content of the wbesite accessed
src = result.content
# print(src)

# using BeautifulSoup module to parse and process the source
# to do so, we create a BeautifulSoup object 
# based on the source variable we created above
soup = BeautifulSoup(src, 'lxml')

# now we can access specific informatino directly from it...
# ex)list of all of the links on the page 

links = soup.find_all("a")
# print(links)
# print("\n")

 # say that we just want to extract the link that has contains the text
#  "about" on the page instead of every link... 
# we can use the built-in TEXT FUCNTION to access the text conent between a tag

for link in links:
    if "About" in link.text:
        print(link)
        print(link.attrs['href'])