import unittest
from unittest.mock import Mock
import sys
sys.path.append('../src')
from medibus_interface import MedibusInterface
from auxiliary_functions import generateChecksum
from auxiliary_functions import asciiBytes

# Runs tests assuming that the serial port has already been opened - we mock the 
# read and write functions of the port accordingly.
class TestMedibusOpenPort(unittest.TestCase):

    def testGenerateChecksum(self):
        bytearraysToTest = [bytearray(x, encoding='ascii') for x in ['\x1b\x30', '\x1b\x51']]
        actualChecksums = [MedibusInterface.generateChecksum(x) for x in bytearraysToTest]
        desiredChecksums = [bytearray(x, encoding='ascii') for x in ['4B', '6C']]
        for i in range(len(actualChecksums)):
            self.assertEqual(desiredChecksums[i], actualChecksums[i])

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

    def testRequestDeviceIdentification(self):
        actualCommand = self.medibus.generateCommand('requestDeviceIdentification')
        desiredCommand = self.requestDeviceIdentificationCommand
        self.assertEqual(desiredCommand, actualCommand, msg='generate request device identification')

    def testGenerateCommandRequestCurrentData(self):
        actualCommand = self.medibus.generateCommand('requestCurrentData')
        desiredCommand = self.requestCurrentDataCommand
        self.assertEqual(desiredCommand, actualCommand, msg='generate request current data')

    def testGenerateCommandRequestCurrentLowAlarmLimits(self):
        actualCommand = self.medibus.generateCommand('requestCurrentLowAlarmLimits')
        desiredCommand = self.requestCurrentLowAlarmLimitsCommand
        self.assertEqual(desiredCommand, actualCommand, msg='generate request current low alarms')

    def testGenerateRequestCurrentHighAlarmLimits(self):
        actualCommand = self.medibus.generateCommand('requestCurrentHighAlarmLimits')
        desiredCommand = self.requestCurrentHighAlarmLimitsCommand
        self.assertEqual(desiredCommand, actualCommand, msg='generate request current high alarms')

    def testGenerateRequestCurrentAlarms(self):
        actualCommand = self.medibus.generateCommand('requestCurrentAlarms')
        desiredCommand = self.requestCurrentAlarmsCommand
        self.assertEqual(desiredCommand, actualCommand, msg='generate request current alarms')

    def testGenerateRequestCurrentDeviceSettings(self):
        actualCommand = self.medibus.generateCommand('requestCurrentDeviceSettings')
        desiredCommand = self.requestCurrentDeviceSettingsCommand
        self.assertEqual(desiredCommand, actualCommand, msg='generate request current device settings')

    def testConfigureDataResponse(self):
        actualCommand = self.medibus.generateCommand('configureDataResponse')
        desiredCommand = self.configureDataResponseCommand
        self.assertEqual(desiredCommand, actualCommand, msg='generate configure data response')

    def requestRealtimeConfiguration(self):
        actualCommand = self.medibus.generateCommand('requestRealtimeConfiguration')
        desiredCommand = self.requestRealtimeConfigurationCommand
        self.assertEqual(desiredCommand, actualCommand, msg='generate request realtime configuration')

    def configureRealtimeTransmission(self):
        actualCommand = self.medibus.generateCommand('configureRealtimeTransmission')
        desiredCommand = self.configureRealtimeTransmissionCommand
        self.assertEqual(desiredCommand, actualCommand, msg='generate configure realtime transmission')

    def testGenerateDeviceSpecific(self):
        actualCommand = self.medibus.generateCommand('deviceSpecific')
        desiredCommand = self.deviceSpecificCommand
        self.assertEqual(desiredCommand, actualCommand, msg='generate device specific')

    def testGenerateCommandUnrecognized(self):
        with self.assertRaises(KeyError):
            command = self.medibus.generateCommand('blob')

    @classmethod
    def setUpClass(self):
        def serialWriteReturnValue(writeArguments):
            return len(writeArguments)

        self.medibus = MedibusInterface()
        self.medibus.serialPort.write = Mock(spec=[], side_effect=serialWriteReturnValue)

        self.commandBegin = bytearray('\x1b', encoding='ascii')
        self.commandEnd = bytearray('\x0d', encoding='ascii')

        self.NOPCode = bytearray('\x30', encoding='ascii')
        self.NOPChecksum = asciiBytes('4B')
        self.NOPCommand = asciiBytes('\x1b04B\r')

        self.initializeCommunicationCode = bytearray('\x51', encoding='ascii')
        self.initializeCommunicationChecksum = asciiBytes('6C')
        self.initializeCommunicationCommand = asciiBytes('\x1bQ6C\r')

        self.requestDeviceIdentificationCode = bytearray('\x52', encoding='ascii')
        self.requestDeviceIdentificationChecksum = asciiBytes('6D')
        self.requestDeviceIdentificationCommand = asciiBytes('\x1bR6D\r')

        self.requestCurrentDataCode = bytearray('\x24', encoding='ascii')
        self.requestCurrentDataChecksum = asciiBytes('3F')
        self.requestCurrentDataCommand = asciiBytes('\x1b$3F\r')

        self.requestCurrentLowAlarmLimitsCode = bytearray('\x25', encoding='ascii')
        self.requestCurrentLowAlarmLimitsChecksum = asciiBytes('40')
        self.requestCurrentLowAlarmLimitsCommand = asciiBytes('\x1b%40\r')

        self.requestCurrentHighAlarmLimitsCode = bytearray('\x26', encoding='ascii')
        self.requestCurrentHighAlarmLimitsChecksum = asciiBytes('41')
        self.requestCurrentHighAlarmLimitsCommand = asciiBytes('\x1b&41\r')

        self.requestCurrentAlarmsCode = bytearray('\x27', encoding='ascii')
        self.requestCurrentAlarmsChecksum = asciiBytes('42')
        self.requestCurrentAlarmsCommand = asciiBytes("\x1b\'42\r")

        self.requestCurrentDeviceSettingsCode = bytearray('\x29', encoding='ascii')
        self.requestCurrentDeviceSettingsChecksum = asciiBytes('44')
        self.requestCurrentDeviceSettingsCommand = asciiBytes('\x1b)44\r')

        self.requestCurrentTextMessagesCode = bytearray('\x2A', encoding='ascii')
        self.requestCurrentTextMessagesChecksum = asciiBytes('45')
        self.requestCurrentTextMessagesCommand = asciiBytes('\x1b*45\r')

        self.configureDataResponseCode = bytearray('\x4A', encoding='ascii')
        self.configureDataResponseChecksum = asciiBytes('65')
        self.configureDataResponseCommand = asciiBytes('\x1bJ65\r')

        self.requestRealtimeConfigurationCode = bytearray('\x53', encoding='ascii')
        self.requestRealtimeConfigurationChecksum = asciiBytes('6E')
        self.requestRealtimeConfigurationCommand = asciiBytes('\x1bS6E\r')

        self.configureRealtimeTransmissionCode = bytearray('\x54', encoding='ascii')
        self.configureRealtimeTransmissionChecksum = asciiBytes('6F')
        self.configureRealtimeTransmissionCommand = asciiBytes('\x1bT6F\r')

        self.stopCommunicationCode = bytearray('\x55', encoding='ascii')
        self.stopCommunicationChecksum = asciiBytes('70')
        self.stopCommunicationCommand = asciiBytes('\x1bU70\r')

        self.deviceSpecificCode = bytearray('\x6A', encoding='ascii')
        self.deviceSpecificChecksum = asciiBytes('85')
        self.deviceSpecificCommand = asciiBytes('\x1bj85\r')

        # TEMPORARY - MOCK THE CLASS FUNCTIONS TO FAIL THE TESTS
        self.medibus.writeCommand = Mock(spec=[], side_effect=NotImplementedError)
        #self.medibus.generateCommand = Mock(spec=[], side_effect=NotImplementedError)


if __name__ == '__main__':
    unittest.main()
