import requests
import bs4
from pprint import pprint

if __name__ == '__main__':
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    url_base = 'https://habr.com/ru/all'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    for page in range(1,10):
        response = requests.get(url_base + '/page'+str(page), headers=headers).text

        bs = bs4.BeautifulSoup(response, 'html.parser')
        articles = bs.findAll('article', class_='tm-articles-list__item')
        for article in articles:
            time_tag = article.find('span', class_='tm-article-snippet__datetime-published')
            date = time_tag.find('time').attrs.get('title')

            h2_tag = article.find('h2', class_='tm-article-snippet__title tm-article-snippet__title_h2')
            url = 'https://habr.com' + h2_tag.find('a').attrs.get('href')
            name = h2_tag.find('span').text

            res = article.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
            # print(res)
            if res != None:
                for keyword in KEYWORDS:
                    if keyword in res.text.lower():
                        print('Статья:', name)
                        print('url:', url)
                        print('дата', date)
                        print()
                        break
