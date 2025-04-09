import os
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

PATH = os.path.dirname(os.path.realpath(__file__))


class CTkFileDialog(ctk.CTkToplevel):
    def __init__(
        self, parent, width=500, height=400, initialdir=".", title=None, save=False
    ):
        super().__init__(parent)
        self.geometry(f"{width}x{height}")

        self.title(
            "Save file" if save else "Open file"
        ) if title is None else self.title(title)
        self.save_mode = save

        self.path = None

        # Images by Vijay Verma from Wikimedia Commons, licensed under CC0 1.0
        self.folder_image = tk.PhotoImage(file=os.path.join(PATH, "folder.png"))
        self.file_image = tk.PhotoImage(file=os.path.join(PATH, "file.png"))

        self.path_frame = ctk.CTkFrame(self)
        self.path_frame.pack(fill=ctk.X, padx=10, pady=10)

        self.path_entry = ctk.CTkEntry(self.path_frame)
        self.path_entry.pack(expand=True, fill=ctk.X, side=ctk.LEFT, padx=10, pady=10)
        self.path_entry.insert(ctk.END, os.path.join(os.path.abspath(initialdir), ""))
        self.path_entry.bind("<Return>", self._populate_file_list)

        self.up_btn = ctk.CTkButton(
            self.path_frame, text="↑", width=30, command=self._up
        )
        self.up_btn.pack(side=ctk.RIGHT, padx=10, pady=10)

        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(side=ctk.BOTTOM, fill=ctk.X, padx=10, pady=10)

        ok_btn = ctk.CTkButton(btn_frame, text="OK")
        ok_btn.pack(side=ctk.RIGHT)

        if self.save_mode:
            ok_btn.configure(command=self._ok_save)
        else:
            ok_btn.configure(command=self._on_click)

        ctk.CTkButton(btn_frame, text="Cancel", command=self.destroy).pack(
            side=ctk.RIGHT, padx=10
        )

        if self.save_mode:
            self.save_entry = ctk.CTkEntry(
                self, placeholder_text="Enter name for save..."
            )
            self.save_entry.pack(side=ctk.BOTTOM, fill=ctk.X, padx=10)

        self.tree_frame = ctk.CTkFrame(self)
        self.tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        style = ttk.Style()
        style.configure("Treeview", rowheight=30)

        self.tree = ttk.Treeview(self.tree_frame, columns=("Item"), show="tree")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.tree.heading("Item")
        self.tree.bind("<Double-1>", self._on_click)

        self._populate_file_list()
        self.wait_window()

    def _populate_file_list(self, event=None):
        if self.path_entry.get() == "":
            self.path_entry.insert(ctk.END, os.path.join(os.path.abspath("."), ""))
        self.initialdir = self.path_entry.get()
        try:
            for item in self.tree.get_children():
                self.tree.delete(item)
            for item in os.listdir(self.initialdir):
                full_path = os.path.join(self.initialdir, item)
                if os.path.isdir(full_path):
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
        selected_path = os.path.join(self.initialdir, selected_name)

        if os.path.isdir(selected_path):
            self.initialdir = selected_path
            self.path_entry.delete(0, ctk.END)
            self.path_entry.insert(ctk.END, self.initialdir)
            self._populate_file_list()
        else:
            if not self.save_mode:
                self.path = selected_path
                self.destroy()

    def _ok_save(self):
        filename = self.save_entry.get()
        selected_path = os.path.join(self.initialdir, filename)
        self.path = selected_path
        self.destroy()

    def _up(self):
        current_path = os.path.normpath(self.path_entry.get())
        new_path = os.path.join(os.path.dirname(current_path), "")
        self.path_entry.delete(0, ctk.END)
        self.path_entry.insert(ctk.END, new_path)
        self._populate_file_list()
