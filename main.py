# For the Excel file or for the email we will just use existing Classes
import requests # to get data from URL (connecting to API)
from pprint import pprint # formatting of URL content import
import json # to convert a dictionary into a JSON file

# For getting news we have 2 options: web scraping and a news API (preferable)
# We use newsAPI.org
# API key: cc70925819264ddebb9d63a1faf2539c

class NewsFeed:
    
    """ Getting multiple news titles and URLs as a single string
    """

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = f"https://newsapi.org/v2/everything?"\
                f"qInTitle={self.interest}&"\
                f"from={self.from_date}&"\
                f"to={self.to_date}&"\
                "sortBy=publishedAt&"\
                f"language={self.language}&"\
                "apiKey=cc70925819264ddebb9d63a1faf2539c"
        response = requests.get(url)
        content = response.json()
        articles_list = content["articles"]
        email_body= ""
        for article in articles_list:
            email_body= email_body + article["title"] +"\n" + article["url"] + "\n\n"
        return email_body

news_feed = NewsFeed("valencia", "2023-02-15", "2023-02-27", "en")
print(news_feed.get())