#This is a program to download images from the internet.

import requests

url = input('Enter the image url\n')
r = requests.get(url)
name = input("Enter the filename with extention\n")
with open('F:/CodeDownloads/{}'.format(name), 'wb') as F1:
    F1.write(r.content)

if F1.closed == True:
    print("Image saved\n")

#The image will be saved in Local Disk F -> CodeDownloads folder.

