import requests
import json
from pprint import pprint


# 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/78.0.3904.97 YaBrowser/19.12.0.358 Yowser/2.5 Safari/537.36'}
main_link = 'https://api.github.com'
user_name = input(f'введите имя пользователя: ', )
user_link = f'{main_link}/users/{user_name}/repos'

response = requests.get(user_link,headers=headers)
data = json.loads(response.text)
print(*(repo['name'] for repo in data), sep='\n')
# help(json)
with open('lesson1_api.json', 'w') as _:
    json.dump(data, _)


# 2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.

main_link = 'https://api.vk.com/method/friends.getOnline?'
token_id = input(f'введите access_token: ', )
parametres = 'user_id,online_mobile=True,list_id'

response = requests.get(f'{main_link}parametres={parametres}&access_token={token_id}&v=5.103')

if response.ok:
    data = json.loads(response.text)
    pprint(f'Список ID друзей онлайн: {data}')