import os
import shutil
from pathlib import Path

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Code": [".py", ".js", ".cpp", ".java", ".html", ".css"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"]
}

def organize_folder(folder_path):
    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        print("❌ Invalid folder path.")
        return

    for file in folder.iterdir():
        if file.is_file():
            moved = False
            for category, extensions in FILE_TYPES.items():
                if file.suffix.lower() in extensions:
                    category_folder = folder / category
                    category_folder.mkdir(exist_ok=True)
                    shutil.move(str(file), str(category_folder / file.name))
                    moved = True
                    break

            if not moved:
                others_folder = folder / "Others"
                others_folder.mkdir(exist_ok=True)
                shutil.move(str(file), str(others_folder / file.name))

if __name__ == "__main__":
    path_input = input("Enter the folder path to organize: ").strip()
    organize_folder(path_input)
    print("✅ Done organizing files!")
