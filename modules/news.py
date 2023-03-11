import keys
import requests
import json
import random

def getHeadlines(country_code):
    url = f'https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={keys.NEWS_KEY}&pageSize=5'
    response = requests.get(url)
    data = json.loads(response.text)
    answer = []

    for article in data["articles"]:
        answer.append(article["title"])
        if(article["description"] != None):
            answer.append(article["description"])

    return answer

