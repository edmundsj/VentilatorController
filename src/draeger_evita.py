from device import Device
evita = Device()

evita.settings = {
    "FiO2": '0x01',
    "maxInspiratoryFlow": '0x02',
    "maxInspiratoryPressure": '0x13',
    "tidalVolume": '0x04',
    "SIMVFrequency": '0x09',
    "IPPVFrequency": '0x0A',
    "PEEP": '0x0B',
    "BIPAPLowPressure": '0x0D',
    "BIPAPHighPressure": '0x0E',
    "BIPAPLowTime": '0x0F',
    "BIPAPHighTime": '0x10',
    "apneaTime": '0x11',
    "tachyapneaFrequency": '0x16',
    "tachyapneaDuration": '0x17'
}
evita.alarms = {
        'airwayPressureOverHighLimit': {
            'code': '0x10',
            'priority': 27,
            'phrase': 'PAW HIGH',
            'description': 'Airway Pressure > high Limit'
            },
        'minuteVolumeUnderLowLimit': {
            'code': '0x19',
            'priority': 26,
            'phrase': 'MIN VOL LOW',
            'description': 'Minute Volume < low Limit'
            },
        'volumeNotConstant': {
            'code': '0x33',
            'priority': [26, 3],
            'phrase': 'VOL INCONST',
            'description': 'Volume not constant'
            },
        'tachyapneaAlarmDisabled': {
            'code': '0x40',
            'priority': 1,
            'phrase': 'TACHYPN\'@OFF',
            'description': 'Tachyapnear Alarm disabled'
            },
        'volumeAlarmDisabled': {
            'code': '0x5E',
            'priority': 1,
            'phrase': 'VOL ALRM OFF',
            'description': 'Volume Alarm disabled'
            },
        'respiratoryRateOverHighLimit': {
            'code': '0x90',
            'priority': 26,
            'phrase': 'RESP RATE HI',
            'description': 'Respiratory Rate > high Limit'
            },
        'apnoeDetectedByEvita': {
            'code': '0x98',
            'priority': [27, 8],
            'phrase': 'APNEA EVITA',
            'description': 'Apnoe detected by Evita'
            },
        'minuteVolumeOverHighLimit': {
            'code': '0x9B',
            'priority': 26,
            'phrase': 'MIN VOL HIGH',
            'description': 'Minute Volume > high Limit'
            },
        'volumeMeasurementInoperableAlarm': {
            'code': '0xA4',
            'priority': [27,8],
            'phrase': 'VOL ERR',
            'description': 'Volume Measurement inoperable (Alarm)'
            },
        'minuteVolumeAlarmDisabled': {
            'code': '0xAC',
            'priority': 1,
            'phrase': 'MV ALRM OFF',
            'description': 'MIN VOL Alarm disabled'
            },
        'pressureMeasurementInoperable': {
            'code': '0xAD',
            'priority': 27,
            'phrase': 'PRESS ERR',
            'description': 'Pressure Measurement inoperable'
            },
        'airwayTemperatureMeasurementInoperable': {
            'code': '0xB8',
            'priority': 25,
            'phrase': 'AW-TEMP INOP',
            'description': 'Airway Temperature Measurement inoperable'
            },
        'checkAirwayTemperatureSensor': {
            'code': '0xB9',
            'priority': 25,
            'phrase': 'AW-TEMP SENS',
            'description': 'Check Airway Temperature Sensor'
            },
        'airwayTemperatureOverHighLimit': {
            'code': '0xBA',
            'priority': 25,
            'phrase': 'AW-TEMP HIGH',
            'description': 'Airway Temperature > high Limit'
            },
        'communicationErrorRS232Port': {
            'code': '0x78',
            'priority': 1,
            'phrase': 'RS232 COM ERR',
            'description': 'Communication Error RS232 Port'
            },
        'internalCommunicationError': {
            'code': '0x7C',
            'priority': 1,
            'phrase': 'INT COM ERR',
            'description': 'Internal Communication Error'
            },
        'inspiredOxygenUnderLowerLimitAlarm': {
            'code': '0x08',
            'priority': 26,
            'phrase': '% O2 LOW',
            'description': 'Insp. Oxygen < low Limit (Alarm)'
            },
        'percentOxygenAboveHigherLimitCaution': {
            'code': '0x37',
            'priority': 23,
            'phrase': '% O2 HIGH',
            'description': '% Oxygen > high Limit (Caution)'
            },
        'inspiratoryOxygenMeasurementInoperableAlarm': {
            'code': '0xA1',
            'priority': 28,
            'phrase': '% O2 ERR',
            'description': 'Insp O2 Measurement inoperable (Alarm)'
            },
        'oxygenMeasurementInoperableAdvisory': {
            'code': '0xBE',
            'priority': 8,
            'phrase': '% O2 ERR',
            'description': 'O2 Measurement inoperable (Advisory)'
            },
        'inspiratoryOxygenOverHighLimitAdvisory': {
            'code': '0xBF',
            'priority': 7,
            'phrase': '% O2 HIGH',
            'description': 'Insp O2 > high Limit (Advisory)'
            },
        'inspiratoryOxygenUnderLowLimitAdvisory': {
            'code': '0xC0',
            'priority': 7,
            'phrase': '% O2 LOW',
            'description': 'Insp O2 < low Limit (Advisory)'
            },
        'checkAirSupply': {
            'code': '0x12',
            'priority': [31, 2],
            'phrase': 'AIR SUPPLY ?',
            'description': 'Check Air Supply'
            },
        'assistedSpontaneousBreathingOver4Seconds': {
            'code': '0x3A',
            'priority': 26,
            'phrase': 'ASB > 4 SEC',
            'description': 'Assisted Spontaneous Breathing > 4 sec.'
            },
        'disconnectionVentilator': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            },
        'problemsWithRespiratorEvita': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            },
        'checkExpirationValve': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            },
        'tooHighRespiratorDeviceTemperatureAlarm': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            },
        'sighModeActive': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            },
        'breathingSystemVented': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            },
        'checkOxygenSupplyAdvisory': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            },
        'gasMixerInoperableAdvisory': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            },
        'timeLimitedRespiratoryVolume': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            },
        'pressureLimitedRespiratoryVolume': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            },
        'highRespiratorDeviceTemperatureAdvisory': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            },
        'respiratorSynchronizationInoperable': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            },
        'failToCycle': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            },
        'gasMixerInoperableAlarm': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        }
