import requests

payload = {'page': 2, 'count': 25} # APIye iki bilgi gönderiyorsun, 2. sayfa 25 bilgi/sonuç --> istek attığınde elde etmek istediğin bilgiye göre yazarsın.
r = requests.get('https://httpbin.org/get', params=payload)

print(r.url)

