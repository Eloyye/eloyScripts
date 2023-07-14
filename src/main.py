import winreg
import os
from dotenv import load_dotenv, set_key


def add_to_startup(file_path):
    key = winreg.HKEY_CURRENT_USER
    run_key = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'

    with winreg.OpenKey(key, run_key, 0, winreg.KEY_SET_VALUE) as registry_key:
        winreg.SetValue(registry_key, 'eloyScripts', 0, winreg.REG_SZ, file_path)


if __name__ == '__main__':
    # load local environmental variables
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    load_dotenv(dotenv_path=dotenv_path)

    with os.getenv('PATH_TO_EXT_SSD_KEY') as exec_path:
        if not exec_path:
            print('WHICH DRIVE IS THE UNLOCK ON?')
            full_path = rf'{input()}:\SanDisk Drive Unlock.exe'
            if not os.path.exists(full_path):
                raise Exception(f"Path: {full_path} , could not be found")
            set_key('../.env', 'PATH_TO_EXT_SSD_KEY', full_path)
            exec_path = os.getenv('PATH_TO_EXT_SSD_KEY')

    add_to_startup(exec_path)
