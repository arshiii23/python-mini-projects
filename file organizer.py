import os
import shutil

folder_to_organize = input("Enter folder path: ")

if not os.path.exists(folder_to_organize):
    print("Folder does not exist")
    exit()

file_types = {
    "Images": [".png", ".jpg", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3"]
}

for filename in os.listdir(folder_to_organize):

    file_path = os.path.join(folder_to_organize, filename)

    if os.path.isfile(file_path):

        extension = os.path.splitext(filename)[1].lower()

        moved = False

        for folder_name, extensions in file_types.items():

            if extension in extensions:

                destination_folder = os.path.join(folder_to_organize, folder_name)

                os.makedirs(destination_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(destination_folder, filename)
                )

                print(f"Moved {filename} to {folder_name}")

                moved = True
                break

        if not moved:
            others_folder = os.path.join(folder_to_organize, "Others")

            os.makedirs(others_folder, exist_ok=True)

            shutil.move(
                file_path,
                os.path.join(others_folder, filename)
            )

            print(f"Moved {filename} to Others")