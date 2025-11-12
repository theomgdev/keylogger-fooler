#!/usr/bin/env python3
"""
Keylogger Fooler - A defensive security tool to generate fake sensitive data
This script generates fake credentials, crypto keys, and other sensitive-looking
data to confuse keyloggers, file searchers, and clipboard catchers.
"""

import random
import string
import time
import os
import sys
from pathlib import Path

try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False
    print("⚠️  pyperclip not installed. Clipboard functionality disabled.")
    print("   Install with: pip install pyperclip")

try:
    from pynput.keyboard import Controller as KeyboardController
    KEYBOARD_AVAILABLE = True
except ImportError:
    KEYBOARD_AVAILABLE = False
    print("⚠️  pynput not installed. Keyboard simulation disabled.")
    print("   Install with: pip install pynput")


class FakeDataGenerator:
    """Generate fake sensitive-looking data"""

    # Common words for BIP39-style seed phrases
    BIP39_WORDS = [
        "abandon", "ability", "able", "about", "above", "absent", "absorb", "abstract",
        "absurd", "abuse", "access", "accident", "account", "accuse", "achieve", "acid",
        "acoustic", "acquire", "across", "act", "action", "actor", "actress", "actual",
        "adapt", "add", "addict", "address", "adjust", "admit", "adult", "advance",
        "advice", "aerobic", "afford", "afraid", "again", "age", "agent", "agree",
        "ahead", "aim", "air", "airport", "aisle", "alarm", "album", "alcohol",
        "alert", "alien", "all", "alley", "allow", "almost", "alone", "alpha",
        "already", "also", "alter", "always", "amateur", "amazing", "among", "amount",
        "amused", "analyst", "anchor", "ancient", "anger", "angle", "angry", "animal",
        "ankle", "announce", "annual", "another", "answer", "antenna", "antique", "anxiety",
        "any", "apart", "apology", "appear", "apple", "approve", "april", "arch",
        "arctic", "area", "arena", "argue", "arm", "armed", "armor", "army",
        "around", "arrange", "arrest", "arrive", "arrow", "art", "artefact", "artist",
        "artwork", "ask", "aspect", "assault", "asset", "assist", "assume", "asthma",
        "athlete", "atom", "attack", "attend", "attitude", "attract", "auction", "audit",
        "august", "aunt", "author", "auto", "autumn", "average", "avocado", "avoid",
        "awake", "aware", "away", "awesome", "awful", "awkward", "axis", "baby",
        "bachelor", "bacon", "badge", "bag", "balance", "balcony", "ball", "bamboo",
        "banana", "banner", "bar", "barely", "bargain", "barrel", "base", "basic",
        "basket", "battle", "beach", "bean", "beauty", "because", "become", "beef",
        "before", "begin", "behave", "behind", "believe", "below", "belt", "bench",
    ]

    COMMON_DOMAINS = [
        "gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "protonmail.com",
        "icloud.com", "aol.com", "mail.com", "zoho.com", "yandex.com", "fastmail.com",
        "tutanota.com", "gmx.com", "inbox.com", "hey.com"
    ]

    FIRST_NAMES = [
        "john", "sarah", "mike", "emma", "david", "lisa", "chris", "anna",
        "james", "mary", "robert", "jennifer", "william", "linda", "richard",
        "patricia", "thomas", "nancy", "daniel", "karen", "alex", "jessica"
    ]

    LAST_NAMES = [
        "smith", "johnson", "williams", "brown", "jones", "garcia", "miller",
        "davis", "rodriguez", "martinez", "wilson", "anderson", "taylor", "thomas",
        "moore", "martin", "jackson", "thompson", "white", "lopez", "lee", "walker"
    ]

    PASSWORD_PATTERNS = [
        lambda: ''.join(random.choice(string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?") for _ in range(random.randint(12, 24))),
        lambda: random.choice(["Welcome", "Password", "Admin", "Secret", "P@ssw0rd"]) + str(random.randint(100, 9999)) + random.choice(["!", "@", "#", "$"]),
        lambda: random.choice(["Summer", "Winter", "Spring", "Autumn"]) + str(random.randint(2015, 2024)) + random.choice(["!", "?", "#"]),
        lambda: ''.join(random.choices(string.ascii_uppercase, k=2)) + ''.join(random.choices(string.ascii_lowercase, k=4)) + ''.join(random.choices(string.digits, k=3)) + random.choice("!@#$"),
    ]

    @staticmethod
    def generate_password(length=None):
        """Generate a fake password with various patterns"""
        if length is None:
            return random.choice(FakeDataGenerator.PASSWORD_PATTERNS)()

        chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
        password = ''.join(random.choice(chars) for _ in range(length))
        return password

    @staticmethod
    def generate_username():
        """Generate a fake username with multiple patterns"""
        patterns = [
            # Pattern 1: adjective + noun + numbers
            lambda: random.choice(["cool", "super", "mega", "ultra", "pro", "elite", "master", "dark", "shadow", "cyber", "quantum", "digital"]) +
                    random.choice(["user", "hacker", "coder", "gamer", "ninja", "wizard", "dragon", "phoenix", "wolf", "tiger", "eagle", "lion"]) +
                    str(random.randint(0, 9999)),
            # Pattern 2: first name + last name
            lambda: random.choice(FakeDataGenerator.FIRST_NAMES) + random.choice(FakeDataGenerator.LAST_NAMES) + str(random.randint(0, 999)),
            # Pattern 3: first initial + last name + numbers
            lambda: random.choice(FakeDataGenerator.FIRST_NAMES)[0] + random.choice(FakeDataGenerator.LAST_NAMES) + str(random.randint(10, 99)),
            # Pattern 4: name with underscore
            lambda: random.choice(FakeDataGenerator.FIRST_NAMES) + "_" + random.choice(FakeDataGenerator.LAST_NAMES),
            # Pattern 5: name with dots
            lambda: random.choice(FakeDataGenerator.FIRST_NAMES) + "." + random.choice(FakeDataGenerator.LAST_NAMES) + str(random.randint(1, 99)),
        ]

        return random.choice(patterns)()

    @staticmethod
    def generate_email():
        """Generate a fake email address"""
        username = FakeDataGenerator.generate_username().lower()
        domain = random.choice(FakeDataGenerator.COMMON_DOMAINS)
        return f"{username}@{domain}"

    @staticmethod
    def generate_eth_address():
        """Generate a fake Ethereum-style address"""
        hex_chars = '0123456789abcdef'
        address = '0x' + ''.join(random.choice(hex_chars) for _ in range(40))
        return address

    @staticmethod
    def generate_btc_address():
        """Generate a fake Bitcoin-style address"""
        patterns = [
            # Legacy address (starts with 1)
            lambda: '1' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(26, 34))),
            # P2SH address (starts with 3)
            lambda: '3' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(26, 34))),
            # Bech32 address (starts with bc1)
            lambda: 'bc1' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(39, 59))),
        ]
        return random.choice(patterns)()

    @staticmethod
    def generate_other_crypto_address():
        """Generate fake addresses for other cryptocurrencies"""
        crypto_patterns = [
            ("Litecoin", lambda: random.choice(['L', 'M']) + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(33))),
            ("Dogecoin", lambda: 'D' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(33))),
            ("Ripple", lambda: 'r' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(33))),
            ("Cardano", lambda: 'addr1' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(90, 104)))),
            ("Solana", lambda: ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(44))),
            ("Polkadot", lambda: '1' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(47))),
        ]
        name, generator = random.choice(crypto_patterns)
        return name, generator()

    @staticmethod
    def generate_private_key():
        """Generate a fake private key with multiple formats"""
        formats = [
            # Hex format with 0x prefix
            lambda: '0x' + ''.join(random.choice('0123456789abcdef') for _ in range(64)),
            # Pure hex without prefix
            lambda: ''.join(random.choice('0123456789abcdef') for _ in range(64)),
            # WIF format (Bitcoin)
            lambda: random.choice(['5', 'K', 'L']) + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(50)),
        ]
        return random.choice(formats)()

    @staticmethod
    def generate_seed_phrase(word_count=None):
        """Generate a fake BIP39-style seed phrase"""
        if word_count is None:
            word_count = random.choice([12, 15, 18, 24])
        return ' '.join(random.choice(FakeDataGenerator.BIP39_WORDS) for _ in range(word_count))

    @staticmethod
    def generate_api_key_for_service(service_name):
        """Generate a fake API key with service-specific formats"""
        service_formats = {
            # AI Services
            "OpenAI": lambda: 'sk-' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(48)),
            "Anthropic Claude": lambda: 'sk-ant-' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(90, 110))),
            "Google AI (Gemini)": lambda: 'AIzaSy' + ''.join(random.choice(string.ascii_letters + string.digits + '-_') for _ in range(33)),
            "Hugging Face": lambda: 'hf_' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(30, 40))),
            "Cohere": lambda: ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(40)),
            "Replicate": lambda: 'r8_' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(35, 45))),

            # Cloud Services
            "AWS": lambda: 'AKIA' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16)),
            "AWS Secret": lambda: ''.join(random.choice(string.ascii_letters + string.digits + '+/') for _ in range(40)),
            "Google Cloud": lambda: 'AIzaSy' + ''.join(random.choice(string.ascii_letters + string.digits + '-_') for _ in range(33)),
            "Azure": lambda: ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32)),
            "DigitalOcean": lambda: 'dop_v1_' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(64)),
            "Heroku": lambda: ''.join(random.choice(string.ascii_lowercase + string.digits + '-') for _ in range(36)),

            # Payment Services
            "Stripe": lambda: random.choice(['sk_live_', 'sk_test_']) + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(24, 99))),
            "PayPal": lambda: 'A' + ''.join(random.choice(string.ascii_letters + string.digits + '-_') for _ in range(random.randint(60, 80))),

            # Communication Services
            "Twilio": lambda: 'SK' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(32)),
            "SendGrid": lambda: 'SG.' + ''.join(random.choice(string.ascii_letters + string.digits + '-_') for _ in range(random.randint(60, 70))),
            "Mailgun": lambda: 'key-' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(32)),

            # Development Services
            "GitHub": lambda: random.choice(['ghp_', 'gho_', 'ghu_']) + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(36)),
            "GitLab": lambda: 'glpat-' + ''.join(random.choice(string.ascii_letters + string.digits + '-_') for _ in range(20)),
            "npm": lambda: 'npm_' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(36)),
            "Docker Hub": lambda: 'dckr_pat_' + ''.join(random.choice(string.ascii_letters + string.digits + '-_') for _ in range(random.randint(40, 60))),

            # Database Services
            "MongoDB Atlas": lambda: ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(30, 40))),
            "Supabase": lambda: 'eyJ' + ''.join(random.choice(string.ascii_letters + string.digits + '-_') for _ in range(random.randint(100, 150))),
            "Firebase": lambda: 'AIzaSy' + ''.join(random.choice(string.ascii_letters + string.digits + '-_') for _ in range(33)),

            # Analytics & Monitoring
            "Google Analytics": lambda: 'UA-' + str(random.randint(10000000, 99999999)) + '-' + str(random.randint(1, 9)),
            "Datadog": lambda: ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(32)),
            "New Relic": lambda: 'NRAK-' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(27)),

            # Social Media APIs
            "Twitter/X": lambda: ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(40, 50))),
            "Facebook": lambda: 'EAA' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(100, 180))),
            "Discord Bot": lambda: 'MTE' + ''.join(random.choice(string.ascii_letters + string.digits + '-_') for _ in range(random.randint(60, 70))),

            # Maps & Location
            "Google Maps": lambda: 'AIzaSy' + ''.join(random.choice(string.ascii_letters + string.digits + '-_') for _ in range(33)),
            "Mapbox": lambda: 'pk.' + ''.join(random.choice(string.ascii_letters + string.digits + '.') for _ in range(random.randint(80, 100))),
        }

        if service_name in service_formats:
            return service_formats[service_name]()
        else:
            # Fallback to generic format
            return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))

    @staticmethod
    def generate_api_key():
        """Generate a fake API key with various formats (legacy method)"""
        formats = [
            # Standard alphanumeric
            lambda: ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32)),
            # With dashes (like AWS)
            lambda: '-'.join(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4)) for _ in range(8)),
            # With underscores
            lambda: 'sk_' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(48)),
            # JWT-style (base64-like)
            lambda: '.'.join(''.join(random.choice(string.ascii_letters + string.digits + '-_') for _ in range(random.randint(20, 40))) for _ in range(3)),
        ]
        return random.choice(formats)()

    @staticmethod
    def generate_ssh_key():
        """Generate a fake SSH private key header"""
        return """-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAYEA{}
-----END OPENSSH PRIVATE KEY-----""".format(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(60)))

    @staticmethod
    def generate_credit_card():
        """Generate a fake credit card number (Luhn algorithm not implemented, purely fake)"""
        # Common card prefixes
        prefixes = ['4', '51', '52', '53', '54', '55', '37', '34', '6011']
        prefix = random.choice(prefixes)
        remaining_length = 16 - len(prefix)
        card_number = prefix + ''.join(random.choice(string.digits) for _ in range(remaining_length))

        # Format with spaces
        formatted = ' '.join([card_number[i:i+4] for i in range(0, len(card_number), 4)])
        expiry = f"{random.randint(1, 12):02d}/{random.randint(25, 30)}"
        cvv = ''.join(random.choice(string.digits) for _ in range(3))

        return f"Card: {formatted}\nExpiry: {expiry}\nCVV: {cvv}"

    @staticmethod
    def generate_database_connection():
        """Generate fake database connection strings"""
        db_types = [
            lambda: f"mongodb://admin:{FakeDataGenerator.generate_password(16)}@localhost:27017/production",
            lambda: f"postgresql://user:{FakeDataGenerator.generate_password(16)}@db.example.com:5432/maindb",
            lambda: f"mysql://root:{FakeDataGenerator.generate_password(16)}@192.168.1.100:3306/app_database",
            lambda: f"redis://:{FakeDataGenerator.generate_password(16)}@cache-server:6379/0",
        ]
        return random.choice(db_types)()

    @staticmethod
    def generate_credential_pair():
        """Generate a username:password pair in various formats"""
        formats = [
            lambda: f"user: {FakeDataGenerator.generate_username()}\npass: {FakeDataGenerator.generate_password()}",
            lambda: f"username: {FakeDataGenerator.generate_email()}\npassword: {FakeDataGenerator.generate_password()}",
            lambda: f"login: {FakeDataGenerator.generate_username()} | password: {FakeDataGenerator.generate_password()}",
            lambda: f"email: {FakeDataGenerator.generate_email()}\npasswd: {FakeDataGenerator.generate_password()}",
            lambda: f"User={FakeDataGenerator.generate_username()};Password={FakeDataGenerator.generate_password()}",
            lambda: f"{FakeDataGenerator.generate_email()}:{FakeDataGenerator.generate_password()}",
            lambda: f"LOGIN={FakeDataGenerator.generate_username()}\nPASSWORD={FakeDataGenerator.generate_password()}\nDOMAIN=corporate.local",
        ]
        return random.choice(formats)()


class KeyloggerFooler:
    """Main class to fool keyloggers and data catchers"""

    def __init__(self, output_dir="./fake_data"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.generator = FakeDataGenerator()

        if KEYBOARD_AVAILABLE:
            self.keyboard = KeyboardController()

    def simulate_typing(self, text, delay_range=(0.05, 0.15)):
        """Simulate typing to fool keyloggers"""
        if not KEYBOARD_AVAILABLE:
            print(f"[KEYBOARD] {text}")
            return

        print(f"[TYPING] {text}")
        for char in text:
            self.keyboard.type(char)
            time.sleep(random.uniform(*delay_range))
        time.sleep(0.3)

    def write_to_file(self, filename, content):
        """Write fake data to a file"""
        filepath = self.output_dir / filename
        with open(filepath, 'a') as f:
            f.write(content + "\n")
        print(f"[FILE] Written to {filepath}")

    def copy_to_clipboard(self, text):
        """Copy fake data to clipboard"""
        if not CLIPBOARD_AVAILABLE:
            print(f"[CLIPBOARD] {text}")
            return

        pyperclip.copy(text)
        print(f"[CLIPBOARD] Copied: {text}")

    def generate_fake_credentials(self):
        """Generate and output fake credentials"""
        print("\n--- Generating Fake Credentials ---")

        # Type credentials
        creds = self.generator.generate_credential_pair()
        self.simulate_typing(creds)

        # Write to file
        self.write_to_file("credentials.txt", creds)

        # Copy to clipboard
        email = self.generator.generate_email()
        password = self.generator.generate_password()
        self.copy_to_clipboard(f"{email}:{password}")

    def generate_fake_crypto(self):
        """Generate and output fake crypto data"""
        print("\n--- Generating Fake Crypto Data ---")

        crypto_type = random.choice(['eth', 'btc', 'altcoin', 'seed'])

        if crypto_type == 'eth':
            # Ethereum data
            eth_address = self.generator.generate_eth_address()
            private_key = self.generator.generate_private_key()
            eth_data = f"ETH Address: {eth_address}\nPrivate Key: {private_key}"
            self.simulate_typing(eth_data)
            self.write_to_file("crypto_wallets.txt", eth_data)
            self.copy_to_clipboard(private_key)

        elif crypto_type == 'btc':
            # Bitcoin data
            btc_address = self.generator.generate_btc_address()
            private_key = self.generator.generate_private_key()
            btc_data = f"BTC Address: {btc_address}\nWIF Private Key: {private_key}"
            self.simulate_typing(btc_data)
            self.write_to_file("crypto_wallets.txt", btc_data)
            self.copy_to_clipboard(btc_address)

        elif crypto_type == 'altcoin':
            # Other cryptocurrency
            crypto_name, address = self.generator.generate_other_crypto_address()
            private_key = self.generator.generate_private_key()
            altcoin_data = f"{crypto_name} Address: {address}\nPrivate Key: {private_key}"
            self.simulate_typing(altcoin_data)
            self.write_to_file("crypto_wallets.txt", altcoin_data)
            self.copy_to_clipboard(address)

        else:
            # Seed phrase
            seed_phrase = self.generator.generate_seed_phrase()
            seed_data = f"Seed Phrase ({len(seed_phrase.split())} words):\n{seed_phrase}"
            self.simulate_typing(seed_data)
            self.write_to_file("seed_phrases.txt", seed_phrase)
            self.copy_to_clipboard(seed_phrase)

    def generate_fake_api_keys(self):
        """Generate and output fake API keys with realistic service-specific formats"""
        print("\n--- Generating Fake API Keys ---")

        # All available services with specific key formats
        services = [
            # AI Services
            "OpenAI", "Anthropic Claude", "Google AI (Gemini)", "Hugging Face", "Cohere", "Replicate",
            # Cloud Services
            "AWS", "AWS Secret", "Google Cloud", "Azure", "DigitalOcean", "Heroku",
            # Payment Services
            "Stripe", "PayPal",
            # Communication Services
            "Twilio", "SendGrid", "Mailgun",
            # Development Services
            "GitHub", "GitLab", "npm", "Docker Hub",
            # Database Services
            "MongoDB Atlas", "Supabase", "Firebase",
            # Analytics & Monitoring
            "Google Analytics", "Datadog", "New Relic",
            # Social Media APIs
            "Twitter/X", "Facebook", "Discord Bot",
            # Maps & Location
            "Google Maps", "Mapbox",
        ]

        service = random.choice(services)
        api_key = self.generator.generate_api_key_for_service(service)
        api_data = f"{service} API Key: {api_key}"
        self.simulate_typing(api_data)
        self.write_to_file("api_keys.txt", api_data)
        self.copy_to_clipboard(api_key)

    def generate_fake_ssh_keys(self):
        """Generate and output fake SSH keys"""
        print("\n--- Generating Fake SSH Keys ---")

        ssh_key = self.generator.generate_ssh_key()
        self.simulate_typing(ssh_key)
        self.write_to_file("ssh_keys.txt", ssh_key)
        self.copy_to_clipboard(ssh_key)

    def generate_fake_credit_cards(self):
        """Generate and output fake credit card data"""
        print("\n--- Generating Fake Credit Card Data ---")

        card_data = self.generator.generate_credit_card()
        self.simulate_typing(card_data)
        self.write_to_file("payment_methods.txt", card_data)
        # Copy just the card number
        card_line = card_data.split('\n')[0].replace('Card: ', '')
        self.copy_to_clipboard(card_line)

    def generate_fake_database_connections(self):
        """Generate and output fake database connection strings"""
        print("\n--- Generating Fake Database Connections ---")

        db_conn = self.generator.generate_database_connection()
        self.simulate_typing(f"Database Connection:\n{db_conn}")
        self.write_to_file("database_configs.txt", db_conn)
        self.copy_to_clipboard(db_conn)

    def run_continuous(self, interval=10, iterations=None):
        """Run continuously generating fake data"""
        print(f"\n{'='*50}")
        print("KEYLOGGER FOOLER - CONTINUOUS MODE")
        print(f"{'='*50}")

        if KEYBOARD_AVAILABLE:
            print("\n" + "!"*50)
            print("⚠️  WARNING: KEYBOARD SIMULATION IS ACTIVE!")
            print("⚠️  STAY IN THIS TERMINAL WINDOW AT ALL TIMES!")
            print("⚠️  Switching windows may cause random keystrokes")
            print("⚠️  to interfere with other applications!")
            print("!"*50 + "\n")

        print(f"Interval: {interval} seconds")
        print(f"Output directory: {self.output_dir.absolute()}")
        print(f"Press Ctrl+C to stop\n")

        count = 0
        try:
            while iterations is None or count < iterations:
                count += 1
                print(f"\n[Iteration {count}]")

                # Randomly choose what type of fake data to generate
                actions = [
                    self.generate_fake_credentials,
                    self.generate_fake_crypto,
                    self.generate_fake_api_keys,
                    self.generate_fake_ssh_keys,
                    self.generate_fake_credit_cards,
                    self.generate_fake_database_connections,
                ]

                action = random.choice(actions)
                action()

                if iterations is None or count < iterations:
                    print(f"\nWaiting {interval} seconds before next iteration...")
                    time.sleep(interval)

        except KeyboardInterrupt:
            print("\n\nStopped by user.")
            print(f"Generated {count} iterations of fake data.")


def main():
    """Main entry point"""
    print("""
╔═══════════════════════════════════════════════════════════╗
║           KEYLOGGER FOOLER - Defensive Tool               ║
║                                                           ║
║  Generates fake sensitive data to confuse:               ║
║  • Keyloggers                                            ║
║  • File searchers                                        ║
║  • Clipboard catchers                                    ║
╚═══════════════════════════════════════════════════════════╝
    """)

    # Parse simple arguments
    interval = 10
    iterations = None

    if len(sys.argv) > 1:
        try:
            interval = int(sys.argv[1])
        except ValueError:
            print("Usage: python keylogger_fooler.py [interval_seconds] [iterations]")
            sys.exit(1)

    if len(sys.argv) > 2:
        try:
            iterations = int(sys.argv[2])
        except ValueError:
            print("Usage: python keylogger_fooler.py [interval_seconds] [iterations]")
            sys.exit(1)

    fooler = KeyloggerFooler()
    fooler.run_continuous(interval=interval, iterations=iterations)


if __name__ == "__main__":
    main()
