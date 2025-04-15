# CTkFileDialog
Unofficial file dialog for CustomTkinter.

![Screenshot](https://raw.githubusercontent.com/limafresh/CTkFileDialog/main/screenshot1.png)

![Screenshot](https://raw.githubusercontent.com/limafresh/CTkFileDialog/main/screenshot2.png)

## How to use?
Download and place the CTkFileDialog folder into your script folder.

### Open file
```python
dialog = CTkFileDialog(root, save=False)
if dialog.path:
    print(dialog.path)
```

### Save file
```python
dialog = CTkFileDialog(root, save=True)
if dialog.path:
    print(dialog.path)
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

## Projects using CTkFileDialog
- [Brushshe](https://github.com/limafresh/Brushshe): fully functional painting app written in CustomTkinter
