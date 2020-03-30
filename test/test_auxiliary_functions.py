import sys
sys.path.append('../src')
from auxiliary_functions import numToAscii, generateChecksum
import unittest

class TestAuxiliaryFunctions(unittest.TestCase):
    def testNumToAscii(self):
        numbersToTest = [0, 1, 3, 6, 10, 20, 50, 65, 100, 130, 181, 192, 200, 212, 233, 255, 256, 300]
        stringRepresentations = ['00', '01', '03', '06', '0A', '14', '32', '41', '64', '82',
                'B5', 'C0', 'C8', 'D4', 'E9', 'FF', '00', '2C']
        byteRepresentationsDesired = [bytearray(x, encoding='ascii') for x in stringRepresentations]
        for i in range(len(numbersToTest)):
            byteRepresentationActual = numToAscii(numbersToTest[i])
            byteRepresentationDesired = byteRepresentationsDesired[i]
            self.assertEqual(byteRepresentationActual, byteRepresentationDesired)

    def testGenerateChecksum(self):
        bytearraysToTest = [bytearray(x, encoding='ascii') for x in ['\x1b\x30', '\x1b\x51']]
        actualChecksums = [generateChecksum(x) for x in bytearraysToTest]
        desiredChecksums = [bytearray(x, encoding='ascii') for x in ['4B', '6C']]
        for i in range(len(actualChecksums)):
            self.assertEqual(actualChecksums[i], desiredChecksums[i])


if __name__ == '__main__':
    unittest.main()
