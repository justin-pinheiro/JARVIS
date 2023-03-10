from selenium.webdriver.common.by import By
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests
import keys
import os

def playMusic(musicName : str):

    print("play music : " + musicName)

    #Your google app API key
    #for that, you need to add to your google app, the library : 'youtube big data v3' and to put the key in keys
    api_key = keys.GOOGLE_KEY

    # The search request
    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={musicName}&key={api_key}'
    response = requests.get(url)

    # Parse the JSON data
    data = json.loads(response.text)
    print(data['items'][0]['id']['videoId'])

    # Make the link
    link = ('https://music.youtube.com/watch?v=' + data['items'][0]['id']['videoId'])

    # Define Brave path
    chromedriver = "C:/webdrivers/chromedriver.exe"
    option = webdriver.ChromeOptions()
    option.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    s = Service(chromedriver)
    driver = webdriver.Chrome(service=s, options=option)

    #Open the link and launch the music
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR, "form[jsaction='JIbuQc:ldDdv(b3VHJd)']").click()

    #pause to not quit the driver
    os.system('pause')