# --- encryption.py ---


# --- Imports ---


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