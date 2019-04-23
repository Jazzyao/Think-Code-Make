import csv
import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=aapl&newwindow=1&source=lnms&tbm=nws&sa=X&ved=0ahUKEwjzxLOovOXhAhVEJt8KHS9EAwYQ_AUIDygC&biw=1440&bih=700'

r = requests.get(url)

html_content = r.text

soup = BeautifulSoup(html_content, 'lxml')

for i in range(3): 

    url = "https://www.google.com/search?q=aapl&newwindow=1&source=lnms&tbm=nws&sa=X&ved=0ahUKEwjzxLOovOXhAhVEJt8KHS9EAwYQ_AUIDygC&biw=1440&bih=700{}".format(i)

    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'})
 
    soup = BeautifulSoup(r.text, 'lxml')

news = []
##stories = []

for sub_heading in soup.find_all('h3'):
	new = sub_heading.text.encode('utf-8')
	news.append(new)
	print news

##for sub_heading in soup.find_all('p'):
## 	story = sub_heading.text.encode('utf-8')
## 	stories.append(story)
## 	print stories

   
with open("googlenews.csv", "wb") as f:
    writer = csv.writer(f, delimiter=' ',
                            escapechar=' ', quoting=csv.QUOTE_NONE)
    writer.writerow(news)
##    writer.writerow(stories)



##print soup.find_all('p')[0:10]

