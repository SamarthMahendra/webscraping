import requests

url = "http://books.toscrape.com"
response = requests.get(url)

if response.ok:
    print("Here's the response")
    print(response.text[:500])
else:
    print("Couldn't fetch!")