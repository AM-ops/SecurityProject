#Cryptography Project for ITRI615
# J&A's Cryptography Project
import math
import random as r

#Formatting files
#for any type of file :D
def fileToByteString(file):
    byteStream =[]
    f = open(file, 'rb')
    fileData = f.read()
    fileData = bytearray(fileData)

    for item in fileData:
        byteStream.append(item)

    f.close()
    return byteStream

def byteStringToFile(byteStream,file):
    pathStr = str(file)
    f = open(file, 'wb')
    byteStream = bytearray(byteStream)
    f.write(byteStream)
    f.close()
    return pathStr

#Transposition
def keyCheck(key):
    check = True
    for item in key:
        if(not(ord(item) >= 48 and ord(item) <= 57)):
            check = False
    if(check):
        return int(key)
    else:
        return len(key)

#String to Matrix function
def StrToMatrix_TEXT(text,key):
    matrix = []
    row = []
    count = 0
    length = len(text)
    for item in text:
        row.append(item)
        count = count + 1
        length = length - 1
        if(count == key):
            matrix.append(row)
            row = []
            count = 0
        elif(length == 0):
            while(len(row)<key):
                row.append("")
            matrix.append(row)
    return matrix

def StrToMatrix_FILE(text,key):
    matrix = []
    row = []
    count = 0
    length = len(text)
    for item in text:
        row.append(item)
        count += 1
        length -= 1
        if(count == key):
            matrix.append(row)
            row = []
            count = 0
        elif(length == 0):
            while(len(row)<key):
                row.append(item)
            matrix.append(row)
    return matrix

#Text algoritms
def Transposition_TEXT_Encryption(message, key):
    key = keyCheck(key)
    matrix = StrToMatrix_TEXT(message, key)
    encryptedMessage = ""
    for j in range(0,key):
        for item in matrix:
            strList = str(item.pop(0))
            encryptedMessage = encryptedMessage+strList
    return encryptedMessage

def Transposition_TEXT_Decryption(encryptedMessage, key):
    key = keyCheck(key)
    numberColumns = math.ceil(len(encryptedMessage) / key)
    numberRows = key
    numberBlanks = (numberColumns * numberRows) - len(encryptedMessage)
    decryptedMessage = ['']*numberColumns
    col,row = 0,0

    for item in encryptedMessage:
        decryptedMessage[col] += item
        col += 1
        if (col == numberColumns) or (col == numberColumns - 1 and row >= numberRows - numberBlanks):
            col = 0
            row += 1
    return ''.join(decryptedMessage)

'''
print(Transposition_TEXT_Encryption("The brown fox has eyes seeing an infinite amount of stars","5"))
print(Transposition_TEXT_Decryption(Transposition_TEXT_Encryption("The brown fox has eyes seeing an infinite amount of stars","5"),"5"))
'''
def Transposition_FILE_Encryption(message, key):
    key = keyCheck(key)
    matrix = StrToMatrix_FILE(message, key)
    encryptedMessage = []
    origLength = str(len(message))
    lenLen = len(origLength)
    encryptedMessage.append(lenLen)
    for i in range(0,lenLen):
        encryptedMessage.append(ord(origLength[i]))


    for j in range(0,key):
        for item in matrix:
            strList = item.pop(0)
            encryptedMessage.append(strList)
    return encryptedMessage

def Transposition_FILE_Decryption(message,key):
    key = keyCheck(key)

    lenLen = message.pop(0)
    origLengthARR = []
    for i in range(0,lenLen):
        strList = message.pop(0)
        origLengthARR.append(str(chr(strList)))
    origLengthSTR = ''.join(origLengthARR)
    origLength = int(origLengthSTR)

    numberColumns = math.ceil(len(message) / key)
    numberRows = key
    numberBlanks = (numberColumns * numberRows) - origLength
    matrix = StrToMatrix_FILE(message, numberColumns)
    decryptedMessageARR = []

    for j in range(0,numberColumns):
        for item in matrix:
            strList = item.pop(0)
            decryptedMessageARR.append(strList)

    for i in range(0,numberBlanks):
        decryptedMessageARR.pop(-1)

    returnMessage =[]
    for item in decryptedMessageARR:
        returnMessage.append(int(item))

    returnMessage = bytearray(returnMessage)

    return returnMessage
'''
plainInput = fileToByteString("file.jpg")
encrypt = Transposition_FILE_Encryption(plainInput,"100")
byteStringToFile(encrypt,"tran_encrypt.jpg")
cipherInput = fileToByteString("tran_encrypt.jpg")
decrypt = Transposition_FILE_Decryption(cipherInput,"100")
byteStringToFile(decrypt,"tran_decrypt.jpg")
'''

#Vignere
#Set Up Vigenere Table
'''
VignereTable = []*26
alphabet  = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

addRow = []
for i in range(0,26):
    for j in range(0,26):
        k = i+j
        if k >= 26:
            k -= 26
        addRow.append(alphabet[k])
    VignereTable.append(addRow)
    addRow = []
'''
#Fixes key length to match size of message
def extendKeyLength(messageLength,key):
    keyLength = len(key)
    newKey = list(key)
    if messageLength == keyLength:
        return(key)

    else:
        for i in range(0,(messageLength - keyLength)):
            newKey.append(key[i % keyLength])
        return ("".join(newKey)).upper()

#Text algorithms
def Vigenere_TEXT_Encryption(message, key):
    message = message.upper()
    messageLength = len(message)
    encryptedMessage = []
    key = extendKeyLength(messageLength, key)
    for i in range(0,messageLength):
        if ord(message[i]) < 65 or ord(message[i]) > 90:
            encryptedMessage.append(message[i])
        else:
            newEncrypted = ord(message[i]) + ord(key[i])
            newEncrypted = newEncrypted % 26
            newEncrypted += ord('A') #gets ascii values back to "letters area"
            encryptedMessage.append(chr(newEncrypted))

    return "".join(encryptedMessage)

def Vigenere_TEXT_Decryption(encryptedMessage, key):
    decryptedMessage = []
    messageLength = len(encryptedMessage)
    key = extendKeyLength(messageLength, key)
    for i in range(0,messageLength):
        if ord(encryptedMessage[i]) < 65 or ord(encryptedMessage[i]) > 90:
            decryptedMessage.append(encryptedMessage[i])
        else:
            newDecrypted = (ord(encryptedMessage[i]) - ord(key[i])) % 26
            newDecrypted += ord('A')
            decryptedMessage.append(chr(newDecrypted))

    return "".join(decryptedMessage)

#File algortitms
def Vigenere_FILE_Encryption(message, key):
    messageLength = len(message)
    encryptedMessage = []
    key = extendKeyLength(messageLength, key)
    for i in range(0,messageLength):
            newEncrypted = ((message[i]) + ord(key[i])) % 256
            encryptedMessage.append(newEncrypted)

    return encryptedMessage

def Vigenere_FILE_Decryption(message, key):
    messageLength = len(message)
    decryptedMessage = []
    key = extendKeyLength(messageLength, key)
    for i in range(0,messageLength):
        newDecrypted = (message[i] - ord(key[i])) % 256
        decryptedMessage.append(newDecrypted)

    return decryptedMessage

#Vernam
#Key generators
def vernam_Key_Generator(messageLength):
    key = []
    for i in range(0,messageLength):
        char = chr(r.randrange(65,91))
        key.append(char)
    return ("".join(key)).upper()

def vernam_Key_Generator_FILE(messageLength):
    key = []
    for i in range(0,messageLength):
        char = chr(r.randrange(0,256))
        key.append(ord(char))
    return key

#Text algorithms
def Vernam_TEXT_Encryption(message):
    messageStrip = message.replace(" ","")
    messageStrip = messageStrip.upper()
    messageLength = len(messageStrip)
    key = vernam_Key_Generator(messageLength)
    encryptedMessage = "" + key
    encryptedMessage = list(encryptedMessage)
    for i in range(0,messageLength):
        newEncrypted = (ord(messageStrip[i]) + ord(key[i])) % 26
        newEncrypted += 65
        encryptedMessage.append(chr(newEncrypted))
    return "".join(encryptedMessage)

def Vernam_TEXT_Decryption(message):
    messageLength = int(len(message)/2)
    key = []
    baseMessage = []
    decryptedMessage = []

    for i in range(0,messageLength):
        key.append(message[i])
        baseMessage.append(message[(i+messageLength)])

    for j in range(0,messageLength):
        newDecrypted = (ord(baseMessage[j]) - ord(key[j])) % 26
        newDecrypted += 65
        decryptedMessage.append(chr(newDecrypted))

    return "".join(decryptedMessage)

#File algorithms
def Vernam_FILE_Encryption(message):
    messageLength = len(message)
    key = vernam_Key_Generator_FILE(messageLength)
    baseMessage = []
    encryptedMessage = []
    for j in key:
        encryptedMessage.append(j)
    for i in range(0,messageLength):
        newEncrypted = (message[i] + key[i]) % 256
        baseMessage.append(newEncrypted)


    encryptedMessage = [key,baseMessage]
    returnMessage = []
    for item in encryptedMessage:
        for thing in item:
            returnMessage.append(thing)

    return returnMessage

def Vernam_FILE_Decryption(message):
    messageLength = int(len(message)/2)
    key = []
    baseMessage = []
    decryptedMessage = []

    for i in range(0,messageLength):
        key.append(message[i])
        baseMessage.append(message[(i+messageLength)])

    for j in range(0,messageLength):
        newDecrypted = (baseMessage[j] - key[j]) % 256
        decryptedMessage.append(newDecrypted)

    return decryptedMessage

#Own algorithm
def own_TEXT_Encryption(message, key):
    key = keyCheck(key)
    messageLength = len(message)
    numericEncryptedValues = []
    for item in message:
        numeric = ord((item))
        mathPart = (((key*numeric)) - key)
        numericEncryptedValues.append(mathPart)

    randomKey = []
    for i in range(0,messageLength):
        num = r.randrange(32,256)
        randomKey.append(chr(num))

    encryptedMessage = []
    for i in range(0,messageLength):
        encryptedMessage.append(chr((numericEncryptedValues[i]+ord(randomKey[i]))))

    addedKey = ''.join(randomKey)
    strEncryptedMessage = ''.join(encryptedMessage)

    return (addedKey+strEncryptedMessage)

def own_TEXT_Decryption(message, key):
    key = keyCheck(key)
    messageLength = int(len(message)/2)
    encryptedMessage = []
    randomKey = []

    for i in range(0,messageLength):
        encryptedMessage.append(ord(message[i+messageLength]))
        randomKey.append(ord(message[i]))

    partA = []
    for j in range(0,messageLength):
        partA.append(chr((encryptedMessage[j]-randomKey[j])))

    decryptedMessage = []
    for item in partA:
        numeric = ord(item)
        unMathPart = ((numeric+key)/key)
        decryptedMessage.append(chr(int(unMathPart)))

    return ''.join(decryptedMessage)

def own_FILE_Encryption(message, key):
    key = keyCheck(key)
    messageLength = len(message)
    numericEncryptedValues = []
    for item in message:
        mathPart = (item - key)
        numericEncryptedValues.append(mathPart)

    randomKey = []
    for i in range(0,messageLength):
        num = r.randrange(0,256)
        randomKey.append(num)

    combined = []
    for i in range(0,messageLength):
        combined.append((numericEncryptedValues[i]+randomKey[i])%256)

    encryptedMessage = [randomKey,combined]
    returnMessage = []
    for item in encryptedMessage:
        for thing in item:
            returnMessage.append(thing)

    return returnMessage

def own_FILE_Decryption(message, key):
    key = keyCheck(key)
    messageLength = int(len(message)/2)
    encryptedMessage = []
    randomKey = []

    for i in range(0,messageLength):
        encryptedMessage.append(message[i+messageLength])
        randomKey.append(message[i])

    partA = []
    for j in range(0,messageLength):
        partA.append((encryptedMessage[j]-randomKey[j]))

    decryptedMessage = []
    for item in partA:
        unMathPart = (item+key)
        decryptedMessage.append(unMathPart%256)

    return decryptedMessage


'''
Example of implementation of file functions/methods:

Encryption:
plainData = fileToByteString("file/file path Origional")
cipherData = FILE_Encryption(fileData,key) - key depends on which method
byteStringToFile(cipherData,"file/file path Encrypted")

Decryption:
cipherData = fileToByteString("file/file path Encrypted")
plainData = FILE_Decryption(fileData,key) - key depends on which method
byteStringToFile(plainData,"file/file path Decrypted")
'''

'''''''''''''''''''''''''''
plainText = "The brown fox has eyes seeing an infinite amount of stars"
cipherText = Transposition_TEXT_Encryption(plainText,"hello")
print(cipherText)
decryptedText = Transposition_TEXT_Decryption(cipherText,5)
print(decryptedText)


plainInput = fileToByteString("file.mp3")
encrypt = Vigenere_FILE_Encryption(plainInput,"appayipyip")
byteStringToFile(encrypt,"vig_encrypt.mp3")
cipherInput = fileToByteString("vig_encrypt.mp3")
decrypt = Vigenere_FILE_Decryption(cipherInput,"appayipyip")
byteStringToFile(decrypt,"vig_decrypt.mp3")

plainInput = fileToByteString("file.png")
encrypt = Vernam_FILE_Encryption(plainInput)
byteStringToFile(encrypt,"ver_encrypt.png")
cipherInput = fileToByteString("ver_encrypt.png")
decrypt = Vernam_FILE_Decryption(cipherInput)
byteStringToFile(decrypt,"ver_decrypt.png")

plainInput = fileToByteString("file.jpg")
encrypt = own_FILE_Encryption(plainInput,20)
byteStringToFile(encrypt,"own_encrypt.jpg")
cipherInput = fileToByteString("own_encrypt.jpg")
decrypt = own_FILE_Decryption(cipherInput,20)
byteStringToFile(decrypt,"own_decrypt.jpg")

'''''''''''''''''''''''''''
