import os

def copy_files(source_dir, destination_dir, file_extension):
    if not os.path.exists(destination_dir):
        os.mkdir(destination_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(file_extension):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_dir, file)
                
                with open(source_path, 'rb') as source_file:
                    with open(destination_path, 'wb') as destination_file:
                        destination_file.write(source_file.read())

# Replace 'source_dir' with the path to the directory you want to search in
source_dir = r"C:\Users\user2\Desktop\Sat-OD\S2SHIPS"
destination_dir = r"C:\Users\user2\Desktop\imagesss"
file_extension = "_rgb.png"

copy_files(source_dir, destination_dir, file_extension)