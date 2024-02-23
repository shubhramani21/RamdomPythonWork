import datetime
import time
from plyer import notification
import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=d7a5f27b31c044039bf6ca75919aed10')



try:
    respond=requests.get(url)
except:
    print("not able to fetch the api")

if(respond!=None):
    data=respond.json()
    
    i = 0
    while i < 6:
        article = data['articles'][i]
        date_time = datetime.date.today()
        formatted_date = date_time.strftime("%d-%m-%Y")
        title = "{formatted_date}\nToday's News".format(formatted_date=formatted_date)
        message = "Source: {author}\n{title}".format(author=article['author'], title=article['title'])
        notification.notify(
            title=title,
            message=message,
            app_icon="new1_.ico",
            timeout=5
        )
        time.sleep(10)
        i += 1