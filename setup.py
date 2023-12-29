from cx_Freeze import setup, Executable

base = None    

executables = [Executable("fishing.py", base=base)]

packages = ["idna", "mouse", "keyboard", "time", "pyautogui", "pytesseract", "cv2"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "minecraft fishing",
    options = options,
    version = "1.0",
    description = 'minecraft afk fishing',
    executables = executables
)