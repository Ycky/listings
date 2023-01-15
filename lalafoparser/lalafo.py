import requests
import json
import time
import pandas as pd
import datetime
import asyncio
import aiohttp


cats = {2040: 3, 5830: 4, 2043: 5}


def get_json(params ,cat_id):
    url = f"https://lalafo.kg/api/search/v3/feed/search?expand=url&per-page=17&category_id={cat_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
        "Accept": "application/json, text/plain, */*",
        "device": "pc",
        "language": "ru_RU"
    }
    params['category_id'] = cat_id
    response = requests.get(url, headers=headers, params=params)
    return response.json()


def save_json(data):
    """сохрание ответа в файл для наглядного просмотра"""
    with open('lalafo_data.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        print(f'Данные сохранены в lalafo_data.json')

def save_filtered_json(data):
    """сохрание ответа в файл для наглядного просмотра"""
    with open('lalafo_filtered_data.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        print(f'Данные сохранены в lalafo_filtered_data.json')


def get_data_form_json(json_file, category_id):
    domen_photo = 'https://img5.lalafo.com/i/posters/api'
    # domen = 'https://lalafo.kg'
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
        # imgs = {}
        # for img in image:
        #     r = requests.get(img['original_url'])
        #     imgs['images'] = ("file.jpg", r.content, 'image/jpeg')
        try:
            nameseller = i['user']['username']
        except:
            nameseller = ''

        data = {
            'title': title, 'description': description, 'price': price, 'city': city, 'category': cats.get(cat_id),
            'phone': phone, 'name_seller': nameseller,
        }
        r = requests.post("http://127.0.0.1:8000/api/v1/aam/", json=data)
        print(r.text)

def save_excel(data, cat_id):
    # df = pd.DataFrame(data)
    # writer = pd.ExcelWriter('lalafo_result.xlsx')
    # df.to_excel(writer, 'data')
    # writer.save()
    print('Все сохранено')


if __name__ == '__main__':
    result = []
    v = []
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
        save_filtered_json(data=result)
        save_data_db(cat_id, data=result)
    # print("G" * 50, result)
    print(result)
    print(len(result))
    print(len(data_json['items']))


