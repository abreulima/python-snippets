import requests

url = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Flag_of_Arizona.svg/640px-Flag_of_Arizona.svg.png")
f = open("arizona.png", "wb")
f.write(url.content)
f.close()