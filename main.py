import requests
from bs4 import BeautifulSoup

KEYWORDS = {'Дизайн', 'Фото', 'Web', 'Python'}

response = requests.get('https://habr.com/ru/all/')
if not response.ok:
    raise RuntimeError("Сайт не доступен")

text = response.text

soup = BeautifulSoup(text, features='html.parser')
articles = (soup.find_all('article'))
interesting_articles = []

for article in articles:
    hubs = {h.text.strip() for h in  article.find_all('a', class_='hub-link')}
    if hubs & KEYWORDS:
        interesting_article = []
        
        a = article.find('a', class_='post__title_link')
        link = a.attrs.get('href')
        title = a.text
        
        span_time = article.find('span', class_='post__time')
        date = span_time.text

        interesting_article.append(date)
        interesting_article.append(title)
        interesting_article.append(link)

        interesting_articles.append(interesting_article)

print(interesting_articles)

# <a href="https://habr.com/ru/company/otus/blog/563860/" class="post__title_link">Создание самодостаточных исполняемых JAR</a>