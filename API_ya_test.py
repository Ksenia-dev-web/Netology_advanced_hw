### Задача №2 Автотест API Яндекса
# Проверим правильность работы Яндекс.Диск REST API.
# Написать тесты, проверяющий создание папки на Диске.
# Используя библиотеку requests напишите unit-test на верный ответ
# и возможные отрицательные тесты на ответы с ошибкой
#
# Пример положительных тестов:
# * Код ответа соответствует 200.
# * Результат создания папки - папка появилась в списке файлов.

import requests
from yandex_auth_info import yandex_token


def folder_creation(token):
    HEADERS = {'Authorization': token}
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    params = {'path': 'mmmnew_folder'}
    response = requests.put(url=url, params=params, headers=HEADERS)
    return response.status_code


if __name__== '__main__':
    print(folder_creation(yandex_token))
