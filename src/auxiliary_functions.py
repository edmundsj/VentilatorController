import numpy as np

def numToAscii(number):
    remainder = number % 256
    firstHexadecimal = int(np.floor(remainder / 16))
    secondHexadecimal = remainder % 16
    firstCharacter = hex(firstHexadecimal).upper()[-1]
    secondCharacter = hex(secondHexadecimal).upper()[-1]
    return bytearray(firstCharacter, encoding='ascii') + bytearray(secondCharacter, encoding='ascii')

def generateChecksum(myByteArray):
    checksum = 0
    for elem in myByteArray:
        checksum += elem

    checksum = checksum % 256
    return numToAscii(checksum)

def asciiBytes(myString):
    return bytearray(myString, encoding='ascii')
