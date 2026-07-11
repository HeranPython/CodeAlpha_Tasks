import requests
import re

response = requests.get("https://example.com")

title = re.search("<title>(.*?)</title>", response.text)

file = open("title.txt", "w")
file.write(title.group(1))
print(title.group(1))
file.close()
