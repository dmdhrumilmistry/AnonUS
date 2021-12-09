from requests import post

base_headers = {
    'Content-Type' : 'application/json',
}
url = "http://127.0.0.1:8000/new_link"
data = {
    'link':'https://duckduckgo.com/'
}
response = post(url=url, json=data).content.decode()

print(response)