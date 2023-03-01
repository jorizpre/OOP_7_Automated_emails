# For the Excel file or for the email we will just use existing Classes
import requests # to get data from URL
from pprint import pprint # formatting of URL content import

# For getting news we have 2 options: web scraping and a news API (preferable)
# We use newsAPI.org
# API key: cc70925819264ddebb9d63a1faf2539c

class NewsFeed:

    def __init__(self, data):
        self.data = data
    
    def get(self):
        pass
url = "https://newsapi.org/v2/everything?"\
      "qInTitle=Valencia&"\
      "from=2023-02-01&"\
      "sortBy=publishedAt&"\
      "language=en&"\
      "apiKey=cc70925819264ddebb9d63a1faf2539c"

response = requests.get(url)
# content = response.text # extracting data as a string
content = response.json # getting the data as json file (which Python converts to dictionary)
pprint(content)

content_file = json.dumps(content)