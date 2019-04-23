import csv
import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL'

r = requests.get(url)

html_content = r.text

soup = BeautifulSoup(html_content, 'lxml')

for i in range(3): 

    url = "https://finance.yahoo.com/quote/AAPL?p=AAPL{}".format(i)

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

   
with open("news.csv", "wb") as f:
    writer = csv.writer(f, delimiter=' ',
                            escapechar=' ', quoting=csv.QUOTE_NONE)
    writer.writerow(news)
##    writer.writerow(stories)



##print soup.find_all('h3')[0:10]
##print soup.find_all('p')[0:10]

