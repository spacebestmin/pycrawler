from bs4 import BeautifulSoup

# to keep things simple and aolso reproducible, consider the following html code

html_doc="""
<html><head><title>The Dormouse's stordy </title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; their names:
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link1">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link1">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>

<b class="boldest">Extremely bold</b>
<blockquote class="boldest">Extremely bold</blockquote>
<b id="1">Test 1</b>
<b another-attribute="1" id="verybold">test 2</b>
<p id="my id"></p></htnl>
"""

with open('index.html', 'w') as f:
    f.write(html_doc)

soup = BeautifulSoup(html_doc, "lxml")

#print(soup.prettify())
#print(soup)

#print(soup.p) #bold <b> tags are printed
#finds the FIRST tag with b tag

#the find funtions also does the same
#print(soup.find('b'))
#again, the first finding will be printed
