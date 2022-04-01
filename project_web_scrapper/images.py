from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
import requests


search = input("Enter search term : ")
params = {"q": search}

r = requests.get("https://www.bing.com/images/search", params=params)
soup = BeautifulSoup(r.text, "html.parser")
links = soup.findAll("a", {"class": "itm"})

'''
f = open("temp_2.txt", "w+")
f2 = open("temp_2.html", "w+")
f.write(soup.prettify())
f2.write(soup.prettify())
'''

i = 1

for item in links:
	try:
		img_obj = requests.get(item.find("img").attrs["src2"])
		title = item.find("img").attrs["alt"]
		#print("status", img_obj.status_code)
		try:
			img = Image.open(BytesIO(img_obj.content))
			path = "scrapped_img/" + title + "." + img.format
			#print(path)
			img.save(path, img.format)
			print("img saved " + str(i))
		except:
			print("could not save img")
	except:
		print("request error")
	i += 1