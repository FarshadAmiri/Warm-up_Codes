import os
import re

def copy_matching_files(source_dir, destination_dir, regex_pattern):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if re.match(regex_pattern, file):
                new_file_path = os.path.join(destination_dir, file)
                with open(file_path, 'rb') as src_file, open(new_file_path, 'wb') as dest_file:
                    dest_file.write(src_file.read())

# Example usage
source_directory = r"C:\Users\user2\Desktop\Sat-OD\S2SHIPS"
destination_directory = r"C:\Users\user2\Desktop\images2"
regex_pattern = ".*_rgb.png"

copy_matching_files(source_directory, destination_directory, regex_pattern)