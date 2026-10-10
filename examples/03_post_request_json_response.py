import requests

payload = {'username': 'faruque', 'password': 'apitesting'} # postlayacağın bilgiler --> json form kısmında yazar
r = requests.post('https://httpbin.org/post', data=payload)


print(r.text)
print(r.json()) # json responseyi python dicte çevirir

# spesifik bir kısmı almak için ;
r_json = r.json()
print(r_json['form'])