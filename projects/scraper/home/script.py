from bs4 import BeautifulSoup
import requests
from .models import News


def get_imdb_news():
    # url = "https://www.imdb.com/news/movie"
    url = "https://www.w3schools.com/js/default.asp"
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url=url, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(response.text)

    articles = []
    news_items = soup.find_all('div', class_ = 'ipc-list-card--border-line')
    for item in news_items:
        title_elem = item.find('a', class_ = 'ipc-link')
        description = item.find('div', class_ = 'ipc-html-content-inner-div')
        image = item.find('img', class_ = 'ipc-image')

        title = title_elem.text.strip() if title_elem else 'No Title'
        description = description.text.strip() if description else 'No Description'
        image = image['src']
        external_link = title_elem['href']

        news = {
            "title": title,
            "description": description,
            "image": image,
            "external_link": external_link,
        }
        News.objects.create(**news)
        articles.append(news)

