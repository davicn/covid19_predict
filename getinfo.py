import requests

r = requests.get('https://covid19-brazil-api.now.sh/api/report/v1')
print(r.json())