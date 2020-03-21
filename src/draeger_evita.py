from devices import Device
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
            'code': ,
            'priority': None,
            'phrase': None,
            'description': None
            },
        'minuteVolumeUnderLowLimit': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            },
        'volumeNotConstant': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'tachyapneaAlarmDisabled': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'respiratoryRateOverHighLimit': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'apnoeDetectedByEvita': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'minuteVolumeOverHighLimit': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'volumeMeasurementInoperableAlarm': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'minuteVolumeAlarmDisabled': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'pressureMeasurementInoperable': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'airwayTemperatureMeasurementInoperable': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'checkAirwayTemperatureSensor': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'airwayTemperatureOverHighLimit': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'communicationErrorRS232Port': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'internalCommunicationError': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'inspiredOxygenUnderLowerLimitAlarm': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'percentOxygenAboveHigherLimitCaution': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'inspiratoryOxygenMeasurementInoperableAlarm': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'oxygenMeasurementInoperableAdvisory': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'inspiratoryOxygenOverHighLimitAdvisory': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'inspiratoryOxygenUnderLowLimitAdvisory': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'checkAirSupply': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'assistedSpontaneousBreathingOver4Seconds': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            },
        'disconnectionVentilator': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'problemsWithRespiratorEvita': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'checkExpirationValve': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'tooHighRespiratorDeviceTemperatureAlarm': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'sighModeActive': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'breathingSystemVented': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'checkOxygenSupplyAdvisory': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'gasMixerInoperableAdvisory': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'timeLimitedRespiratoryVolume': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'pressureLimitedRespiratoryVolume': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'highRespiratorDeviceTemperatureAdvisory': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'respiratorSynchronizationInoperable': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'failToCycle': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        'gasMixerInoperableAlarm': {
            'code': None,
            'priority': None,
            'phrase': None,
            'description': None
            }
        }
