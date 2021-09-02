import requests
from bs4 import BeautifulSoup
from pprint import pprint

# Вывести в консоль список подходящих статей в формате: <дата> - <заголовок> - <ссылка>.

KEYWORDS = ['SQL', 'веб-приложение', 'python', 'словари', 'программирование', 'фокус', 'системы', 'человек']


def habrScrap():
    response = requests.get('https://habr.com/ru/all/')
    if not response.ok:
        raise RuntimeError('страница не найдена')

    text = response.text

    soup = BeautifulSoup(text, features='html.parser')
    articles = soup.find_all('article')
    new_interesting_posts = []

    for article in articles:
        date = [d.text.strip() for d in article.find_all('span', class_='tm-article-snippet__datetime-published')]
        preview1 = [p.text.strip() for p in article.find_all('div', class_='article-formatted-body')]
        title = [t.text.strip() for t in article.find_all('h2', class_='tm-article-snippet__title')]
        a = article.find('a', class_='tm-article-snippet__title-link')
        true_link = f'https://habr.com' + a.attrs.get('href')
        # print(preview1)

        for keyword in KEYWORDS:
            if keyword.lower() in ''.join(preview1).lower():
                new_interesting_posts.append(f'{date} - {title} - {true_link}')
                # print(preview1)
                # print(keyword)
    return new_interesting_posts

if __name__ == '__main__':
    interesting_links = habrScrap()
    print('Такие ссылки найдены для вас сегодня:')
    pprint(interesting_links)

