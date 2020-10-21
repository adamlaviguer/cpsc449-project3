import requests

r = requests.get('http://127.0.0.1:5100/')

for key in r.json():
    print('{} {}'.format(key, key))

# print(r.text, '\n')
