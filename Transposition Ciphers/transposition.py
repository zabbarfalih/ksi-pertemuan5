def encrypt(text, num_cols):
    # Hilangkan spasi untuk kesederhanaan
    text = text.replace(" ", "").upper()
    # Inisialisasi ciphertext
    ciphertext = ""
    # Iterasi melalui setiap kolom
    for col in range(num_cols):
        idx = col
        while idx < len(text):
            ciphertext += text[idx]
            idx += num_cols
    return ciphertext

def decrypt(ciphertext, num_cols):
    # Menghitung jumlah baris yang diperlukan
    num_rows = len(ciphertext) // num_cols
    # Menangani kasus di mana ciphertext tidak memenuhi matriks secara sempurna
    if len(ciphertext) % num_cols != 0:
        num_rows += 1

    # Membuat matriks kosong untuk dekripsi
    matrix = [''] * num_cols
    
    # Menghitung jumlah karakter ekstra di baris terakhir
    extra_chars = len(ciphertext) % num_cols

    # Mengisi matriks untuk dekripsi
    idx = 0
    for col in range(num_cols):
        for row in range(num_rows):
            if row == num_rows - 1 and col >= extra_chars and extra_chars != 0:
                # Jika baris terakhir dan kolom melebihi jumlah karakter ekstra, lanjutkan
                matrix[col] += ' '
            else:
                matrix[col] += ciphertext[idx]
                idx += 1

    # Menggabungkan karakter dari matriks untuk mendapatkan plaintext
    plaintext = ''
    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[col][row] != ' ':
                plaintext += matrix[col][row]

    return plaintext

# Contoh penggunaan
text = "Muhammad Zabbar Falihin"
num_cols = 4

encrypted_text = encrypt(text, num_cols)
print("Encrypted Text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, num_cols)
print("Decrypted Text:", decrypted_text)