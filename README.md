# Keylogger Fooler

A defensive security tool that generates fake sensitive-looking data to confuse keyloggers, file searchers, and clipboard catchers.

**Made with pride by Cahit Karahan**

## Features

- **Fake Credentials**: Generates random usernames, passwords, and email addresses
- **Fake Crypto Data**: Creates fake Ethereum/Bitcoin addresses, private keys, and seed phrases
- **Fake API Keys**: Generates random API keys for various services
- **Multiple Output Methods**:
  - Simulates keyboard typing (fools keyloggers)
  - Writes to files (fools file searchers)
  - Copies to clipboard (fools clipboard catchers)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic usage (runs continuously every 10 seconds):
```bash
python keylogger_fooler.py
```

### Custom interval (e.g., every 5 seconds):
```bash
python keylogger_fooler.py 5
```

### Limited iterations (e.g., run 20 times with 3 second intervals):
```bash
python keylogger_fooler.py 3 20
```

### Arguments:
```
python keylogger_fooler.py [interval_seconds] [iterations]
```
- `interval_seconds`: Time between generations (default: 10)
- `iterations`: Number of times to run (default: infinite)

## Output

Fake data is written to the `./fake_data/` directory in files:
- `credentials.txt` - Fake usernames and passwords
- `crypto_wallets.txt` - Fake crypto addresses and private keys
- `seed_phrases.txt` - Fake wallet seed phrases
- `api_keys.txt` - Fake API keys

## Example Output

```
user: megawizard8234
pass: K7#mP9$xL2@vN5&qR8

ETH Address: 0x742d35cc6634c0532925a3b844bc9e7fa6785f92
Private Key: 0x47f3e5d8c9a1b6...

Seed Phrase (12 words):
amazing dragon master account secure wallet digital access crypto elite super fund
```

## Disclaimer

This tool is for educational and defensive security purposes only. It generates completely fake data to add noise and misdirection against unauthorized monitoring tools.

## How It Works

1. **Keyboard Simulation**: Uses `pynput` to simulate realistic typing patterns
2. **File Writing**: Writes fake data to files that searchers might target
3. **Clipboard**: Copies fake sensitive data to clipboard periodically

This creates multiple layers of fake "sensitive" data that would confuse automated data collection tools.

## License

MIT License

Copyright (c) 2025 Cahit Karahan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
