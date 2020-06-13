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
        return str(r.content)

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
        return str(r.content)


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
        return str(r.content) 

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
    r = requests.post(f'https://bunnycdn.com/api/pullzone/addHostname',data= json.dumps(values), headers=headers)
    print(r.status_code)
    if r.status_code == 200:
        return "Host added!!!"
    else:
        return str(r.content)  

def force_ssl(api, id, Hostname, ssl):
    values= {
    "PullZoneId": id,
    "Hostname": Hostname,
    "ForceSSL": ssl,
    }

    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'AccessKey':api,
    }
    r = requests.post(f'https://bunnycdn.com/api/pullzone/setForceSSL',data= json.dumps(values), headers=headers)
    print(r.status_code)
    if r.status_code == 200:
        return "Ssl forced!!!"
    else:
        return str(r.content)                        


def get_free_ssl(api, Hostname):
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'AccessKey':api,
    }
    r = requests.post(f'https://bunnycdn.com/api/pullzone/loadFreeCertificate?hostname={Hostname}',data= json.dumps(values), headers=headers)
    print(r.status_code)
    if r.status_code == 200:
        return "Ssl forced!!!"
    else:
        return str(r.content)                        


def billing_info(api):
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'AccessKey':api,
    }
    r = requests.post(f'https://bunnycdn.com/api/billing', headers=headers)
    print(r.status_code)
    if r.status_code == 200:
        return "Sucess" + str(r.content)
    else:
        return str(r.content) 


def add_newblocked_ip(api, pullzoneid, ip):
    values ={
    "PullZoneId": int(pullzoneid),
    "BlockedIp": ip,
     }
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'AccessKey':api,
    }
    r = requests.post(f'https://bunnycdn.com/api/pullzone/addBlockedIp', data = json.dumps(values), headers=headers)
    print(r.status_code)
    if r.status_code == 200:
        return "Sucess" + str(r.content)
    else:
        return str(r.content)   

def remove_blocked_ip(api, pullzoneid, ip):
    values ={
    "PullZoneId": int(pullzoneid),
    "BlockedIp": float(ip)
     }
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'AccessKey':api,
    }
    r = requests.post(f'https://bunnycdn.com/api/pullzone/removeBlockedIp', data = json.dumps(values), headers=headers)
    print(r.status_code)
    if r.status_code == 200:
        return "Sucess" + str(r.content)
    else:
        return str(r.content)                  





      