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
    f = open(file, 'wb')
    byteStream = bytearray(byteStream)
    f.write(byteStream)
    f.close()
    return

#Transposition
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
                row.append(ord("\u0000"))
            matrix.append(row)

    return matrix

#Text algoritms
def Transposition_TEXT_Encryption(message, key):
    matrix = StrToMatrix_TEXT(message, key)
    encryptedMessage = ""
    for j in range(0,key):
        for item in matrix:
            strList = str(item.pop(0))
            encryptedMessage = encryptedMessage+strList
    return encryptedMessage

def Transposition_TEXT_Decryption(encryptedMessage, key):
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

def Transposition_FILE_Encryption(message, key):

    f = open("UN-encryptedData.txt", 'wb')
    f.write( bytearray(message))
    f.close()

    matrix = StrToMatrix_FILE(message, key)
    encryptedMessage = []
    for j in range(0,key):
        for item in matrix:
            strList = item.pop(0)
            encryptedMessage.append(strList)

    f = open("encryptedData.txt", 'wb')
    f.write( bytearray(encryptedMessage))
    f.close()

    return encryptedMessage

def Transposition_FILE_Decryption(message,key):
    numberRows = math.ceil(len(message) / key)
    numberColumns = key
    numberBlanks = (numberColumns * numberRows) - len(message)
    decryptedMessage = ['']*numberColumns
    col,row = 0,0

    for item in message:
        decryptedMessage[col] += str(item)
        col += 1
        if (col == numberColumns) or (col == numberColumns - 1 and row >= numberRows - numberBlanks):
            col = 0
            row += 1

    return ''.join(decryptedMessage)

'''
input = fileToByteString("file.mp3")
encrypt = Transposition_FILE_Encryption(input,20)

for i in range(0,x):
    print(input[i*20],"and",encrypt[i])
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
        print(len(newKey))
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
    messageStrip = message.replace(" "," ")
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
    messageLength = len(message)
    numericEncryptedValues = []
    for item in message:
        numeric = ord((item))
        mathPart = (((key*numeric)) - key)
        numericEncryptedValues.append(mathPart)

    randomKey = []
    for i in range(0,messageLength):
        num = r.randrange(0,256)
        randomKey.append(chr(num))

    encryptedMessage = []
    for i in range(0,messageLength):
        encryptedMessage.append(chr((numericEncryptedValues[i]+ord(randomKey[i]))))

    addedKey = ''.join(randomKey)
    strEncryptedMessage = ''.join(encryptedMessage)

    return (addedKey+strEncryptedMessage)

def own_TEXT_Decryption(message, key):
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
