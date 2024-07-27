import os
import shutil
import customtkinter as ctk
from tkinter import filedialog, messagebox

def organize(directory):
    extensions = {
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",
        ".jfif": "Images",
        ".gif": "Images",
        ".mp4": "Videos",
        ".mov": "Videos",
        ".py": "Python",
        ".ipynb": "Python",
        ".pdf": "Documents",
        ".txt": "Documents",
        ".mp3": "Music",
        ".wav": "Music",
        ".doc": "Documents",
        ".docx": "Documents",
        ".zip": "Directories",
        ".rar": "Directories",
        ".csv": "Sheets",
        ".xlsx": "Sheets",
        ".xlsm": "Sheets",
        ".sql": "SQL"
    }

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower()

            if extension in extensions:
                folder_name = extensions[extension]

                folder_path = os.path.join(directory, folder_name)
                os.makedirs(folder_path, exist_ok=True)

                destination_path = os.path.join(folder_path, filename)
                shutil.move(file_path, destination_path)

                print(f"Moved {filename} to {folder_name} folder.")
            else:
                print(f"Skipped {filename}. Unknown file extension.")
        else:
            print(f"Skipped {filename}. It is a directory")

    messagebox.showinfo("Info", "File organization completed.")

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        organize(directory)

app = ctk.CTk()
app.title("File Organizer")
app.geometry("400x200")

title_label = ctk.CTkLabel(app, text="File Organizer", font=ctk.CTkFont(size=20, weight="bold"))
title_label.pack(pady=20)

frame = ctk.CTkFrame(app)
frame.pack(padx=20, pady=20, expand=True)

select_button = ctk.CTkButton(frame, text="Select Directory", command=select_directory)
select_button.pack(side=ctk.LEFT, padx=10)

exit_button = ctk.CTkButton(frame, text="Exit", command=app.quit, fg_color="#ff6666", hover_color="#cc0000")
exit_button.pack(side=ctk.RIGHT, padx=10)

app.mainloop()
