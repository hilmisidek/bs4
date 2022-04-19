from bs4 import BeautifulSoup
import lxml
import requests

response=requests.get("https://news.ycombinator.com/")
yc_web_page=response.text

#with open("https://news.ycombinator.com/") as file:
#    contents = file.read()

soup=BeautifulSoup(yc_web_page, "html.parser")
#print(soup.title)
#print(soup.title.string)
#print (soup.prettify())
article1=soup.find_all(name="a", class_="titlelink")
article_texts=[]
article_links=[]

for alllink in article1:
    article1_text=alllink.getText()
    article_texts.append(article1_text)
    article1_url=alllink.get("href")
    article_links.append(article1_url)

article1_upvote=[score.getText() for score in soup.find_all(name="span", class_="score")]
intUpvote=[]
for extracted in article1_upvote:
    intUpvote.append(int(extracted.split(" ")[0]))
largest_number = max(intUpvote)
largest_index = intUpvote.index(largest_number)

print (article_texts[largest_index])
print (article_links[largest_index])

print (article_texts)
print (article_links)
print (intUpvote)

