def hex2(numberInHex):
    return int(numberInHex, 0)

class Device:
    def __init__(self):
        self.commandCodes = {}
        self.measuredDataCodes = {}
        self.realtimeDataCodes = {}
        self.alarmLimits = {}

        # NOTE - 
        # In all cases, I have just compressed the short description of the alarm into camel notation, replacing
        # 'O2' with 'oxygen' and '>' with 'over' and '<' with under. Anytime there is an (Alarm) (Advisory)
        # or other thing in parentheses I have just appended that as a word.
        self.alarms = {
                'airwayPressureOverHighLimit': {
                    'code': None,
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
                    },
                'tachyapneaAlarmDisabled': {
                    'code': None,
                    'priority': None,
                    'phrase': None,
                    'description': None
                    },
                'volumeAlarmDisabled': {
                    'code': None,
                    'priority': None,
                    'phrase': None,
                    'description': None
                    },
                'respiratoryRateOverHighLimit': {
                    'code': None,
                    'priority': None,
                    'phrase': None,
                    'description': None
                    },
                'apnoeDetectedByEvita': {
                    'code': None,
                    'priority': None,
                    'phrase': None,
                    'description': None
                    },
                'minuteVolumeOverHighLimit': {
                    'code': None,
                    'priority': None,
                    'phrase': None,
                    'description': None
                    },
                'volumeMeasurementInoperableAlarm': {
                    'code': None,
                    'priority': None,
                    'phrase': None,
                    'description': None
                    },
                'minuteVolumeAlarmDisabled': {
                    'code': None,
                    'priority': None,
                    'phrase': None,
                    'description': None
                    },
                'pressureMeasurementInoperable': {
                    'code': None,
                    'priority': None,
                    'phrase': None,
                    'description': None
                    },
                'airwayTemperatureMeasurementInoperable': {
                    'code': None,
                    'priority': None,
                    'phrase': None,
                    'description': None
                    },
                'checkAirwayTemperatureSensor': {
                    'code': None,
                    'priority': None,
                    'phrase': None,
                    'description': None
                    },
                'airwayTemperatureOverHighLimit': {
                    'code': None,
                    'priority': None,
                    'phrase': None,
                    'description': None
                    },
                'communicationErrorRS232Port': {
                    'code': None,
                    'priority': None,
                    'phrase': None,
                    'description': None
                    },
                'internalCommunicationError': {
                    'code': None,
                    'priority': None,
                    'phrase': None,
                    'description': None
                    },
                'inspiredOxygenUnderLowerLimitAlarm': {
                    'code': None,
                    'priority': None,
                    'phrase': None,
                    'description': None
                    },
                'percentOxygenAboveHigherLimitCaution': {
                    'code': None,
                    'priority': None,
                    'phrase': None,
                    'description': None
                    },
                'inspiratoryOxygenMeasurementInoperableAlarm': {
                    'code': None,
                    'priority': None,
                    'phrase': None,
                    'description': None
                    },
                'oxygenMeasurementInoperableAdvisory': {
                    'code': None,
                    'priority': None,
                    'phrase': None,
                    'description': None
                    },
                'inspiratoryOxygenOverHighLimitAdvisory': {
                    'code': None,
                    'priority': None,
                    'phrase': None,
                    'description': None
                    },
                'inspiratoryOxygenUnderLowLimitAdvisory': {
                    'code': None,
                    'priority': None,
                    'phrase': None,
                    'description': None
                    },
                'checkAirSupply': {
                    'code': None,
                    'priority': None,
                    'phrase': None,
                    'description': None
                    },
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


        # MIGHT NEED TO ADD FORMAT TO THE SETTINGS AND WANT TO ADD UNITS
        self.settings = {
                "FiO2": None,
                "maxInspiratoryFlow": None,
                "maxInspiratoryPressure": None,
                "tidalVolume": None,
                "SIMVFrequency": None,
                "IPPVFrequency": None,
                "PEEP": None,
                "BIPAPLowPressure": None,
                "BIPAPHighPressure": None,
                "BIPAPLowTime": None,
                "BIPAPHighTime": None,
                "apneaTime": None,
                "tachyapneaFrequency": None,
                "tachyapneaDuration": None
        }
