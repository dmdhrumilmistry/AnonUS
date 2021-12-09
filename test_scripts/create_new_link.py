from requests import post

base_headers = {
    'Content-Type' : 'application/json',
}
url = "http://app-name.herokuapp.com/new_link"
data = {
    'link':'https://github.com/dmdhrumilmistry/AnonUS'
}
response = post(url=url, json=data).content.decode()

print(response)
