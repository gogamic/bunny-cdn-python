import requests
import json


def create_pull_zone(api, name, original_url, type):
    values ={
        "Name": name,
        "Type": type,
        "OriginUrl": original_url,
    }
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'AccessKey':api,
    }
    r = requests.post('https://bunnycdn.com/api/pullzone', data=json.dumps(values), headers=headers)
    print(r.status_code)
    if r.status_code == 201:
        return "Pull Zone Created and here are the details" + r.content
    else:
        return r.content

def delete_pull_zone(api, id):
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'AccessKey':api,
    }
    r = requests.delete(f'https://bunnycdn.com/api/pullzone/{id}', headers=headers)
    print(r.status_code)
    if r.status_code == 204:
        return "Pull Zone Delted!!!"
    else:
        return r.content


def purge_cache(api, id):
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'AccessKey':api,
    }
    r = requests.post(f'https://bunnycdn.com/api/pullzone/{id}/purgeCache', headers=headers)
    print(r.status_code)
    if r.status_code == 200:
        return "Purged!!!"
    else:
        return r.content 

def add_host_name(api, id, Hostname):
    values= {
    "PullZoneId": id,
    "Hostname": Hostname,
    }

    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'AccessKey':api,
    }
    r = requests.post(f'https://bunnycdn.com/api/pullzone/{id}/purgeCache',data= json.dumps(values), headers=headers)
    print(r.status_code)
    if r.status_code == 200:
        return "Host added!!!"
    else:
        return r.content                


      