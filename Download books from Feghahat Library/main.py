from bs4 import BeautifulSoup
import re
import requests
from PIL import Image
import os
import time

# book_url = r'http://pdf.lib.eshia.ir/97136/1/19'
# a, z = 1, 10   #first and last page to download.
# save_dir = r'C:\Users\Farshad\Desktop\New_book10'
book_url = input("Enter the book url at Feghahat Library (pdf.lib.eshia.ir/BookCode/VolumeNumber/Page):"'\n')
a, z = map(int, input("Please enter the range of pages you want to download (eg. 5-120)"'\n').split('-'))
save_dir = input(r"Please enter the directory in which downloaded book will be placed:"'\n'r"(eg. C:\Users\Farshad\Desktop\New_book)"'\n')
print(f"Please wait, It's going to take {int((z-a)/180)+2} minutes at the most" )
book_url = re.search(r'(.+/).*',book_url).group(1)
pages_dirs = [f"{book_url}{x}" for x in range (a,z+1)]

images_links = []
for url in pages_dirs:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    image = soup.find('img', attrs={'class': 'libimages'})
    images_links.append(f"http://pdf.lib.eshia.ir{image['src']}")

if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
for link in images_links:
    img = requests.get(link, allow_redirects=True)
    number = re.search(r'.*/(\d*)',link).group(1)
    f = open(f"{save_dir}\{number}.jpg", 'wb')
    f.write(img.content)
    print(f'Page {number} is downloaded')
    f.close()

images_dict = dict()
for image in os.listdir(save_dir):
    images_dict[image] = Image.open(f"{save_dir}\{image}")

pdf_filename = fr"{save_dir}\book.pdf"
im1 = images_dict[os.listdir(save_dir)[0]]
im1.save(pdf_filename, "PDF" ,resolution=100.0, save_all=True, append_images= list(images_dict.values())[1:])

for i in images_dict.values():
    i.close()


for image in os.listdir(save_dir):
    if image != 'book.pdf':
        os.remove(f"{save_dir}\{image}")

print()
print()
print('*** Your PDF is ready ***')
time.sleep(3)