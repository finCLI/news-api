# import necessary libraries
from bs4 import BeautifulSoup
import requests
import re
import csv

# function to extract html document from given url
def getHTMLdocument(url):
	# request for HTML document of given url
	response = requests.get(url)
	
	# response will be provided in JSON format
	return response.text
	
url_bitcoin = "https://news.google.com/search?q=bitcoin%20when%3A1h&hl=en-IN&gl=IN&ceid=IN%3Aen"
url_ethereum = "" 
url_cryptocurrency = ""
url_global_finance = ""
url_indian_finance = ""


# create document
html_document = getHTMLdocument(url_bitcoin)

# create soap object
soup = BeautifulSoup(html_document, 'html.parser')

news_link_collection = []
headline = []
news_pubisher = []

# news_link
for link in soup.find_all('a', attrs={'class': 'VDXfz'}):
    news_link = "https://news.google.com" + (link.get('href'))[1:-1]
    news_link_collection.append(news_link)

# news_headline
for i in soup.find_all('a', attrs={'class':'DY5T1d RZIKme'}):
    headline.append(i.text)

# news_publsher
for i in soup.find_all('a', attrs={'class':'wEwyrc AVN2gc uQIVzc Sksgp'}):
    news_pubisher.append(i.text)    

header = ['news_publisher', 'news_headline', 'news_link']


with open('bitcoin.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(len(news_link_collection)):
        data = [news_pubisher[i], headline[i], news_link_collection[i]]
        writer.writerow(data)