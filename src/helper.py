import os
import sys

def get_asset_path(filename):
    #if running in PyInstaller bundle, it gets the base path from the temporary directory _MEIPASS
    #otherwise, it returns the path relative to the script's directory.
    if hasattr(sys, '_MEIPASS'):
        #running in a PyInstaller bundle
        base_path = sys._MEIPASS
        print(base_path)
    else:
        #running as a script in Visual Studio Code
        base_path = os.path.dirname(os.path.abspath(__file__))
        base_path = base_path + "/../"

    joined = os.path.join(base_path, filename)
    return joined