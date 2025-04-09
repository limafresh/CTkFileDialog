import customtkinter as ctk
from CTkFileDialog import CTkFileDialog


def open_dialog():
    dialog = CTkFileDialog(root, title="Open project, please)", save=False)
    if dialog.path:
        print(dialog.path)


def save_dialog():
    dialog = CTkFileDialog(root, title="Save project, please)", save=True)
    if dialog.path:
        print(dialog.path)


root = ctk.CTk()

btn1 = ctk.CTkButton(root, text="Open", command=open_dialog)
btn1.pack(padx=20, pady=20)

btn2 = ctk.CTkButton(root, text="Save", command=save_dialog)
btn2.pack(padx=20, pady=20)

root.mainloop()
