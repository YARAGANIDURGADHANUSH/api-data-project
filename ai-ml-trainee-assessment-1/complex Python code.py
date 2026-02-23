import os
import shutil

# Folder you want to organize
TARGET_FOLDER = r"C:\Users\Sree\Downloads"



FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Archives": [".zip", ".rar"]
}

def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)

def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category
    return "Others"

def organize_files():
    if not os.path.exists(TARGET_FOLDER):
        print(f"Folder '{TARGET_FOLDER}' does not exist.")
        return

    for file_name in os.listdir(TARGET_FOLDER):
        file_path = os.path.join(TARGET_FOLDER, file_name)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file_name)
            category = get_category(ext.lower())

            category_path = os.path.join(TARGET_FOLDER, category)
            create_folder(category_path)

            shutil.move(file_path, category_path)

    print("Files organized successfully!")

if __name__ == "__main__":
    organize_files()