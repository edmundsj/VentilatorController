import serial
from auxiliary_functions import asciiBytes, numToAscii
import numpy as np


class MedibusInterface:
    def __init__(self, port=None, baudrate=19200, timeout=10):
        self.readBuffer = ''
        self.serialPort = serial.Serial(port=port, baudrate=baudrate)

    @staticmethod
    def generateChecksum(myByteArray):
        checksum = 0
        for elem in myByteArray:
            checksum += elem

        checksum = checksum % 256
        return numToAscii(checksum)


    def generateCommand(self, commandString):
        beginCommand = asciiBytes('\x1b')
        commandCode = self.commandLookupTable[commandString]['code']
        print("command code")
        print(commandCode)
        commandChecksum = self.generateChecksum(beginCommand + commandCode)
        endCommand = asciiBytes('\r')
        fullCommand = beginCommand + commandCode + commandChecksum + endCommand
        return fullCommand

    commandLookupTable = {
        'NOP': {
                'code': asciiBytes('\x30'),
                'description': 'Do nothing (NOP)'
                },
        'initializeCommunication': {
                'code': asciiBytes('\x51'),
                'description': 'Initialize Communication (ICC)'
                },
        'requestDeviceIdentification': {
                'code': asciiBytes('\x52'),
                'description': 'Request Device Identification'
                },
        'requestCurrentData': {
                'code': asciiBytes('\x24'),
                'description': 'Request current DATA'
                },
        'requestCurrentLowAlarmLimits': {
                'code': asciiBytes('\x25'),
                'description': 'Request current LOW ALARM LIMITS'
                },
        'requestCurrentHighAlarmLimits': {
                'code': asciiBytes('\x26'),
                'description': 'Request current HIGH ALARM LIMITS'
                },
        'requestCurrentAlarms': {
                'code': asciiBytes('\x27'),
                'description': 'Request current ALARMS'
                },
        'requestCurrentDeviceSettings': {
                'code': asciiBytes('\x29'),
                'description': 'Request current DEVICE SETTINGS'
                },
        'configureDataResponse': {
                'code': asciiBytes('\x4A'),
                'description': 'Configure Data Response'
                },
        'requestRealtimeConfiguration': {
                'code': asciiBytes('\x53'),
                'description': 'Request Realtime Configuration'
                },
        'configureRealtimeTransmission': {
                'code': asciiBytes('\x54'),
                'description': 'Configure Realtime Transmission'
                },
        'stopCommunication': {
                'code': asciiBytes('\x55'),
                'description': 'Stop Communication'
                },
        'deviceSpecific': {
                'code': asciiBytes('\x6A'),
                'description': 'Device Specific'
                }
        }
