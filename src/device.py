def hex2(numberInHex):
    return int(numberInHex, 0)

# The intent of the length of this class is so it can be copy-pasted to define a particular instance of that class
# The reason I used dictionaries rather than some standard YAML-type storage format for all this information
# is because they are easy to handle and write down and can easily be transitioned into that type of
# data format (or any other) if we so desire.
class Device:
    def __init__(self):
        # NOTE - 
        # In all cases, I have just compressed the short description of the alarm into camel notation, replacing
        # 'O2' with 'oxygen' and '>' with 'over' and '<' with under. Anytime there is an (Alarm) (Advisory)
        # or other thing in parentheses I have just appended that as a word.
        self.commands = {}
        self.alarms = {}
        self.alarmLimitsRead = {}
        self.alarmLimitsWrite = {} # THIS IS NOT CURRENTLY KNOWN
        self.settingsRead= {}
        self.settingsWrite= {} # THIS IS NOT CURRENTLY KNOWN
        self.measuredData = {}
        self.realtimeData = {}
        self.textMessages = {}

        self.commands = {
                'NOP': {
                        'code': None,
                        'description': None
                        }
                'initializeCommunication': {
                        'code': None,
                        'description': None
                        }
                'requestDeviceIdentification': {
                        'code': None,
                        'description': None
                        }
                'requestCurrentData': {
                        'code': None,
                        'description': None
                        }
                'requestCurrentLowAlarmLimits': {
                        'code': None,
                        'description': None
                        }
                'requestCurrentHighAlarmLimits': {
                        'code': None,
                        'description': None
                        }
                'requestCurrentAlarms': {
                        'code': None,
                        'description': None
                        }
                'requestCurrentDeviceSettings': {
                        'code': None,
                        'description': None
                        }
                'configureDataResponse': {
                        'code': None,
                        'description': None
                        }
                'requestRealtimeConfiguration': {
                        'code': None,
                        'description': None
                        }
                'configureRealtimeTransmission': {
                        'code': None,
                        'description': None
                        }
                'stopCommunication': {
                        'code': None,
                        'description': None
                        }
                'deviceSpecific': {
                        'code': None,
                        'description': None
                        }
                }

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

        self.alarmLimitsRead = {
                'peakBreathingPressureHigh': {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                'respiratoryMinuteVolumeLow': {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                'respiratoryMinuteVolumeHigh': {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                'respiratoryRatePediatricHigh': {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    }
                }

        # THIS IS UNKNOWN - THIS WILL HAVE TO BE FIGURED OUT AND CHANGED IF THE MANUFACTURER GIVES US THE DATA
        self.alarmLimitsWrite = {
                'peakBreathingPressureHigh': {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                'respiratoryMinuteVolumeLow': {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                'respiratoryMinuteVolumeHigh': {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                'respiratoryRatePediatricHigh': {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    }
                }

        self.settingsRead = {
                "FiO2": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "maximumInspiratoryFlow": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "maximumInspiratoryPressure": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "inspiredTidalVolume": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "frequencyIMVSIMV": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "frequencyIPPV": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "PEEP": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "intermittendPEEP": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    }, # UNCLEAR IF MISSPELLING IN DRAEGER MEDIBUS ICU DOCUMENT
                "BIPAPLowPressure": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "BIPAPHighPressure": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "BIPAPLowTime": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "BIPAPHighTime": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "apneaTime": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "assistedSpontaneousBreathing": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "maximumInspiredAirwayPressure": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "triggerPressure": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "tachyapneaFrequency": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "tachyapneaDuration": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "flowTrigger": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "ASBRamp": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    }
        }

        # THIS WILL ALSO HAVE TO BE CHANGED ONCE WE GET INFO FROM THE MANUFACTURER
        self.settingsWrite = {
                "FiO2": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "maximumInspiratoryFlow": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "maximumInspiratoryPressure": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "inspiredTidalVolume": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "frequencyIMVSIMV": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "frequencyIPPV": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "PEEP": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "intermittendPEEP": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    }, # UNCLEAR IF MISSPELLING IN DRAEGER MEDIBUS ICU DOCUMENT
                "BIPAPLowPressure": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "BIPAPHighPressure": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "BIPAPLowTime": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "BIPAPHighTime": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "apneaTime": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "assistedSpontaneousBreathing": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "maximumInspiredAirwayPressure": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "triggerPressure": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "tachyapneaFrequency": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "tachyapneaDuration": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "flowTrigger": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                "ASBRamp": {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    }
        }

        self.measuredData = {
                'compliance': {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                'resistance': {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                'minimalAirwayPressure': {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                'occlusionPressure': {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                'meanBreathingPressure': {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                'plateauPressure': {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                'PEEPBreathingPressure': {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                'intrinsicPEEPBreathingPressure': {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                'peakBreathingPressure': {
                    'code': None,
                    'unit': None,
                    'format': None,
                    'description': None
                    },
                'trappedVolume': {
                        'code': None,
                        'unit': None,
                        'format': None,
                        'description': None
                        },
                'tidalVolume': {
                        'code': None,
                        'unit': None,
                        'format': None,
                        'description': None
                        },
                'spontaneousRespiratoryRate': {
                        'code': None,
                        'unit': None,
                        'format': None,
                        'description': None
                        },
                'spontaneousMinuteVolume': {
                        'code': None,
                        'unit': None,
                        'format': None,
                        'description': None
                        },
                'respiratoryMinuteVolume': {
                        'code': None,
                        'unit': None,
                        'format': None,
                        'description': None
                        },
                'airwayTemperature': {
                        'code': None,
                        'unit': None,
                        'format': None,
                        'description': None
                        },
                'respiratoryRatePediatric': {
                        'code': None,
                        'unit': None,
                        'format': None,
                        'description': None
                        }
                }

        self.realtimeData = {
                'airwayPressure': {
                        'code': None,
                        'unit': None,
                        'descriptioin': None
                        },
                'flow': {
                        'code': None,
                        'unit': None,
                        'descriptioin': None
                        },
                'respiratoryVolumeSinceInspiratoryBegin': {
                        'code': None,
                        'unit': None,
                        'descriptioin': None
                        },
                'expiratoryVolume': {
                        'code': None,
                        'unit': None,
                        'descriptioin': None
                        }
            }

        self.textMessages = {
                'modeIPPV': {
                        'code': None,
                        'message': None
                        }
                'modeIPPVAssist': {
                        'code': None,
                        'message': None
                        },
                'modeCPPV': {
                        'code': None,
                        'message': None
                        },
                'modeCPPVAssist': {
                        'code': None,
                        'message': None
                        },
                'modeSIMV': {
                        'code': None,
                        'message': None
                        },
                'modeSIMVASB': {
                        'code': None,
                        'message': None
                        },
                'modeSB': {
                        'code': None,
                        'message': None
                        },
                'modeASB': {
                        'code': None,
                        'message': None
                        },
                'modeCPAP': {
                        'code': None,
                        'message': None
                        },
                'modeCPAPASB': {
                        'code': None,
                        'message': None
                        },
                'modeMMV': {
                        'code': None,
                        'message': None
                        },
                'modeBIPAP': {
                        'code': None,
                        'message': None
                        },
                'modeSynchronizeMaster': {
                        'code': None,
                        'message': None
                        },
                'modeSynchronizeSlave': {
                        'code': None,
                        'message': None
                        },
                'modeApneaVentilation': {
                        'code': None,
                        'message': None
                        },
                'modeDS': {
                        'code': None,
                        'message': None
                        },
                'modeBIPAP-SIMV': {
                        'code': None,
                        'message': None
                        },
                'modeBIPAP-SIMVASB': {
                        'code': None,
                        'message': None
                        },
                'modeBIPAP-APRV': {
                        'code': None,
                        'message': None
                        }
                }
