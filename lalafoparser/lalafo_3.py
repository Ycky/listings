import requests
import json



# cats = {2040: 3, 5830: 4, 2043: 5}
cats = 2040, 5830, 2040

def get_json(params ,cat_id):
    url = f"https://lalafo.kg/api/search/v3/feed/search{cat_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
        "Accept": "application/json, text/plain, */*",
        "device": "pc",
        "language": "ru_RU"
    }
    params['category_id'] = cat_id
    response = requests.get(url, headers=headers, params=params)
    return response.json()


def save_filtered_json(data):
    """сохрание ответа в файл для наглядного просмотра"""
    with open('lalafo_filtered_data.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        print(f'Данные сохранены в lalafo_filtered_data.json')


def get_data_form_json(json_file, category_id):
    domen_photo = 'https://img5.lalafo.com/i/posters/api'
    result = []
    for d in json_file[0]['items']:
        title = d['title']
        description = d['description']
        price = d['price']
        post_id = d['id']
        phone = d['mobile']
        try:
            image = domen_photo + d['image']
        except TypeError:
            image = 'not photo'
        city = d['city']
        try:
            nameseller = d['user']['username']
        except:
            nameseller = ''

        result.append({
            'title': title,
            'description': description,
            'price': price,
            'image': image,
            'city': city,
            'cat_id': category_id,
            'phone': phone,
            'name_seller': nameseller,
            'post_id': post_id
        })
    return result


def save_data_db(cat_id, data):
    # print('M' * 50, data)
    for i in data:
        title = i['title']
        description = i['description']
        price = i['price']
        city = i['city']
        cat_id = i['cat_id']
        image = i['image']
        phone = i['phone']
        """images = i['images']
        for img in images:
            o = requests.get(img['original_url'])
            img['images'] = ("file.jpg", o.content, 'image/jpeg')
        phone = ['mobile']"""
        imgs = {}
        for img in image:
            r = requests.get(img['original_url'])
            imgs['images'] = ("file.jpg", r.content, 'image/jpeg')
        try:
            nameseller = i['user']['username']
        except:
            nameseller = ''

        data = {
            'title': title, 'description': description, 'price': price, 'city': city, 'category': cats.get(cat_id),
            'phone': phone, 'name_seller': nameseller, 'image': image
        }
        r = requests.post("http://127.0.0.1:8000/api/v1/aam/", json=data)
        print(r.text)


if __name__ == '__main__':
    result = []
    v = []
    params = {
        'expend': 'url',
        'per-page': 5,
        'category_id': cats,
    }

    for cat_id in cats:
        data_json = get_json(params, cat_id=cat_id)
        result.extend(get_data_form_json(data_json, category_id=cat_id))
        save_filtered_json(data=result)
        save_data_db(cat_id, data=v) #data=v если не нужно отправлять запрос
    # print("G" * 50, result)
    print(result)
    print(len(result))
    print(len(data_json['items']))


'''
это старое версия вдруг понадыбиться
import requests
import json
import pandas as pd

cats = (2040, 5830, 2043)

def save_data_db(cat_id, data):
    for i in data:
        title = i['title']
        description = i['description']
        price = i['price']
        post_id = i['id']
        phone = i['mobile']
        image = i['image']
        city = i['city']
        cat_id = i['category']
        imgs = {}
        for img in image:
            r = requests.get(img['original_url'])
            imgs['images'] = ("file.jpg",r.content, 'image/jpeg')
        try:
            nameseller = i['user']['username']
        except:
            nameseller = ''

        v = {'user': 1, 'category': cats.get(cat_id),
             'title': title, 'description': description,
             'price': price, 'city': city,
             'phone': phone, 'name_seller': nameseller,
             'post_id': post_id}
        print(imgs)
        requests.post("http://127.0.0.1:8000/api/v1/aam/", data=v, files=imgs)


def get_json(params ,cat_id):
    url = f"https://lalafo.kg/api/search/v3/feed/search?expand=url&per-page=17&category_id={cat_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
        "Accept": "application/json, text/plain, */*",
        "device": "pc",
        "language": "ru_RU"
    }
    params['category_id'] = cat_id
    response = requests.get(url, headers=headers)
    return response.json()

def save_json(data):
    """сохрание ответа в файл для наглядного просмотра"""
    with open('lalafo_data.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        print(f'Данные сохранены в file.json')



def get_data_form_json(json_file, category_id):
    domen_photo = 'https://img5.lalafo.com/i/posters/api'
    domen = 'https://lalafo.kg'
    result = []
    for d in json_file['items']:
        title = d['title']
        description = d['description']
        price = d['price']
        post_id = d['id']
        phone = d['mobile']
        try:
            image = domen_photo + d['image']
        except TypeError:
            image = 'not photo'
        city = d['city']
        try:
            nameseller = d['user']['username']
        except:
            nameseller = ''

        result.append({
            'title': title,
            'description': description,
            'price': price,
            'image': image,
            'city': city,
            'cat_id': category_id,
            'phone': phone,
            'name_seller': nameseller,
            'post_id': post_id
        })
    return result




def save_excel(data):
    df = pd.DataFrame(data)
    writer = pd.ExcelWriter('lalafo_result.xlsx')
    df.to_excel(writer, 'data')
    writer.save()
    print('Все сохранено')




if __name__ == '__main__':
    result = []
    params = {
        'city_id': 103184,
        'cat_id': 'cat_id',
        'category_id': 0,
        'price[form]': 1000000,
        'price[to]': 8000000,
        'per-page': 500,
        'page': 1
    }

    for cat_id in cats:
        data_json = get_json(params, cat_id=cat_id)
        result.extend(get_data_form_json(data_json, category_id=cat_id))
        save_excel(result)
    print(result)
    print(len(result))
    print(len(data_json['items']))
'''









# its last version of lalafo_3.py
# # import requests
# # import json
# #
# # url = f"https://lalafo.kg/api/search/v3/feed/search"
# #
# # headers = {
# #     "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
# #     "Accept": "application/json, text/plain, */*",
# #     "device": "pc",
# #     "language": "ru_RU"
# # }
# #
# # params = {
# #     'expand': 'url',
# #     'category_id': 5830,
# #     'per_page': 5
# # }
# #
# # def get_json(params):
# #     response = requests.get(url, headers=headers, params=params)
# #     return response.json()
# #
# #
# # def save_json(data):
# #     """сохрание ответа в файл для наглядного просмотра"""
# #     with open('lalafo_data_3.json', 'w', encoding='UTF-8') as file:
# #         json.dump(data, file, indent=2, ensure_ascii=False)
# #         print(f'Данные сохранены в lalafo_data_3.json')
# #
# #
# # def save_data_to_db(params, data):
# #     data = []
# #     for i in data:
# #         title = i['title']
# #         description = i['description']
# #         price = i['price']
# #         city = i['city']
# #         cat_id = i[5830]
# #         images = i['images']
# #         for img in images:
# #             o = requests.get(img['original_url'])
# #             img['images'] = ("file.jpg", o.content, 'image/jpeg')
# #         phone = ['mobile']
# #         try:
# #             nameseller = i['user']['username']
# #         except:
# #             nameseller =''
# #
# #         data.append({
# #             'title': title, 'description': description, 'price': price, 'city': city, 'category': 5830,
# #             'phone': phone, 'name_seller': nameseller, 'image': images
# #         })
# #         o = requests.post("http://127.0.0.1:8000/api/v1/aam/", json=data, files=images)
# #         return data
# #
# #
# # if __name__=='__main__':
# #     data = []
# #     for cat_id in range(5830):
# #         data_json = get_json(params)
# #         data.extend(save_data_to_db(data_json, 5830))
# #         save_json(data=data)
# #     print(data)
# #
# # json_data = get_json(params)
# # save_json(json_data)
# #
# # import requests
# # import json
# #
# #
# # def get_json(params):
# #     url = f"https://lalafo.kg/api/search/v3/feed/search"
# #     headers = {
# #         "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
# #         "Accept": "application/json, text/plain, */*",
# #         "device": "pc",
# #         "language": "ru_RU"
# #     }
# #     response = requests.get(url, headers=headers, params=params)
# #     return response.json()
# #
# #
# # def save_json(data):
# #     """сохрание ответа в файл для наглядного просмотра"""
# #     with open('lalafo_data.json', 'w', encoding='UTF-8') as file:
# #         json.dump(data, file, indent=2, ensure_ascii=False)
# #         print(f'Данные сохранены в lalafo_data.json')
# #
# #
# # def get_data_from_json(json_file):
# #     domen_photo = 'https://img5.lalafo.com/i/posters/api'
# #     domen = 'https://lalafo.kg'
# #     # проходимся по данным и собираем в список то, что нам нужно
# #     result = []
# #     for d in json_file['items']:
# #         title = d['title']
# #         phone = d['mobile']
# #         description = d['description'].replace('\n', ' ')
# #         price = d['price']
# #         try:
# #             image = domen_photo + d['image']
# #         except TypeError:
# #             image = 'без изображения'
# #         city = d['city']
# #         try:
# #             nameseller = d['user']['username']
# #         except:
# #             nameseller = ''
# #
# #         result.append({
# #             'title': title,
# #             'description': description,
# #             'city': city,
# #             'price': price,
# #             'image': image,
# #             'name_seller': nameseller,
# #             'phone': phone,
# #         })
# #     return result
# #
# #
# # if __name__ == '__main__':
# #     result = []
# #     params = {
# #         'expend': 'url',
# #         'per-page': 5,
# #         'category_id': 5830,
# #     }
# #     for cdat in params:
# #         data_json = get_json(params)
# #         save_json(data=result)
# #         result.extend(get_data_from_json(data_json))
# #
# #     print(len(data_json['items']))
#
#
# import requests
# import json
# import time
# import pandas as pd
# import datetime
# import asyncio
# import aiohttp
#
#
# cats = {2040: 3, 5830: 4, 2043: 5}
#
#
# def get_json(params ,cat_id):
#     url = f"https://lalafo.kg/api/search/v3/feed/search?expand=url&per-page=17&category_id={cat_id}"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
#         "Accept": "application/json, text/plain, */*",
#         "device": "pc",
#         "language": "ru_RU"
#     }
#     params['category_id'] = cat_id
#     response = requests.get(url, headers=headers, params=params)
#     return response.json()
#
#
# def save_json(data):
#     """сохрание ответа в файл для наглядного просмотра"""
#     with open('lalafo_data.json', 'w', encoding='UTF-8') as file:
#         json.dump(data, file, indent=2, ensure_ascii=False)
#         print(f'Данные сохранены в lalafo_data.json')
#
# def save_filtered_json(data):
#     """сохрание ответа в файл для наглядного просмотра"""
#     with open('lalafo_filtered_data.json', 'w', encoding='UTF-8') as file:
#         json.dump(data, file, indent=2, ensure_ascii=False)
#         print(f'Данные сохранены в lalafo_filtered_data.json')
#
#
# def get_data_form_json(json_file, category_id):
#     domen_photo = 'https://img5.lalafo.com/i/posters/api'
#     # domen = 'https://lalafo.kg'
#     result = []
#     for d in json_file['items']:
#         title = d['title']
#         description = d['description']
#         price = d['price']
#         post_id = d['id']
#         phone = d['mobile']
#         try:
#             image = domen_photo + d['image']
#         except TypeError:
#             image = 'not photo'
#         city = d['city']
#         try:
#             nameseller = d['user']['username']
#         except:
#             nameseller = ''
#
#         result.append({
#             'title': title,
#             'description': description,
#             'price': price,
#             'image': image,
#             'city': city,
#             'cat_id': category_id,
#             'phone': phone,
#             'name_seller': nameseller,
#             'post_id': post_id
#         })
#     return result
#
#
# def save_data_db(cat_id, data):
#     # print('M' * 50, data)
#     for i in data:
#         title = i['title']
#         description = i['description']
#         price = i['price']
#         city = i['city']
#         cat_id = i['cat_id']
#         image = i['image']
#         phone = i['phone']
#         imgs = {}
#         for img in image:
#             r = requests.get(img['original_url'])
#             imgs['images'] = ("file.jpg", r.content, 'image/jpeg')
#         try:
#             nameseller = i['user']['username']
#         except:
#             nameseller = ''
#
#         data = {
#             'title': title, 'description': description, 'price': price, 'city': city, 'category': cats.get(cat_id),
#             'phone': phone, 'name_seller': nameseller,
#         }
#         r = requests.post("http://127.0.0.1:8000/api/v1/aam/", json=data)
#         print(r.text)
#
# def save_excel(data, cat_id):
#     # df = pd.DataFrame(data)
#     # writer = pd.ExcelWriter('lalafo_result.xlsx')
#     # df.to_excel(writer, 'data')
#     # writer.save()
#     print('Все сохранено')
#
#
# if __name__ == '__main__':
#     result = []
#     v = []
#     params = {
#         'city_id': 103184,
#         'cat_id': 'cat_id',
#         'category_id': 0,
#         'price[form]': 1000000,
#         'price[to]': 8000000,
#         'per-page': 500,
#         'page': 1
#     }
#
#     for cat_id in cats:
#         data_json = get_json(params, cat_id=cat_id)
#         result.extend(get_data_form_json(data_json, category_id=cat_id))
#         save_filtered_json(data=result)
#         save_data_db(cat_id, data=result)
#     # print("G" * 50, result)
#     print(result)
#     print(len(result))
#     print(len(data_json['items']))





''' asyncio parser
import time

import httpx
import requests
import json
import asyncio
import aiohttp
from requests import Session


cats = {5830: 4, 2040: 3, 2043: 5}
start_time = time.time()


async def get_json(cat_id, client):
    url = f"https://lalafo.kg/api/search/v3/feed/search?expand=url&per-page=1&category_id={cat_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
        "Accept": "application/json, text/plain, */*",
        "device": "pc",
        "language": "ru_RU"
    }
    response = await client.get(url, headers=headers)
    return response.json()


async def parse_categories():
    async with httpx.AsyncClient() as client:
        tasks = []
        for cat_id, value in cats.items():
            tasks.append(asyncio.ensure_future(get_json(cat_id, client)))
        async_json = await asyncio.gather(*tasks)
        save_json(async_json)
        # tasks.extend(filter_json(async_json, category_id=cat_id))
        # post_json(cat_id, data=tasks, client=client)
    return async_json


def save_json(data):
    """сохрание ответа в файл для наглядного просмотра"""
    with open('lalafo_data.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        print(f'Данные сохранены в lalafo_data.json')


def filter_json(json_data, category_id):
    domen_photo = 'https://img5.lalafo.com/i/posters/api'
    tasks = []
    for key, value in json_data.items():
        title = value['title']
        description = value['description']
        price = value['price']
        phone = value['mobile']
        try:
            image = domen_photo + value['image']
        except TypeError:
            image = 'not photo'
        city = value['city']
        try:
            nameseller = value['nameseller']
        except:
            nameseller = ''

        tasks.append({
            'title': title,
            'description': description,
            'price': price,
            'image': image,
            'city': city,
            'cat_id': category_id,
            'phone': phone,
            'name_seller': nameseller,
        })
    return tasks


def post_json(cat_id, data, client):
    for i in data:
        title = i['title']
        description = i['description']
        price = i['price']
        city = i['city']
        cat_id = i['cat_id']
        image = i['image']
        phone = i['phone']
        imgs = {}
        r = client.get(image)
        imgs['images'] = ("file.jpg", r.content, 'image/jpeg')
        try:
            nameseller = i['name_seller']
        except:
            nameseller = ''

        data = {
            'title': f'{title}', 'description': f'{description}', 'price': f'{price}', 'city': f'{city}', 'category': f'{cats.get(cat_id)}',
            'phone': f'{phone}', 'author': f'{nameseller}'
        }
        r = client.post("http://127.0.0.1:8000/api/v1/aam/", data=data, files=imgs)
        print(r.text)


if __name__ == '__main__':
    json_data = asyncio.run(parse_categories())
    filter_json(json_data, category_id=cats)
    print('t' * 50, type(json_data))
'''