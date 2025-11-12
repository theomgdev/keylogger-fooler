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
        "icloud.com", "aol.com", "mail.com", "zoho.com", "yandex.com"
    ]

    @staticmethod
    def generate_password(length=None):
        """Generate a fake password"""
        if length is None:
            length = random.randint(12, 24)

        chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
        password = ''.join(random.choice(chars) for _ in range(length))
        return password

    @staticmethod
    def generate_username():
        """Generate a fake username"""
        adjectives = ["cool", "super", "mega", "ultra", "pro", "elite", "master", "dark"]
        nouns = ["user", "hacker", "coder", "gamer", "ninja", "wizard", "dragon", "phoenix"]
        numbers = str(random.randint(0, 9999))

        return random.choice(adjectives) + random.choice(nouns) + numbers

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
        # Legacy address format (starts with 1 or 3)
        prefix = random.choice(['1', '3'])
        chars = string.ascii_letters + string.digits
        address = prefix + ''.join(random.choice(chars) for _ in range(random.randint(26, 34)))
        return address

    @staticmethod
    def generate_private_key():
        """Generate a fake private key"""
        hex_chars = '0123456789abcdef'
        key = '0x' + ''.join(random.choice(hex_chars) for _ in range(64))
        return key

    @staticmethod
    def generate_seed_phrase(word_count=12):
        """Generate a fake BIP39-style seed phrase"""
        return ' '.join(random.choice(FakeDataGenerator.BIP39_WORDS) for _ in range(word_count))

    @staticmethod
    def generate_api_key():
        """Generate a fake API key"""
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))

    @staticmethod
    def generate_credential_pair():
        """Generate a username:password pair"""
        formats = [
            lambda: f"user: {FakeDataGenerator.generate_username()}\npass: {FakeDataGenerator.generate_password()}",
            lambda: f"username: {FakeDataGenerator.generate_email()}\npassword: {FakeDataGenerator.generate_password()}",
            lambda: f"login: {FakeDataGenerator.generate_username()} | password: {FakeDataGenerator.generate_password()}",
            lambda: f"email: {FakeDataGenerator.generate_email()}\npasswd: {FakeDataGenerator.generate_password()}",
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

        # Ethereum data
        eth_address = self.generator.generate_eth_address()
        private_key = self.generator.generate_private_key()

        eth_data = f"ETH Address: {eth_address}\nPrivate Key: {private_key}"
        self.simulate_typing(eth_data)
        self.write_to_file("crypto_wallets.txt", eth_data)
        self.copy_to_clipboard(private_key)

        time.sleep(0.5)

        # Bitcoin data
        btc_address = self.generator.generate_btc_address()
        btc_data = f"BTC Address: {btc_address}"
        self.simulate_typing(btc_data)
        self.write_to_file("crypto_wallets.txt", btc_data)

        time.sleep(0.5)

        # Seed phrase
        seed_phrase = self.generator.generate_seed_phrase(12)
        seed_data = f"Seed Phrase (12 words):\n{seed_phrase}"
        self.simulate_typing(seed_data)
        self.write_to_file("seed_phrases.txt", seed_phrase)
        self.copy_to_clipboard(seed_phrase)

    def generate_fake_api_keys(self):
        """Generate and output fake API keys"""
        print("\n--- Generating Fake API Keys ---")

        services = ["AWS", "Google Cloud", "Stripe", "OpenAI", "GitHub"]

        for service in random.sample(services, 2):
            api_key = self.generator.generate_api_key()
            api_data = f"{service} API Key: {api_key}"
            self.simulate_typing(api_data)
            self.write_to_file("api_keys.txt", api_data)
            self.copy_to_clipboard(api_key)
            time.sleep(0.3)

    def run_continuous(self, interval=10, iterations=None):
        """Run continuously generating fake data"""
        print(f"\n{'='*50}")
        print("KEYLOGGER FOOLER - CONTINUOUS MODE")
        print(f"{'='*50}")
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
