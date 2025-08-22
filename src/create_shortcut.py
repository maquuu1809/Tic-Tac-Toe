import os
import winshell
from win32com.client import Dispatch

def create_shortcut(exe_path, name="Tic-Tac-Toe"):
    exe_path = os.path.abspath(exe_path)

    desktop = winshell.desktop()
    shortcut_path = os.path.join(desktop, f"{name}.lnk")

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = exe_path
    shortcut.WorkingDirectory = os.path.dirname(exe_path)
    shortcut.IconLocation = exe_path
    shortcut.save()

    print(f"📌 Shortcut created on Desktop: {shortcut_path}")