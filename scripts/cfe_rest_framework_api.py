import json
import requests
import os


ENDPOINT = "http://127.0.0.1:8000/api/status/"

image_path = os.path.join(os.getcwd(), "logo.jpg")


def do_img(method='get', data={}, is_json=True, img_path=None):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    if img_path is not None:
        with open(image_path, 'rb') as image:
            file_data = {
                'image': image
            }
            r = requests.request(method, ENDPOINT, data=data, files=file_data, headers=headers)
    else:
        r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r



do_img(
    method='put', 
    data={'id': 23, 'user': 1, "content": "Some new content"}, 
    is_json=False, 
    img_path=image_path
    )





def do(method='get', data={}, is_json=True):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r



# do(data={'id': 500})

# do(method='delete', data={'id': 13})

# do(method='put', data={'id': 13, "content": "some cool new content", 'user': 1})

# do(method='post', data={"content": "some cool new content", 'user': 1})

# create
# retrieve / list
# update
# delete
