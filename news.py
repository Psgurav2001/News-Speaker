from email import message
from unicodedata import name
import requests
import json
from win32com.client import Dispatch
import inquirer


api = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=5a272e48b9614ec9b2ec9699cd90babd")


# data loading in news variable by using json module (Json will load in Python dict formate.)
data = api.text
news = json.loads(data)


title = []
news_data = {}

#  This function can be use for hear a news in WIndows SAPI voice 
def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)

#  Main Function
if __name__ == "__main__":
    for i in range(len(news["articles"])):
        headline = (news["articles"][i]["title"])
        title.append(headline)


    # this will show top todays headlines.
    news_title = [
        inquirer.List("news_title",
        message = "select which news do you want hear ?",
        choices=title,
        )
    ]



    chocieNews = inquirer.prompt(news_title)
    print(chocieNews["news_title"])


    # ind = title.index(chocieNews["news_title"])
    # disc = news["articles"][ind]["description"]

