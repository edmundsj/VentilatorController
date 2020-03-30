import unittest
from unittest.mock import Mock
import sys
sys.path.append('../src')
from medibus_interface import MedibusInterface
from auxiliary_functions import generateChecksum

# Runs tests assuming that the serial port has already been opened - we mock the 
# read and write functions of the port accordingly.
class TestMedibusOpenPort(unittest.TestCase):

    #def testGenerateCommandNOP(self):
        #actualCommand  = self.medibus.generateCommand('NOP')
        #desiredCommand = self.NOPCommand
        #self.assertEqual(desiredCommand, actualCommand, msg='generate nop')

    def testGenerateCommandInitializeCommunication(self):
        actualCommand = self.medibus.generateCommand('initializeCommunication')
        desiredCommand = self.initializeCommunicationCommand
        self.assertEqual(desiredCommand, actualCommand, msg='generate initialize communication')

    def testGenerateCommandStopCommunication(self):
        actualCommand = self.medibus.generateCommand('stopCommunication')
        desiredCommand = self.stopCommunicationCommand
        self.assertEqual(desiredCommand, actualCommand, msg='generate stop communication')

    def testGenerateCommandRequestCurrentData(self):
        actualCommand = self.medibus.generateCommand('requestCurrentData')
        desiredCommand = self.requestCurrentDataCommand
        self.assertEqual(desiredCommand, actualCommand, msg='generate request current data')

    def testGenerateCommandUnrecognized(self):
        # assert than an exception is raised if we get an unrecognized string
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
        self.NOPChecksum = generateChecksum(self.NOPCode + self.commandBegin)
        #print(self.NOPChecksum)
        self.NOPCommand = self.commandBegin + self.NOPCode + self.NOPChecksum + self.commandEnd

        self.initializeCommunicationCode = bytearray('\x51', encoding='ascii')
        self.initializeCommunicationChecksum = generateChecksum(self.initializeCommunicationCode + \
                self.commandBegin)
        #print(self.initializeCommunicationChecksum)
        self.initializeCommunicationCommand = self.commandBegin + self.initializeCommunicationCode + \
                self.initializeCommunicationChecksum + self.commandEnd

        self.requestDeviceIdentificationCode = bytearray('\x52', encoding='ascii')
        self.requestDeviceIdentificationChecksum = generateChecksum(self.requestDeviceIdentificationCode + \
                self.commandBegin)
        #print(self.requestDeviceIdentificationChecksum)
        self.requestDeviceIdentificationCommand = self.commandBegin + self.requestDeviceIdentificationCode + \
                self.requestDeviceIdentificationChecksum + self.commandEnd

        self.requestCurrentDataCode = bytearray('\x24', encoding='ascii')
        self.requestCurrentDataChecksum = generateChecksum(self.requestCurrentDataCode + self.commandBegin)
        #print(self.requestCurrentDataChecksum)
        self.requestCurrentDataCommand = self.commandBegin + self.requestCurrentDataCode + \
                self.requestCurrentDataChecksum + self.commandEnd

        self.requestCurrentLowAlarmLimitsCode = bytearray('\x25', encoding='ascii')
        self.requestCurrentLowAlarmLimitsChecksum = generateChecksum(self.requestCurrentLowAlarmLimitsCode + \
                self.commandBegin)
        #print(self.requestCurrentLowAlarmLimitsChecksum)
        self.requestCurrentLowAlarmLimitsCommand = self.commandBegin + self.requestCurrentLowAlarmLimitsCode + \
                self.requestCurrentLowAlarmLimitsChecksum + self.commandEnd

        self.requestCurrentHighAlarmLimitsCode = bytearray('\x26', encoding='ascii')
        self.requestCurrentHighAlarmLimitsChecksum = generateChecksum(self.requestCurrentHighAlarmLimitsCode + \
                self.commandBegin)
        self.requestCurrentHighAlarmLimitsCommand = self.commandBegin + self.requestCurrentHighAlarmLimitsCode + \
                self.requestCurrentHighAlarmLimitsChecksum + self.commandEnd

        self.requestCurrentAlarmsCode = bytearray('\x27', encoding='ascii')
        self.requestCurrentAlarmsChecksum = generateChecksum(self.requestCurrentAlarmsCode + self.commandBegin)
        self.requestCurrentAlarmsCommand = self.commandBegin + self.requestCurrentAlarmsCode + \
                self.requestCurrentAlarmsChecksum + self.commandEnd

        self.requestCurrentDeviceSettingsCode = bytearray('\x29', encoding='ascii')
        self.requestCurrentDeviceSettingsChecksum = generateChecksum(self.requestCurrentDeviceSettingsCode + \
                self.commandBegin)
        self.requestCurrentDeviceSettingsCommand = self.commandBegin + self.requestCurrentDeviceSettingsCode + \
                self.requestCurrentDeviceSettingsChecksum + self.commandEnd

        self.requestCurrentTextMessagesCode = bytearray('\x2A', encoding='ascii')
        self.requestCurrentTextMessagesChecksum = generateChecksum(self.requestCurrentTextMessagesCode + \
                self.commandBegin)
        self.requestCurrentTextMessagesCommand = self.commandBegin + self.requestCurrentTextMessagesCode + \
                self.requestCurrentTextMessagesChecksum + self.commandEnd

        self.configureDataResponseCode = bytearray('\x4A', encoding='ascii')
        self.configureDataResponseChecksum = generateChecksum(self.configureDataResponseCode + self.commandBegin)
        self.configureDataResponseCommand = self.commandBegin + self.configureDataResponseCode + \
                self.configureDataResponseChecksum + self.commandEnd

        self.requestRealtimeConfigurationCode = bytearray('\x53', encoding='ascii')
        self.requestRealtimeConfigurationChecksum = generateChecksum(self.requestRealtimeConfigurationCode + \
                self.commandBegin)
        self.requestRealtimeConfigurationCommand = self.commandBegin + self.requestRealtimeConfigurationCode + \
                self.requestRealtimeConfigurationChecksum + self.commandEnd

        self.configureRealtimeTransmissionCode = bytearray('\x54', encoding='ascii')
        self.configureRealtimeTransmissionChecksum = generateChecksum(self.configureRealtimeTransmissionCode + \
                self.commandBegin)
        self.configureRealtimeTransmissionCommand = self.commandBegin + self.configureRealtimeTransmissionCode + \
                self.configureRealtimeTransmissionChecksum + self.commandEnd

        self.stopCommunicationCode = bytearray('\x55', encoding='ascii')
        self.stopCommunicationChecksum = generateChecksum(self.stopCommunicationCode + self.commandBegin)
        self.stopCommunicationCommand = self.commandBegin + self.stopCommunicationCode + \
                self.stopCommunicationChecksum + self.commandEnd

        self.deviceSpecificCode = bytearray('\x6A', encoding='ascii')
        self.deviceSpecificChecksum = generateChecksum(self.deviceSpecificCode + self.commandBegin)
        self.deviceSpecificCommand = self.commandBegin + self.deviceSpecificCode + \
                self.deviceSpecificChecksum + self.commandEnd

        # TEMPORARY - MOCK THE CLASS FUNCTIONS TO FAIL THE TESTS
        self.medibus.writeCommand = Mock(spec=[], side_effect=NotImplementedError)
        self.medibus.generateCommand = Mock(spec=[], side_effect=NotImplementedError)


if __name__ == '__main__':
    unittest.main()
