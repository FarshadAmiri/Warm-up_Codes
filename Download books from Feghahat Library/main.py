from bs4 import BeautifulSoup
import re
import requests
from PIL import Image
import os

### Inputs:

# book_url = r'http://pdf.lib.eshia.ir/94033/1/1'    
# a, z = 1, 20   #first and last page to download.
# save_dir = r'C:\Users\Farshad\Desktop\New_book'
book_url = input("Enter the book url at the Feghahat Library (pdf.lib.eshia.ir/BookCode/VolumeNumber/Page) :  "))
a, z = input("Enter the range of pages you want to download (eg. 5-120)").split('-')
save_dir = input(r'Enter destination directory:\n(eg. C:\Users\PC_NAME\Desktop\New_book') ')

# --------------------------------------------------------------------
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
    open(f"{save_dir}\{number}.jpg", 'wb').write(img.content)

images_dict = dict()
for image in os.listdir(save_dir):
    images_dict[image] = Image.open(f"{save_dir}\{image}")
pdf_filename = f"{save_dir}\ book.pdf"
im1 = images_dict[os.listdir(save_dir)[0]]
im1.save(pdf_filename, "PDF" ,resolution=100.0, save_all=True, append_images=images_dict.values())