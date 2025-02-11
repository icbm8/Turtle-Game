import os
import sys

def get_asset_path(filename):
    if hasattr(sys, '_MEIPASS'):
        # Running in a PyInstaller bundle
        base_path = sys._MEIPASS
    else:
        # Running as a script in Visual Studio Code
        base_path = os.path.dirname(os.path.abspath(__file__))
        base_path = base_path + "/../"
    print(base_path)

    bob = os.path.join(base_path, filename)
    print(bob)
    return bob