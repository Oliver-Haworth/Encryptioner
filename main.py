# --- main.py ---


# --- Imports ---
from encryption import Encrypt

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


def EncryptAlgorithmChoice():
    ''' Display the encryption algorithm choices to the user'''

    print('Choose an encryption algorithm:')
    print('1. Caesar Cipher')

    algo_choice = int(input('Enter your choice (1-3): '))

    translate = {
        1: 'caesar cipher',

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


def main():
    while True:
        task = menu()
        if task == 'encrypt':
            EncryptRouter(EncryptAlgorithmChoice())
        else:
            print('Nope not allowed to do that yet')


main()