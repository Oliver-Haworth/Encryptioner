# --- Imports ---
import os

# --- Functions ---

class Encrypt():

    def caesar_cipher(self, message, shift):
        ''' Encrypts a message using the Caesar Cipher algorithm'''
        print(f'Encrypting message using Caesar Cipher with shift {shift}.')
        encrypted_message = ''
        for char in message:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
                encrypted_message += encrypted_char
            else:
                encrypted_message += char
        return encrypted_message

    def custom_algorithm(self, message, key=None):
        """Encrypts a message using an improved XOR-based algorithm (educational only)."""
        print(' ######### WARNING ######### ')
        print('This is a custom algorithm built for educational purposes only.')
        print('DO NOT EXPECT THIS TO BE SECURE OR SAFE TO USE IN ANY WAY, SHAPE, OR FORM\n')

        use_specific_key = input('do you want to use a specific key? (y/n): ')
        if use_specific_key.lower() == 'y':
            key_hex = input('Enter the key in hexadecimal format: ')
            key = bytes.fromhex(key_hex)
        else:
            key = os.urandom(32)  # increased key size

        iv = os.urandom(16)  # random initialization vector
        message_bytes = message.encode('utf-8')
        encrypted_bytes = bytearray()

        prev = iv[0]
        for i, b in enumerate(message_bytes):
            c = b ^ key[i % len(key)] ^ prev  # XOR with key + feedback
            # rotate left
            c = ((c << (i % 8)) & 0xFF) | (c >> (8 - (i % 8)))
            encrypted_bytes.append(c)
            prev = c

        encrypted_message = iv.hex() + encrypted_bytes.hex()
        return encrypted_message, key


class Decrypt():

    def caesar_cipher(self, message, shift):
        ''' Decrypts a message using the Caesar Cipher algorithm'''
        print(f'Decrypting message using Caesar Cipher with shift {shift}.')
        decrypted_message = ''
        for char in message:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
                decrypted_message += decrypted_char
            else:
                decrypted_message += char
        return decrypted_message

    def custom_algorithm(self, encrypted_message, key):
        """Decrypts a message using the improved XOR-based algorithm"""
        if key is None:
            raise ValueError("Key must be provided for decryption!")

        print(' ######### WARNING ######### ')
        print('This is a custom algorithm built for educational purposes only.')
        print('DO NOT EXPECT THIS TO BE SECURE OR SAFE TO USE IN ANY WAY, SHAPE, OR FORM\n')

        iv_hex = encrypted_message[:32]  # first 16 bytes = IV
        ciphertext_hex = encrypted_message[32:]
        iv = bytes.fromhex(iv_hex)
        encrypted_bytes = bytes.fromhex(ciphertext_hex)

        decrypted_bytes = bytearray()
        prev = iv[0]
        for i, c in enumerate(encrypted_bytes):
            # rotate right
            rotated = ((c >> (i % 8)) | ((c << (8 - (i % 8)) & 0xFF))) & 0xFF
            b = rotated ^ key[i % len(key)] ^ prev
            decrypted_bytes.append(b)
            prev = c  # feedback uses original encrypted byte

        return decrypted_bytes.decode('utf-8')
