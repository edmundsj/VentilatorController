import unittest
from unittest.mock import Mock
import sys
sys.path.append('../src')
from medibus_interface import MedibusInterface

# Runs tests assuming that the serial port has already been opened - we mock the 
# read and write functions of the port accordingly.
class TestMedibusOpenPort(unittest.TestCase):

    def testGenerateCommandNOP(self):
        actualCommand  = self.medibus.generateCommand('NOP')
        desiredCommand = self.NOPCommand
        self.assertEqual(desiredCommand, actualCommand, msg='generate nop')

    def testGenerateCommandInitializeCommunication(self):
        actualCommand = self.medibus.generateCommand('initializeCommunication')
        desiredCommand = self.initializeCommunicationCommand
        self.assertEqual(desiredCommand, actualCommand, msg='generate initialize communication')

    def testGenerateCommandStopCommunication(self):
        actualCommand = self.medibus.generateCommand('stopCommunication')
        desiredCommand = self.stopCommunicationCommand
        self.assertEqual(desiredCommand, actualCommand, msg='generate stop communication')

    def testGenerateCommandUnrecognized(self):
        # assert than an exception is raised if we get an unrecognized string
        with self.assertRaises(KeyError):
            command = self.medibus.generateCommand('blob')


    def setUp(self):
        def serialWriteReturnValue(writeArguments):
            return len(writeArguments)

        self.medibus = MedibusInterface()
        self.medibus.serialPort.write = Mock(spec=[], side_effect=serialWriteReturnValue)
        self.commandBegin = bytearray('\x1b', encoding='ascii')
        self.commandEnd = bytearray('\x0d', encoding='ascii')

        self.NOPCode = bytearray('\x30', encoding='ascii')
        self.NOPChecksum = NotImplementedError
        self.NOPCommand = self.commandBegin + self.NOPCode + self.NOPChecksum + self.commandEnd

        self.initializeCommunicationCode = bytearray('\x51', encoding='ascii')
        self.stopCommunicationCode = bytearray('\x55', encoding='ascii')

        # TEMPORARY - MOCK THE CLASS FUNCTIONS TO FAIL THE TESTS
        self.medibus.writeCommand = Mock(spec=[], side_effect=NotImplementedError)
        self.medibus.generateCommand = Mock(spec=[], side_effect=NotImplementedError)


if __name__ == '__main__':
    unittest.main()
