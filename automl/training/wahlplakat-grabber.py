#!/usr/bin/python3
import sys

print(sys.argv)

from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()
keyword = "{} Wahlplakat".format(sys.argv[1])
print("grabbing for {}".format(keyword))

arguments = {
"keywords": keyword,
"limit": 300,
"print_urls": True, 
"chromedriver": "/home/daniel/bin/chromedriver"
}

paths = response.download(arguments)
