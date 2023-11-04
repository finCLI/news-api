# import necessary libraries
from bs4 import BeautifulSoup
import requests
import re
import csv
import json
from datetime import datetime

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
url_indian_startups = "https://news.google.com/search?q=indian%20startups%20%20when%3A1h&hl=en-IN&gl=IN&ceid=IN%3Aen"
url_indian_tech = "https://news.google.com/search?q=indian%20tech%20%20when%3A1h&hl=en-IN&gl=IN&ceid=IN%3Aen"

def getData(url_topic):
    '''Function to scrape news data from the given url.
    Returns:
        (news_link_collection:list, headline:list, news_publisher:list):tuple
    '''

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

    # news_publisher
    for i in soup.find_all('a', attrs={'class':'wEwyrc'}):
        news_publisher.append(i.text)
    
    return news_link_collection, headline, news_publisher


def createCSVData(url_topic, topic_csv_name):
    '''
    Calls function getData(url) to get data, restructures and saves as csv files

    Returns
    None
    '''
    # Calling the getData() Function
    news_link_collection, headline, news_publisher = getData(url_topic)

    header = ['news_publisher', 'news_headline', 'news_link']

    complete_path = "./../data/"+topic_csv_name
    with open(complete_path, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range(len(news_link_collection)):
            data = [news_publisher[i], headline[i], news_link_collection[i]]
            writer.writerow(data)


def createJSONData(url_topic, json_filename):
    '''
    Calls function getData(url) to get data, restructures and saves as json files

    Returns
    None
    '''

    # Calling the getData() Function
    news_link_collection, headline, news_publisher = getData(url_topic) 

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


def getJSONData(url_topic):
    '''
    Calls function getData(url) to get data, restructures and returns json data.

    Returns
    list of dictionaries of news data.
    '''
    # Calling the getData() Function
    news_link_collection, headline, news_publisher = getData(url_topic) 

    sample_data = []
    for i in range(min(len(news_link_collection), 5)):
        json_data = {
                    "id": i,
                    "news_publisher" : news_publisher[i],
                    "news_headline": headline[i],
                    "news_link": news_link_collection[i]
                }
        sample_data.append(json_data)
    
    return sample_data

def callForAllTopics():
    return {
        "india": getJSONData(url_indian_finance), 
        "globe": getJSONData(url_global_finance),
        "tech": getJSONData(url_indian_tech),
        "startups": getJSONData(url_indian_startups),
        "crypto": getJSONData(url_cryptocurrency)
        }

def get_latest_news(payload):
    print(">> Payload", payload)
    if payload:
        payload_hour = payload["current_hour"]
    hour = datetime.now().strftime("%H")
    # if payload_hour <= hour:
    #     return "from DB"
    # else:
    #     return callForAllTopics()
    return callForAllTopics()

def get_health():
    return "active"

if __name__ == "__main__":
    # So that this function does not run during import of file
    createAllJSONData()