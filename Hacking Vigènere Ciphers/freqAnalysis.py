ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ' # String yang berisi huruf-huruf dalam bahasa Inggris diurutkan berdasarkan frekuensi kemunculannya dalam bahasa Inggris, dari yang paling sering (E) hingga yang paling jarang (Z).
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # String yang berisi semua huruf alfabet dalam huruf besar.

def getLetterCount(message):
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1

    return letterCount
# Menghitung berapa kali setiap huruf muncul dalam message.

def getItemAtIndexZero(items):
    return items[0]


def getFrequencyOrder(message):
    letterToFreq = getLetterCount(message)

    freqToLetter = {}
    for letter in LETTERS:
        if letterToFreq[letter] not in freqToLetter:
            freqToLetter[letterToFreq[letter]] = [letter]
        else:
            freqToLetter[letterToFreq[letter]].append(letter)

    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])

    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)

    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])

    return ''.join(freqOrder)
# Menggunakan getLetterCount untuk mendapatkan jumlah kemunculan setiap huruf dalam pesan. Mengurutkan huruf dalam setiap daftar berdasarkan urutan frekuensi ETAOIN. Ini dilakukan untuk menilai seberapa dekat distribusi frekuensi huruf dalam pesan dengan distribusi frekuensi huruf dalam bahasa Inggris umumnya. Mengembalikan string yang berisi huruf-huruf diurutkan dari yang paling sering muncul ke yang paling jarang muncul berdasarkan analisis pesan.

def englishFreqMatchScore(message):
    freqOrder = getFrequencyOrder(message)

    matchScore = 0
    for commonLetter in ETAOIN[:6]:
        if commonLetter in freqOrder[:6]:
            matchScore += 1
    for uncommonLetter in ETAOIN[-6:]:
        if uncommonLetter in freqOrder[-6:]:
            matchScore += 1

    return matchScore
# Fungsi ini kemudian mengambil 6 huruf paling sering muncul dalam bahasa Inggris (ETAOIN[:6]) dan membandingkannya dengan 6 huruf paling sering muncul dalam freqOrder, yaitu urutan frekuensi huruf dalam pesan. Jika sebuah huruf dari ETAOIN[:6] ditemukan di dalam 6 huruf teratas freqOrder, maka matchScore ditingkatkan sebesar 1. Ini menandakan bahwa ada kesesuaian antara frekuensi huruf dalam pesan dengan apa yang umumnya diharapkan dalam teks bahasa Inggris.