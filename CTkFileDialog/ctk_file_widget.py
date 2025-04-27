import os
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

PATH = os.path.dirname(os.path.realpath(__file__))


class CTkFileWidget(ctk.CTkFrame):
    def __init__(
        self,
        master,
        width=500,
        height=400,
        hidden_files=False,
        initialdir=".",
        save=False,
        save_extension="",
        open_folder=False,
        command=None,
    ):
        super().__init__(master, width=width, height=height)
        self.pack_propagate(False)

        self.hidden_files = hidden_files
        self.save_mode = save
        self.save_extension = save_extension
        self.open_folder = open_folder
        self.command = command

        self.path = None

        # Images by Vijay Verma from Wikimedia Commons, licensed under CC0 1.0
        self.folder_image = tk.PhotoImage(file=os.path.join(PATH, "folder.png"))
        self.file_image = tk.PhotoImage(file=os.path.join(PATH, "file.png"))

        self.path_frame = ctk.CTkFrame(self)
        self.path_frame.pack(fill=ctk.X, padx=10, pady=10)

        self.initialdir = ctk.StringVar(
            value=os.path.join(os.path.abspath(initialdir), "")
        )
        self.path_entry = ctk.CTkEntry(self.path_frame, textvariable=self.initialdir)
        self.path_entry.pack(expand=True, fill=ctk.X, side=ctk.LEFT, padx=10, pady=10)
        self.path_entry.bind("<Return>", self._populate_file_list)

        self.up_btn = ctk.CTkButton(
            self.path_frame, text="↑", width=30, command=self._up
        )
        self.up_btn.pack(side=ctk.RIGHT, padx=10, pady=10)

        if save_extension:
            extension_btn = ctk.CTkButton(
                self.path_frame, text=save_extension, width=50, hover=False
            )
            extension_btn.pack(side=ctk.RIGHT, padx=10, pady=10)

        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(side=ctk.BOTTOM, fill=ctk.X, padx=10, pady=10)

        ok_btn = ctk.CTkButton(btn_frame, text="OK")
        ok_btn.pack(side=ctk.RIGHT)

        if self.save_mode:
            ok_btn.configure(command=self._ok_save)
        elif self.open_folder:
            ok_btn.configure(command=self._ok_folder)
        else:
            ok_btn.configure(command=self._on_click)

        if self.save_mode:
            self.save_entry = ctk.CTkEntry(
                self.frame, placeholder_text="Enter name for save..."
            )
            self.save_entry.pack(side=ctk.BOTTOM, fill=ctk.X, padx=10)

        self.tree_frame = ctk.CTkFrame(self)
        self.tree_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=5)

        style = ttk.Style()
        style.configure("Treeview", rowheight=30)

        self.tree = ttk.Treeview(self.tree_frame, show="tree")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.tree.bind("<Double-1>", self._on_click)

        self._populate_file_list()

    def _populate_file_list(self, event=None):
        if self.initialdir.get() == "":
            self.initialdir.set(os.path.join(os.path.abspath("."), ""))
        try:
            for item in self.tree.get_children():
                self.tree.delete(item)
            items = sorted(os.listdir(self.initialdir.get()))
            for item in items:
                if not item.startswith(".") or self.hidden_files:
                    if os.path.isdir(os.path.join(self.initialdir.get(), item)):
                        self.tree.insert("", tk.END, text=item, image=self.folder_image)
                    else:
                        self.tree.insert("", tk.END, text=item, image=self.file_image)
        except Exception:
            pass

    def _on_click(self, event=None):
        selected_item = self.tree.focus()
        if not selected_item:
            return

        selected_name = self.tree.item(selected_item)["text"]
        selected_path = os.path.join(self.initialdir.get(), selected_name)

        if os.path.isdir(selected_path):
            self.initialdir.set(os.path.join(os.path.abspath(selected_path), ""))
            self._populate_file_list()
        else:
            if not self.save_mode:
                self.path = selected_path
                if self.command is not None:
                    self.command()

    def _ok_folder(self, event=None):
        self.path = self.initialdir.get()
        if self.command is not None:
            self.command()

    def _ok_save(self, event=None):
        if (
            self.save_entry.get() == ""
            or self.save_entry.get().startswith(" ")
            or self.save_entry.get().endswith(" ")
        ):
            return
        selected_path = os.path.join(self.initialdir.get(), self.save_entry.get())
        self.path = selected_path + self.save_extension
        if self.command is not None:
            self.command()

    def _up(self):
        current_path = os.path.normpath(self.initialdir.get())
        self.initialdir.set(os.path.join(os.path.dirname(current_path), ""))
        self._populate_file_list()
