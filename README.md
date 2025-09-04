# CTkFileDialog
Unofficial file dialog for CustomTkinter.

![Screenshot](https://raw.githubusercontent.com/limafresh/CTkFileDialog/main/screenshot1.png)

![Screenshot](https://raw.githubusercontent.com/limafresh/CTkFileDialog/main/screenshot2.png)

![Screenshot](https://raw.githubusercontent.com/limafresh/CTkFileDialog/main/screenshot3.png)

## How to use?
Download and place the CTkFileDialog folder (where `__init__.py` is located) into your script folder.

```python
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

```

## Arguments
| Argument | Description |
| ---------------- | ------------ |
| **width** | dialog window width |
| **height** | dialog window height |
| **hidden_files** | False (by default) or True |
| **initialdir** | initial dir |
| **title** | dialog window title |
| **save** | `save=False` if open file (by default), `save=True` if save file |
| **save_extension** | Save extension, for example, `save_extension=".txt"` |
| **open_folder** | if open folder, `True` or `False` |
| **button_color** | buttons color, for example, `button_color=red` or `button_color=#000000` |
| **btn_hover_color** | buttons hover color |
| **button_radius** | buttons radius, int |
| **button_hover** | `True` or `False` |
| **button_border** | buttons border width, int |
| **btn_border_color** | buttons hover color |
| **btn_text_color** | buttons text color |
| **ok_text** | "OK" button text, for example, `ok_text="Done"` |
| **cancel_text** | "Cancel" button text |

# CTkFileWidget (new!)
A widget that can be added to an existing window.

![Screenshot](https://raw.githubusercontent.com/limafresh/CTkFileDialog/main/screenshot4.png)

```python
def my_command():
    print(filewidget.path)

filewidget = CTkFileWidget(root, command=my_command)
filewidget.pack(padx=10, pady=10)
```

## Arguments
| Argument | Description |
| ---------------- | ------------ |
| **master** | master, required |
| **command** | the command that will be executed when you click "OK" |
| **All of CTkFileDialog** | except **title** and **cancel_text** |

## Projects using CTkFileDialog
- [Brushshe](https://github.com/limafresh/Brushshe) (uses a modified version): fully functional painting app written in CustomTkinter
