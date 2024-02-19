def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():  # Cek apakah karakter adalah huruf
            # Proses untuk huruf kapital
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            # Proses untuk huruf kecil
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Tambahkan karakter asli jika bukan huruf
            result += char
    return result

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)

# Contoh penggunaan
text = "Hello World!"
shift = 3

encrypted_text = encrypt(text, shift)
print("Encrypted Text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted Text:", decrypted_text)