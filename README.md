# 🗃️ File Organizer Script

A simple Python script to automatically organize files in a folder based on file type (e.g., Images, Documents, Music, etc.).

## 📌 Features
- Sorts files into folders by extension
- Supports images, documents, code files, music, videos, archives, and more
- Automatically creates folders if they don’t exist
- Handles unknown file types

## 📂 Example
Before:
```
Downloads/
├── pic.jpg
├── resume.pdf
├── song.mp3
```

After:
```
Downloads/
├── Images/
│   └── pic.jpg
├── Documents/
│   └── resume.pdf
├── Music/
│   └── song.mp3
```

## 🚀 How to Use

1. Clone the repo or download `file_organizer.py`
2. Run the script in terminal:

```bash
python file_organizer.py
```

3. Enter the full path of the folder you want to organize.

## 🔧 Technologies
- Python 3
- `os`, `shutil`, `pathlib`

## 📄 License
MIT License (you can change this)

---

Made with ☕ and Python.
