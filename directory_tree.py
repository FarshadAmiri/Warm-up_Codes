import os

def print_tree(path, indent=""):
    if not os.path.exists(path):
        print("Path does not exist.")
        return
    if os.path.isfile(path):
        print(indent + os.path.basename(path))
        return

    print(indent + os.path.basename(path) + "\\")
    indent += "    "
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        print_tree(item_path, indent)

if __name__ == "__main__":
    directory = input("Enter the directory path: ").strip()

    # Remove quotes if user typed them
    if (directory.startswith('"') and directory.endswith('"')) or \
       (directory.startswith("'") and directory.endswith("'")):
        directory = directory[1:-1]

    print("\nDirectory tree:\n")
    print_tree(directory)
    input("\nPress Enter to exit...")
