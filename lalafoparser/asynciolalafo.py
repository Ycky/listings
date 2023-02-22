import time

import httpx
import requests
import json
import asyncio
import aiohttp
from requests import Session


cats = {2040: 3, 5830: 4, 2043: 5}
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


async def parse_categories(cat_id):
    async with httpx.AsyncClient() as client:
        tasks = []
        # for cat_id, value in cats.items():
        tasks.append(asyncio.ensure_future(get_json(cat_id, client)))
        async_json = await asyncio.gather(*tasks)
        # save_json(async_json)
    return async_json


def save_json(data):
    with open('lalafo_data.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        print(f'Данные сохранены в lalafo_data.json')


def filter_json(json_data, category_id):
    # if json_data in category_id.keys():
    #     return category_id[json_data]
    domen_photo = 'https://img5.lalafo.com/i/posters/api'
    tasks = []
    # print(json_data)
    # print('---------------------' * 100)
    for d in json_data[0]['items']:
            title = d['title']
            description = d['description']
            price = d['price']
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


def post_json(data, client):
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


def main():
    tasks = []
    for cat_id in cats:
        json_data = asyncio.run(parse_categories(cat_id))
        tasks.extend(filter_json(json_data, category_id=cat_id))
        post_json(data=tasks, client=json_data)
        save_json(data=tasks)


if __name__ == '__main__':
    main()
