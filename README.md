# Keylogger Fooler

A defensive security tool that generates fake sensitive-looking data to confuse keyloggers, file searchers, and clipboard catchers.

**Made with pride by Cahit Karahan**

## Features

### Data Types Generated

- **Fake Credentials**: Multiple username/password formats including:
  - Email:password combinations
  - User/pass pairs with various separators
  - Domain authentication credentials
  - Realistic password patterns (Welcome2024!, Summer2023#, etc.)

- **Fake Crypto Data**:
  - Ethereum addresses (0x...) with private keys
  - Bitcoin addresses (Legacy, P2SH, Bech32 formats)
  - Altcoin addresses (Litecoin, Dogecoin, Ripple, Cardano, Solana, Polkadot)
  - Multiple private key formats (hex, WIF)
  - BIP39 seed phrases (12, 15, 18, or 24 words)

- **Fake API Keys**: Service-specific realistic formats for 35+ popular services:
  - **AI Services**: OpenAI, Anthropic Claude, Google AI (Gemini), Hugging Face, Cohere, Replicate
  - **Cloud Hosting**: AWS (Access Key & Secret), Google Cloud, Azure, DigitalOcean, Heroku
  - **Payment**: Stripe (live/test keys), PayPal
  - **Communication**: Twilio, SendGrid, Mailgun
  - **Development**: GitHub, GitLab, npm, Docker Hub
  - **Database**: MongoDB Atlas, Supabase, Firebase
  - **Analytics**: Google Analytics, Datadog, New Relic
  - **Social Media**: Twitter/X, Facebook, Discord Bot
  - **Maps**: Google Maps, Mapbox

- **Fake SSH Keys**: OpenSSH private key format

- **Fake Credit Cards**:
  - Card numbers with realistic prefixes (Visa, Mastercard, Amex)
  - Expiry dates and CVV codes

- **Fake Database Connections**: Connection strings for:
  - MongoDB
  - PostgreSQL
  - MySQL
  - Redis

### Output Methods

- **Keyboard Simulation**: Types data character-by-character to fool keyloggers
- **File Writing**: Saves data to files that searchers might target
- **Clipboard**: Copies sensitive-looking data periodically

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### ⚠️ IMPORTANT WARNING
**STAY IN YOUR TERMINAL/COMMAND PROMPT WINDOW!** When keyboard simulation is enabled, the script will type random characters. If you switch to another window (browser, text editor, etc.), these random keystrokes can mess up your work, trigger unwanted actions, or cause data loss. Always keep focus on the terminal window while the script is running.

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

## Output Files

Fake data is written to the `./fake_data/` directory in separate files:
- `credentials.txt` - Fake usernames, emails, and passwords
- `crypto_wallets.txt` - Fake crypto addresses and private keys
- `seed_phrases.txt` - Fake wallet seed phrases
- `api_keys.txt` - Fake API keys for various services
- `ssh_keys.txt` - Fake SSH private keys
- `payment_methods.txt` - Fake credit card data
- `database_configs.txt` - Fake database connection strings

## Example Output

```
--- Generating Fake Credentials ---
[TYPING] email: john.smith42@gmail.com
         password: Welcome2024!
[FILE] Written to ./fake_data/credentials.txt
[CLIPBOARD] Copied: john.smith42@gmail.com:Welcome2024!

--- Generating Fake Crypto Data ---
[TYPING] Cardano Address: addr1q9x5v8n2m...
         Private Key: 0x7f2a9d4e8b1c...
[FILE] Written to ./fake_data/crypto_wallets.txt
[CLIPBOARD] Copied: addr1q9x5v8n2m...

--- Generating Fake Database Connections ---
[TYPING] Database Connection:
         postgresql://user:Xk9$mP2@vL7&@db.example.com:5432/maindb
[FILE] Written to ./fake_data/database_configs.txt
[CLIPBOARD] Copied: postgresql://user:Xk9$mP2@vL7&@db.example.com:5432/maindb
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
