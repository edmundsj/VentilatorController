import serial

class MedibusInterface:
    def __init__(self, port=None, baudrate=19200, timeout=10):
        self.readBuffer = ''
        self.serialPort = serial.Serial(port=port, baudrate=baudrate)

     # If I had to guess, registers 0x2A through 0x49 are where the write
     # registers are located for the settings.
    commandLookupTable = {
        'NOP': {
                'code': '0x30',
                'description': 'Do nothing (NOP)'
                },
        'initializeCommunication': {
                'code': '0x51',
                'description': 'Initialize Communication (ICC)'
                },
        'requestDeviceIdentification': {
                'code': '0x52',
                'description': 'Request Device Identification'
                },
        'requestCurrentData': {
                'code': '0x24',
                'description': 'Request current DATA'
                },
        'requestCurrentLowAlarmLimits': {
                'code': '0x25',
                'description': 'Request current LOW ALARM LIMITS'
                },
        'requestCurrentHighAlarmLimits': {
                'code': '0x26',
                'description': 'Request current HIGH ALARM LIMITS'
                },
        'requestCurrentAlarms': {
                'code': '0x27',
                'description': 'Request current ALARMS'
                },
        # If I had to guess, registers 0x2A through 0x49 are where the write
        # registers are located for the settings.
        'requestCurrentDeviceSettings': {
                'code': '0x29',
                'description': 'Request current DEVICE SETTINGS'
                },
        'configureDataResponse': {
                'code': '0x4A',
                'description': 'Configure Data Response'
                },
        'requestRealtimeConfiguration': {
                'code': '0x53',
                'description': 'Request Realtime Configuration'
                },
        'configureRealtimeTransmission': {
                'code': '0x54',
                'description': 'Configure Realtime Transmission'
                },
        'stopCommunication': {
                'code': '0x55',
                'description': 'Stop Communication'
                },
        'deviceSpecific': {
                'code': '0x6A',
                'description': 'Device Specific'
                }
        }
