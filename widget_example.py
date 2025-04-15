import customtkinter as ctk
from CTkFileDialog import CTkFileWidget


def configure_label():
    label.configure(text=filewidget.path)


root = ctk.CTk()
root.geometry("600x500")

label = ctk.CTkLabel(root)
label.pack(padx=10, pady=10)

filewidget = CTkFileWidget(root, command=configure_label)
filewidget.pack(padx=10, pady=10)

root.mainloop()
