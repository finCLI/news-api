# import necessary libraries
from bs4 import BeautifulSoup
import requests
import re
import csv
import json

# function to extract html document from given url
def getHTMLdocument(url):
	# request for HTML document of given url
	response = requests.get(url)
	
	# response will be provided in JSON format
	return response.text
	
url_bitcoin = "https://news.google.com/search?q=bitcoin%20when%3A1h&hl=en-IN&gl=IN&ceid=IN%3Aen"
url_ethereum = "https://news.google.com/search?q=ethereum%20when%3A1h&hl=en-IN&gl=IN&ceid=IN%3Aen" 
url_cryptocurrency = "https://news.google.com/search?q=cryptocurrency%20when%3A1h&hl=en-IN&gl=IN&ceid=IN%3Aen"
url_global_finance = "https://news.google.com/search?q=finance%2C%20world%20when%3A1h&hl=en-IN&gl=IN&ceid=IN%3Aen"
url_indian_finance = "https://news.google.com/search?q=indian%20finance%20%20when%3A1h&hl=en-IN&gl=IN&ceid=IN%3Aen"


def createCSVData(url_topic, topic_csv_name):
    # create document
    html_document = getHTMLdocument(url_topic)

    # create soap object
    soup = BeautifulSoup(html_document, 'html.parser')

    news_link_collection = []
    headline = []
    news_publisher = []

    # news_link
    for link in soup.find_all('a', attrs={'class': 'VDXfz'}):
        news_link = "https://news.google.com" + (link.get('href'))[1:-1]
        news_link_collection.append(news_link)

    # news_headline
    for i in soup.find_all('a', attrs={'class':'DY5T1d RZIKme'}):
        headline.append(i.text)

    # news_publsher
    for i in soup.find_all('a', attrs={'class':'wEwyrc AVN2gc uQIVzc Sksgp'}):
        news_publisher.append(i.text)    

    header = ['news_publisher', 'news_headline', 'news_link']

    complete_path = "./../data/"+topic_csv_name
    with open(complete_path, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range(len(news_link_collection)):
            data = [news_publisher[i], headline[i], news_link_collection[i]]
            writer.writerow(data)

def createJSONData(url_topic, json_filename):

    # create document
    html_document = getHTMLdocument(url_topic)

    # create soap object
    soup = BeautifulSoup(html_document, 'html.parser')

    news_link_collection = []
    headline = []
    news_publisher = []

    # news_link
    for link in soup.find_all('a', attrs={'class': 'VDXfz'}):
        news_link = "https://news.google.com" + (link.get('href'))[1:-1]
        news_link_collection.append(news_link)

    # news_headline
    for i in soup.find_all('a', attrs={'class':'DY5T1d RZIKme'}):
        headline.append(i.text)

    # news_publsher
    for i in soup.find_all('a', attrs={'class':'wEwyrc AVN2gc uQIVzc Sksgp'}):
        news_publisher.append(i.text)  

    complete_path = "./../data/" + json_filename
    sample_data = []
    for i in range(len(news_link_collection)):
        json_data = {
                    "id": i,
                    "news_publisher" : news_publisher[i],
                    "news_headline": headline[i],
                    "news_link": news_link_collection[i]
                }

        with open(complete_path,'w+') as file:
            sample_data.append(json_data)
            json.dump(sample_data, file, indent = 4)


def createAllCSVData():
    createCSVData(url_bitcoin, 'bitcoin.csv')
    createCSVData(url_ethereum, 'ethereum.csv') 
    createCSVData(url_cryptocurrency, 'cryptocurrency.csv')           
    createCSVData(url_global_finance, 'globalfinance.csv')
    createCSVData(url_indian_finance, 'indianfinance.csv')

def createAllJSONData():
    createJSONData(url_bitcoin, 'bitcoin.json')
    createJSONData(url_ethereum, 'ethereum.json') 
    createJSONData(url_cryptocurrency, 'cryptocurrency.json')           
    createJSONData(url_global_finance, 'globalfinance.json')
    createJSONData(url_indian_finance, 'indianfinance.json')

createAllJSONData()