import requests
import json

cats = {5830: 4,
        2040: 3,
        2043: 5}


def get_json(params ,cat_id):
    url = f"https://lalafo.kg/api/search/v3/feed/search"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
        "Accept": "application/json, text/plain, */*",
        "device": "pc",
        "language": "ru_RU"
    }
    # params['category_id'] = cat_id
    response = requests.get(url, headers=headers, params=params)
    return response.json()


def save_json(data):
    """сохрание ответа в файл для наглядного просмотра"""
    with open('lalafo_data.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        print(f'Данные сохранены в lalafo_data.json')


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
    for i in data:
        title = i['title']
        description = i['description']
        price = i['price']
        city = i['city']
        cat_id = i['cat_id']
        image = i['image']
        phone = i['phone']
        imgs = {}
        # print(image)
        # print(i)
        r = requests.get(image) #['original_url']
        imgs['images'] = ("file.jpg", r.content, 'image/jpeg')
        try:
            nameseller = i['name_seller']
        except:
            nameseller = ''
        print(price)
        data = {
            'title': f'{title}', 'description': f'{description}', 'price': f'{price}', 'city': f'{city}', 'category': f'{cats.get(cat_id)}',
            'phone': f'{phone}', 'author': f'{nameseller}'
        }
        r = requests.post("http://127.0.0.1:8000/api/v1/aam/", data=data, files=imgs)
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
        save_json(data=result)
        save_data_db(cat_id, data=result)
    # print("G" * 50, result)
    # print(result)
    # print(len(result))
    # print(len(data_json['items']))