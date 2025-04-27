import customtkinter as ctk
from CTkFileDialog import CTkFileDialog


def open_dialog():
    dialog = CTkFileDialog(title="Open project, please")
    if dialog.path:
        print(dialog.path)


def open_folder_dialog():
    dialog = CTkFileDialog(title="Open folder, please", open_folder=True)
    if dialog.path:
        print(dialog.path)


def save_dialog():
    dialog = CTkFileDialog(
        title="Save project, please", save=True, save_extension=".txt"
    )
    if dialog.path:
        print(dialog.path)


root = ctk.CTk()

btn1 = ctk.CTkButton(root, text="Open", command=open_dialog)
btn1.pack(padx=20, pady=20)

btn2 = ctk.CTkButton(root, text="Open folder", command=open_folder_dialog)
btn2.pack(padx=20, pady=20)

btn3 = ctk.CTkButton(root, text="Save", command=save_dialog)
btn3.pack(padx=20, pady=20)

root.mainloop()
