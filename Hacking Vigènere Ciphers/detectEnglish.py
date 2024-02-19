UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Mendefinisikan string yang berisi semua huruf alfabet dalam huruf besar. Ini digunakan untuk memeriksa keberadaan huruf dalam pesan.
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n' # Menggabungkan huruf besar, huruf kecil, dan karakter whitespace (spasi, tab, newline) untuk membuat string yang digunakan untuk memfilter pesan, sehingga hanya menyisakan karakter-karakter tersebut.

def loadDictionary():
    dictionaryFile = open('D:\\STIS\\Semester 6\\KSI\\P5\\Hacking Vigènere Ciphers\\dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary() # Memuat dictionary kata-kata bahasa Inggris yang dibaca dari file teks melalui fungsi loadDictionary().


def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()

    if possibleWords == []:
        return 0.0

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)
# Menghitung berapa persen dari kata-kata dalam message yang merupakan kata-kata bahasa Inggris yang valid berdasarkan dictionary yang telah dimuat.

def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)
# Menghilangkan semua karakter dalam pesan yang bukan huruf atau whitespace. Fungsi ini membantu dalam membersihkan pesan agar hanya tersisa karakter-karakter yang relevan untuk analisis.

def isEnglish(message, wordPercentage=20, letterPercentage=85):
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch
# Menentukan apakah sebuah pesan adalah bahasa Inggris atau tidak berdasarkan dua kriteria:
# Persentase kata dalam pesan yang ada di dalam dictionary bahasa Inggris (wordPercentage). Default-nya adalah 20%.
# Persentase karakter dalam pesan yang merupakan huruf alfabet (letterPercentage). Default-nya adalah 85%.