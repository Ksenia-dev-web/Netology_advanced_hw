import time
import datetime
import requests
from bs4 import BeautifulSoup
from pprint import pprint


def logger_decor(path):
    def decorator(function):
        def new_function(*args, **kwargs):
            answer = function(*args, **kwargs)
            with open(path, 'w', encoding='UTF-8') as f:
                f.write(f'{function.__name__}, {datetime.datetime.now()}, {args}, {kwargs}, {answer}, {path} \n')
            return answer
        return new_function
    return decorator


@logger_decor('log_info_blah.txt')
def blah_blah(x, y):
    answer = x + y
    return answer


KEYWORDS = ['SQL', 'веб-приложение', 'python', 'словари', 'программирование', 'фокус', 'системы', 'человек']


@logger_decor('log_info.txt')
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


def main():
    blah_blah(8, 6)
    blah_blah(10, 8)
    habrScrap()


if __name__ == '__main__':
    main()


# Оксана, здравствуйте!
# Спасибо за выполненную работу!
#
# Можно использовать как абсолютный так и относительный путь.
#
# У Вас отлично получилось: создать декоратор и применить его.
# Обратите внимание, что в new_function не определен return из-за чего теряется результат работы декорируемой функции.
#
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# @logger_decor('log_info.txt')
# def summator(x, y):
#    return x + y
#
# three = summator(1, 2)
# five = summator(2, 3)
#
# result = summator(three, five)
#
# print('result: ', result)
# print('result type: ', type(result))
# В result должно записаться 8 типа int
#
# Вы молодец, но работа требует доработки.
# Давайте внесем правки!