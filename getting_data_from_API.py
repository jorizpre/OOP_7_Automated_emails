# For the Excel file or for the email we will just use existing Classes
import requests # to get data from URL (connecting to API)
from pprint import pprint # formatting of URL content import
import json # to convert a dictionary into a JSON file

# For getting news we have 2 options: web scraping and a news API (preferable)
# We use newsAPI.org
# API key: cc70925819264ddebb9d63a1faf2539c


response = requests.get(url)
# content = response.text # extracting data as a string
content = response.json() # getting the data as json file (which Python converts to dictionary)
# json_saving = json.dumps(content) # converting python dictionary into a JSON file

# Saving a JSON file
with open('data.json', 'w') as json_file: json.dump(content, json_file)

# pprint(content)

# Getting the desired data from the dictionary
print(content["articles"][2]["source"]["name"]) # for example, getting the name of the news source of the 3rd article

# Getting data (for example the URL) from all articles
articles_list = content["articles"]
links_list = []
for article in articles_list:
    links_list.append(article["url"])
print(links_list, len(links_list))
