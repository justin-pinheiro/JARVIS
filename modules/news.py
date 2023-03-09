import keys
import requests
import json
import random

def getHeadlines():
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={keys.NEWS_KEY}&pageSize=5'
    response = requests.get(url)
    data = json.loads(response.text)
    answer = ""

    answer += random.choice([   
        "Of course, here are the latest headlines for you.",    
        "Sure, let me pull up the news for you.",    
        "Absolutely, I can give you a rundown of the news.",    
        "Certainly, here's what's been happening in the world today.",    
        "No problem, I can update you on the latest news and events.",    
        "Yes, here are the top stories of the day.",    
        "I'd be happy to, here's the latest news from around the world.",    
        "Certainly, let me give you a quick summary of the news.",    
        "Of course, here's your daily news briefing.",    
        "Yes, here's what's making headlines at the moment.",    
        "Sure thing, let me give you the latest news updates.",    
        "Absolutely, here are the top stories you need to know today.",    
        "Yes, here's the latest news and current events.",    
        "No problem, let me give you a quick rundown of the news.",    
        "Certainly, here's your daily dose of news and information."
    ])

    answer += ".........."
    for article in data["articles"]:
        answer += article["title"]
        answer += ".........."
        if(article["description"] != None):
            answer += article["description"]
            answer += ".........."

    return answer

