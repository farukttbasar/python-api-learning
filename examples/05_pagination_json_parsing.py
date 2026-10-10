import requests

base_url = 'https://rickandmortyapi.com/api/'
endpoint = 'location'

def main_request(base_url, endpoint, x):
    r = requests.get(base_url + endpoint + f'?page={x}')
    return r.json()

def get_pages(response):
    return response['info']['pages']

def parse_json(response): 
    locationlist = []
    
    for item in response['results']:
        location = {
            'name': item['name'],
            'type': item['type'],
            'dimension': item['dimension'],
            'residents': len(item['residents']),
        }
        locationlist.append(location)
    return locationlist

page_num = int(input("Enter the page number > "))
data = main_request(base_url, endpoint, page_num)

for x in range(1, get_pages(data)+1):
    print(x)

print(parse_json(data))




