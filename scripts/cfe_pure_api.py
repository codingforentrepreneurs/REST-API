import json
import requests # http requests



BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"


def get_list(): #--> Lists all this out
    r = requests.get(BASE_URL + ENDPOINT)
    print(r.status_code)
    status_code = r.status_code
    if status_code != 200: # not found
        print('probably not good sign?')
    data = r.json()
    #print(type(json.dumps(data)))
    for obj in data:
        #print(obj['id'])
        if obj['id'] == 1: #--> User Interaction
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            #print(dir(r2))
            print(r2.json())
    return data



#print(get_list())

get_list()