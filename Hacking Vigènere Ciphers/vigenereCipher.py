# Vigenere Cipher (Polyalphabetic Substitution Cipher)
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # String yang berisi semua huruf alfabet dalam huruf besar.

def main():
    myMessage = """Muhammad Zabbar Falihin is a student in the Department of Computational Statistics, where he is dedicated to mastering the intersection of statistics, computer science, and data analysis."""
    myKey = 'ZABBAR'
    myMode = 'encrypt'

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    print('%sed message:' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('Pesannya telah disalin ke clipboard.')


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = [] # List untuk menyimpan pesan yang telah dienkripsi atau didekripsi.

    keyIndex = 0
    key = key.upper() # Ubah key menjadi huruf besar.

    for symbol in message:
        num = LETTERS.find(symbol.upper()) # Temukan posisi huruf dalam LETTERS.
        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex]) # Tambahkan jika mode adalah 'encrypt'
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex]) # Kurangkan jika mode adalah 'decrypt'

            num %= len(LETTERS) # Operasi modulo dengan len(LETTERS) digunakan untuk memastikan hasilnya tetap dalam rentang alfabet (misalnya, jika hasilnya melebihi panjang alfabet, ia akan "dibalikkan" kembali ke awal alfabet).

            if symbol.isupper():
                translated.append(LETTERS[num]) # Tambahkan huruf yang telah dienkripsi atau didekripsi ke dalam list translated.
            elif symbol.islower():
                translated.append(LETTERS[num].lower()) # Tambahkan huruf yang telah dienkripsi atau didekripsi ke dalam list translated.

            keyIndex += 1 # Pindah ke huruf berikutnya dalam key.
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol) # Tambahkan simbol yang bukan huruf ke dalam list translated.

    return ''.join(translated)

if __name__ == '__main__':
    main()