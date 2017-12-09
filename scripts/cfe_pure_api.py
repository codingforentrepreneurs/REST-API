import json
import requests # http requests



BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"


def get_list(id=None): #--> Lists all this out
    data = json.dumps({})
    if id is not None:
        data = json.dumps({"id": id})
    r = requests.get(BASE_URL + ENDPOINT, data=data)
    print(r.status_code)
    status_code = r.status_code
    if status_code != 200: # not found
        print('probably not good sign?')
    data = r.json()
    return data



def create_update():
    new_data = {
        'user': 1,
        "content": "Another more cool content"  
    }
    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        #print(r.json())
        return r.json()
    return r.text


print(get_list())

# print(create_update())


def do_obj_update():
    new_data = {
        "id": 3,
        "content": "awesomer"  
    }
    r = requests.put(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    # new_data = {
    #     'id': 1
    #     "content": "Another more cool content"  
    # }
    # r = requests.put(BASE_URL + ENDPOINT, data=new_data)
    #print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        #print(r.json())
        return r.json()
    return r.text


def do_obj_delete():
    new_data = {
        "id": 3
    }
    r = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    # new_data = {
    #     'id': 1
    #     "content": "Another more cool content"  
    # }
    # r = requests.put(BASE_URL + ENDPOINT, data=new_data)
    #print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        #print(r.json())
        return r.json()
    return r.text



# print(do_obj_update())



