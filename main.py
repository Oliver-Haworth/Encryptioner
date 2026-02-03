# --- main.py ---


# --- Imports ---
from encrypt_decrypt import Encrypt
from encrypt_decrypt import Decrypt

# --- Functions ---


def menu():
    ''' Display the main menu to the user'''

    print('Welcome, What would you like to do?')
    print('1. encryipt a message')
    print('2. decrypt a message')
    print('3. exit')

    menu_choice = int(input('Enter your choice (1-3): '))

    translate = {
        1: 'encrypt',
        2: 'decrypt',
        3: 'exit'
    }

    menu_choice = translate.get(menu_choice)

    return menu_choice


def AlgorithmChoice():
    ''' presents the encryption algorithm choices to the user'''

    print('Choose an encryption algorithm:')
    print('1. Caesar Cipher')
    print('2. Custom Algorithm (XOR-based, educational only)')

    algo_choice = int(input('Enter your choice (1-3): '))

    translate = {
        1: 'caesar cipher',
        2: 'custom algorithm',

    }

    algo_choice = translate.get(algo_choice)

    return algo_choice


def EncryptRouter(algo_choice):
    ''' Direct user to wanted encryption algorithm'''

    if algo_choice == 'caesar cipher':

        message = input('Enter the message to encrypt: ')
        shift = int(input('Enter the shift value: '))
        print (f'algorithm: {algo_choice}, \nmessage: {message}, \nshift: {shift}')

        encrypted_message = Encrypt().caesar_cipher(message, shift)
        print('')
        print(f'Encrypted message: {encrypted_message}')
        print('')

    elif algo_choice == 'custom algorithm':
        message = input('Enter the message to encrypt: ')
        encrypted_message, key = Encrypt().custom_algorithm(message)
        print(f'Encrypted message: {encrypted_message}')
        print(f'Private key (keep this safe!): {key.hex()}')



def DecryptRouter(algo_choice):
    ''' Direct user to wanted decryption algorithm'''

    if algo_choice == 'caesar cipher':

        message = input('Enter the message to decrypt: ')
        shift = int(input('Enter the shift value: '))
        print (f'algorithm: {algo_choice}, \nmessage: {message}, \nshift: {shift}')

        decrypted_message = Decrypt().caesar_cipher(message, shift)
        print('')
        print(f'Decrypted message: {decrypted_message}')
        print('')
    
    elif algo_choice == 'custom algorithm':
        message = input('Enter the message to decrypt: ')
        key_hex = input('Enter the private key used for encryption (hex): ')
        key = bytes.fromhex(key_hex)

        decrypted_message = Decrypt().custom_algorithm(message, key)
        print(f'Decrypted message: {decrypted_message}')



def main():
    ''' main function to run the program '''

    while True:
        task = menu()

        if task == 'encrypt':
            EncryptRouter(AlgorithmChoice())

        elif task == 'decrypt':
            DecryptRouter(AlgorithmChoice())

        else:
            quit()


if __name__ == "__main__":
    main()