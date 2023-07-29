import os
import re

def subfiles_list(path):
    subfiles = []
    for name in os.listdir(path):
        subfiles.append(name)
    return subfiles 


subfolder_dir = r"C:\Users\Farshad\Desktop\Coursera – Convolutional Neural Networks 2021-4"
subfiles = subfiles_list(subfolder_dir)

regex_pattern = '^.*(?<!\.en)\.srt$'

for file in subfiles:
    if bool(re.match(pattern=regex_pattern, string=file)):
        os.remove(f'{subfolder_dir}\{file}')
        
       