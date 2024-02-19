import itertools, re # Digunakan untuk operasi pada iterables dan ekspresi reguler, bertujuan untuk memanipulasi teks dan pola dalam pesan terenkripsi.
import vigenereCipher, pyperclip, freqAnalysis, detectEnglish

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # String yang berisi semua huruf alfabet dalam huruf besar.
SILENT_MODE = False # Jika diatur ke True, maka program tidak akan mencetak langkah-langkah peretasan ke layar.
NUM_MOST_FREQ_LETTERS = 4 # Jumlah huruf yang paling sering muncul yang akan digunakan dalam analisis frekuensi huruf.
MAX_KEY_LENGTH = 16 # Panjang kunci maksimum yang akan dicoba saat melakukan brute force.
NONLETTERS_PATTERN = re.compile('[^A-Z]') # Ekspresi reguler yang digunakan untuk mencari karakter-karakter yang bukan huruf alfabet.


def main():
    ciphertext = """Luibmdzd Abbszr Gblzgio js r rtveees io uhv Ceqbrkleou ow Bonqukztjpnrk Subtzrtjds, ngesf hv hs efdzbaufd kn mbttvqioh tyd ioueireduifm og ttrsituitr, cpnplses tczdndf, aec dbua rmamzszr. Wjuh r oattifm fps eosrbdtzmg nfaehnhguc hntjgyss gsod bonqlvw dbuajdtt, Nuyzmnbd yzs ipnvc hjt sbhlmt ie rtbuijsidbl dndfmief, mbdhzme mfaimioh, aec dbua mhsvblzyaujoe. Git bcrcenjc anusoep hs nbrbdd cz a tnmnjtddnu uo ropmzief subtzrtjdac leuiour tp tocue sfac-vosmd gqocmedr, lfweizgjog kge qpwvq og dodouujnx so boacxzf bnu hnufrgqeu eakz au tcrke. Bt a gqobdtzue mfaimes, ie tnnujnlnutmy vwpmprvr tif lrsetu tvbhoplffift aec mfuhfcompgzds jo tyd fjflu, zinjnx so dpnkqicvtv rihoiwhcbotcx tp uhv zdwbntdmfot fe cpnplsaujoezl tuakhsujcj. Git fnudawprj hn bdaudmjb aid dsjvvm bz b clqiptikx tp vnudrtuaec pbutvqnt bnu srfodj viuiie caub, azlioh tf lalf idoaduflk dfdijhoot brree pn yhs gjnuhnht."""
    hackedMessage = hackVigenere(ciphertext)

    if hackedMessage != None:
        print('Menyalin pesan yang dipecahkan ke clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Gagal memecahkan pesan.')


def findRepeatSequencesSpacings(message):
    message = NONLETTERS_PATTERN.sub('', message.upper())
    seqSpacings = {}
    for seqLen in range(3, 6):
        for seqStart in range(len(message) - seqLen):
            seq = message[seqStart:seqStart + seqLen]

            for i in range(seqStart + seqLen, len(message) - seqLen):
                if message[i:i + seqLen] == seq:
                    if seq not in seqSpacings:
                        seqSpacings[seq] = []
                    seqSpacings[seq].append(i - seqStart)
    return seqSpacings
# Fungsi ini akan mencari urutan karakter yang berulang dalam pesan. Fungsi ini akan mengembalikan dictionary yang berisi urutan karakter yang berulang dan jarak antara kemunculan urutan karakter tersebut dalam pesan.

def getUsefulFactors(num):
    if num < 2:
        return []

    factors = []

    for i in range(2, MAX_KEY_LENGTH + 1):
        if num % i == 0:
            factors.append(i)
            otherFactor = int(num / i)
            if otherFactor < MAX_KEY_LENGTH + 1 and otherFactor != 1:
                factors.append(otherFactor)
    return list(set(factors))
# Fungsi ini akan mengembalikan faktor-faktor dari num yang lebih kecil dari MAX_KEY_LENGTH. Fungsi ini akan mengembalikan list yang berisi faktor-faktor dari num yang lebih kecil dari MAX_KEY_LENGTH.
# Menghitung faktor-faktor dari jarak antara urutan yang berulang, yang bisa menjadi indikator panjang kunci.

def getItemAtIndexOne(items):
    return items[1]


def getMostCommonFactors(seqFactors):
    factorCounts = {}
    for seq in seqFactors:
        factorList = seqFactors[seq]
        for factor in factorList:
            if factor not in factorCounts:
                factorCounts[factor] = 0
            factorCounts[factor] += 1

    factorsByCount = []
    for factor in factorCounts:
        if factor <= MAX_KEY_LENGTH:
            factorsByCount.append( (factor, factorCounts[factor]) )

    factorsByCount.sort(key=getItemAtIndexOne, reverse=True)

    return factorsByCount
# Mengidentifikasi faktor yang paling sering muncul dari jarak antara urutan yang berulang, memberikan petunjuk tentang panjang kunci yang paling mungkin.

def kasiskiExamination(ciphertext):
    repeatedSeqSpacings = findRepeatSequencesSpacings(ciphertext)

    seqFactors = {}
    for seq in repeatedSeqSpacings:
        seqFactors[seq] = []
        for spacing in repeatedSeqSpacings[seq]:
            seqFactors[seq].extend(getUsefulFactors(spacing))

    factorsByCount = getMostCommonFactors(seqFactors)

    allLikelyKeyLengths = []
    for twoIntTuple in factorsByCount:
        allLikelyKeyLengths.append(twoIntTuple[0])

    return allLikelyKeyLengths
# Fungsi ini akan memanggil findRepeatSequencesSpacings untuk menemukan urutan yang berulang dalam pesan. Fungsi ini akan memanggil getUsefulFactors untuk mendapatkan faktor-faktor dari jarak antara urutan yang berulang. Fungsi ini akan memanggil getMostCommonFactors untuk mendapatkan faktor yang paling sering muncul dalam jarak antara urutan yang berulang. Fungsi ini akan mengembalikan list yang berisi panjang kunci yang paling mungkin berdasarkan analisis jarak antara urutan yang berulang.
# Melakukan Kasiski Examination pada ciphertext untuk menentukan panjang kunci yang mungkin dengan menganalisis jarak antara urutan yang berulang.
# Kasiski Examination adalah teknik yang digunakan untuk menentukan panjang kunci dari enkripsi Vigenere. Teknik ini memanfaatkan fakta bahwa jika dua bagian dari pesan terenkripsi dienkripsi dengan kata kunci yang sama, maka jarak antara kedua bagian tersebut akan merupakan kelipatan dari panjang kunci. Dengan demikian, dengan mencari urutan yang berulang dalam pesan terenkripsi, kita bisa menentukan panjang kunci yang mungkin dengan mencari faktor-faktor dari jarak antara urutan yang berulang tersebut.

def getNthSubkeysLetters(nth, keyLength, message):

    message = NONLETTERS_PATTERN.sub('', message)

    i = nth - 1
    letters = []
    while i < len(message):
        letters.append(message[i])
        i += keyLength
    return ''.join(letters)
# Fungsi ini akan mengembalikan setiap n huruf dalam pesan, dimulai dari huruf ke-n dalam pesan. Fungsi ini akan mengembalikan string yang berisi setiap n huruf dalam pesan, dimulai dari huruf ke-n dalam pesan.

def attemptHackWithKeyLength(ciphertext, mostLikelyKeyLength):
    ciphertextUp = ciphertext.upper()

    allFreqScores = []
    for nth in range(1, mostLikelyKeyLength + 1):
        nthLetters = getNthSubkeysLetters(nth, mostLikelyKeyLength, ciphertextUp)

        freqScores = []
        for possibleKey in LETTERS:
            decryptedText = vigenereCipher.decryptMessage(possibleKey, nthLetters)
            keyAndFreqMatchTuple = (possibleKey, freqAnalysis.englishFreqMatchScore(decryptedText))
            freqScores.append(keyAndFreqMatchTuple)
        freqScores.sort(key=getItemAtIndexOne, reverse=True)

        allFreqScores.append(freqScores[:NUM_MOST_FREQ_LETTERS])

    if not SILENT_MODE:
        for i in range(len(allFreqScores)):
            print('Kemungkinan huruf kunci %s: ' % (i + 1), end='')
            for freqScore in allFreqScores[i]:
                print('%s ' % freqScore[0], end='')
            print() # Print a newline.

    for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS), repeat=mostLikelyKeyLength):
        possibleKey = ''
        for i in range(mostLikelyKeyLength):
            possibleKey += allFreqScores[i][indexes[i]][0]

        if not SILENT_MODE:
            print('Mencoba dengan kunci: %s' % (possibleKey))


        decryptedText = vigenereCipher.decryptMessage(possibleKey, ciphertextUp)

        if detectEnglish.isEnglish(decryptedText):
            origCase = []
            for i in range(len(ciphertext)):
                if ciphertext[i].isupper():
                    origCase.append(decryptedText[i].upper())
                else:
                    origCase.append(decryptedText[i].lower())
            decryptedText = ''.join(origCase)

            print('Kemungkinan peretasan enkripsi dengan kunci %s:' % (possibleKey))
            print(decryptedText[:200])
            print()
            print('Tekan D untuk selesai, atau tekan Enter untuk melanjutkan peretasan:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText

    return None
# Fungsi ini akan mencoba mendekripsi pesan dengan panjang kunci yang dihipotesiskan. Fungsi ini akan mengembalikan pesan yang telah berhasil didekripsi atau None jika pesan tidak berhasil didekripsi.

def hackVigenere(ciphertext):
    allLikelyKeyLengths = kasiskiExamination(ciphertext)
    if not SILENT_MODE:
        keyLengthStr = ''
        for keyLength in allLikelyKeyLengths:
            keyLengthStr += '%s ' % (keyLength)
        print('Hasil periksa Kasiski Examination menunjukkan kemungkinan panjang kunci: ' + keyLengthStr + '\n')
    hackedMessage = None
    for keyLength in allLikelyKeyLengths:
        if not SILENT_MODE:
            print('Mencoba peretasan dengan panjang kunci %s (%s kunci yang mungkin)...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
        hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
        if hackedMessage != None:
            break

    if hackedMessage == None:
        if not SILENT_MODE:
            print('Tidak dapat meretas pesan dengan panjang kunci yang kemungkinan. Memaksa brute force panjang kunci...')
        for keyLength in range(1, MAX_KEY_LENGTH + 1):
            if keyLength not in allLikelyKeyLengths:
                if not SILENT_MODE:
                    print('Mencoba peretasan dengan panjang kunci %s (%s kunci yang mungkin)...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
                hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
                if hackedMessage != None:
                    break
    return hackedMessage
# Fungsi ini akan memanggil kasiskiExamination untuk menentukan panjang kunci yang mungkin dengan menganalisis jarak antara urutan yang berulang. Fungsi ini akan memanggil attemptHackWithKeyLength untuk mencoba mendekripsi pesan dengan panjang kunci tertentu. Fungsi ini akan mengembalikan pesan yang telah berhasil didekripsi atau None jika pesan tidak berhasil didekripsi.

if __name__ == '__main__':
    main()