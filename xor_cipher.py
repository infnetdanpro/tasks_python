#https://pythonworld.ru/osnovy/tasks.html №8

import random as r

def random_key():
    return r.randint(0, 10000)

def XOR_cipher(text, key):
    crypt = ""
    for i in text:
        try:
            crypt += chr(ord(i)^ord(key))
        except TypeError:
            crypt += chr(ord(i)^key)
    return crypt


def XOR_uncipher(s_xor, key):
    decrypt = ""
    for i in s_xor:
        try:
            decrypt += chr(ord(i)^ord(key))
        except:
            decrypt += chr(ord(i)^key)
    return decrypt
    

if __name__ == '__main__':
    key = random_key()

    encrypt_string = XOR_cipher(input('Введите строку для шифрования: '), key)
    decrypt_string = XOR_uncipher(encrypt_string, key)

    print(encrypt_string)
    print(decrypt_string)