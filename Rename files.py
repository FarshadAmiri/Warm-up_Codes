# A program to change audio files names to their audio title tags.

import os
import re
import eyed3

root = r'C:\Users\Farshad\Desktop\tkh'

files = os.listdir(path= root)
files.remove('rename.py')
files.remove('venv')

for file in files:
    title = eyed3.load(file).tag.title
    try:
        name = 'جلسه ' + re.search(r'.*.*: (.*) \|',title).group(1).strip()
    except:
        name = title
    os.rename(src=file, dst= os.path.join(root, f"{name}.mp3"))


