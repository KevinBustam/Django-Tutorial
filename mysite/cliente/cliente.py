import requests

API_ENDPOINT = "http://192.168.1.70:8000/dpd/views/poke/"

data = '{"channel_name":"live_arduino_sensor","label":"arduino_sensor","value":{"valor":1235}}'

r = requests.post(url = API_ENDPOINT, data = data)


pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)
