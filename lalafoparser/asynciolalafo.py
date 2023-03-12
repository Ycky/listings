import time
import httpx
import json
import asyncio
import aiohttp


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


# async def parse_categories(cat_id):
#     async with httpx.AsyncClient() as client:
#         tasks = []
#         tasks.append(asyncio.ensure_future(get_json(cat_id, client)))
#         async_json = await asyncio.gather(*tasks)
#         # post = await post_json(data=tasks, client=client)
#     return async_json


def save_json(data):
    with open('lalafo_data.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        print(f'Данные сохранены в lalafo_data.json')


def filter_json(json_data, category_id):
    domen_photo = 'https://img5.lalafo.com/i/posters/api'
    tasks = []
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


async def post_json(client, data):
    print('d' * 70, data)
    for i in data:
            print('i' * 70, i)
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
            r = await client.post("http://127.0.0.1:8000/api/v1/aam/", data=data, files=imgs)
            return r.json()


async def main():
    async with httpx.AsyncClient() as client:
        tasks = []
        for cat_id in cats:
            pass
            # tasks.append(asyncio.ensure_future(post_json(client, data=)))

        client_post = await asyncio.gather(*tasks)
        for r in client_post:
            print(r)

if __name__ == '__main__':
    asyncio.run(main())
