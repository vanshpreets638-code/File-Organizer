import os
import shutil

# Change this path to the folder you want to organize
path = "C:/Users/vansh/Downloads"

files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)

    if extension in [".jpg", ".png", ".jpeg"]:
        folder = "Images"
    elif extension in [".pdf"]:
        folder = "PDFs"
    elif extension in [".mp4", ".mkv"]:
        folder = "Videos"
    elif extension in [".docx", ".txt"]:
        folder = "Documents"
    elif extension in [".zip", ".rar"]:
        folder = "Zip"
    else:
        folder = "Others"

    folder_path = os.path.join(path, folder)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    shutil.move(os.path.join(path, file), os.path.join(folder_path, file))

print("Files organized successfully!")