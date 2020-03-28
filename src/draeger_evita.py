evita = Device()

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
            'code': '0x9A',
            'priority': 27,
            'phrase': 'PAW LOW',
            'description': 'Disconnection Ventilator'
            },
        'problemsWithRespiratorEvita': {
            'code': '0x9F',
            'priority': 25,
            'phrase': 'EVITA ERR',
            'description': 'Problems with Respirator (Evita)'
            },
        'checkExpirationValve': {
            'code': '0xB0',
            'priority': 27,
            'phrase': 'EXP-VALVE ?',
            'description': 'Check Expiration-Valve'
            },
        'tooHighRespiratorDeviceTemperatureAlarm': {
            'code': '0xB7',
            'priority': 25,
            'phrase': 'COOLNIG INOP',
            'description': 'Too high Respiratory Device Temp. (Alarm)'
            },
        'sighModeActive': {
            'code': '0xBB',
            'priority': 2,
            'phrase': 'SIGH ON',
            'description': 'Sigh Mode active'
            },
        'breathingSystemVented': {
            'code': '0xBC',
            'priority': 10,
            'phrase': 'SYSTEM OPEN',
            'description': 'Breathing System vented'
            },
        'checkOxygenSupplyAdvisory': {
            'code': '0xBD',
            'priority': [31,10],
            'phrase': 'LO O2 SUPPLY',
            'description': 'Check O2 Supply (Advisory'
            },
        'gasMixerInoperableAdvisory': {
            'code': '0xC2',
            'priority': 8,
            'phrase': 'MIXER INOP',
            'description': 'Gas Mixer inoperable (Advisory)'
            },
        'timeLimitedRespiratoryVolume': {
            'code': '0xC3',
            'priority': 7,
            'phrase': 'TIME LIMITED',
            'description': 'Time limited Respiratory Volume'
            },
        'pressureLimitedRespiratoryVolume': {
            'code': '0xC4',
            'priority': 2,
            'phrase': 'PRESSURE LTD',
            'description': 'Pressure limited Respiratory Volume'
            },
        'highRespiratorDeviceTemperatureAdvisory': {
            'code': '0xC5',
            'priority': 10,
            'phrase': 'COOLING INOP',
            'description': 'High Respirator Device Temp. (Advisory)'
            },
        'respiratorSynchronizationInoperable': {
            'code': '0xC6',
            'priority': 26,
            'phrase': 'SYNCHRO INOP',
            'description': 'Respiratory Synchronisation inoperable'
            },
        'failToCycle': {
            'code': '0xC7',
            'priority': 27,
            'phrase': 'CYCLE FAILED',
            'description': 'Fail to Cycle'
            },
        'gasMixerInoperableAlarm': {
            'code': '0xC8',
            'priority': 29,
            'phrase': 'MIXER INOP',
            'description': 'Gas Mixer inoperable (Alarm)'
            }
        }

evita.alarmLimitsRead = {
        'peakBreathingPressureHigh': {
            'code': '0x7D',
            'unit': 'mbar',
            'format': '*_XX_',
            'description': 'Peak Breathing Pressure'
            },
        'respiratoryMinuteVolumeLow': {
            'code': '0xB9',
            'unit': 'L/min',
            'format': 'XX.X',
            'description': 'Respiratory Minute Volume'
            },
        'respiratoryMinuteVolumeHigh': {
            'code': '0xB9',
            'unit': 'L/min',
            'format': 'XX.X',
            'description': 'Respiratory Minute Volume'
            },
        'respiratoryRatePediatricHigh': {
            'code': '0xD6',
            'unit': '1/min',
            'format': 'XXX_',
            'description': 'Resp. Rate (Vol./Flow)(Pediat)'
            }
        }

# THIS IS UNKNOWN - THIS WILL HAVE TO BE FIGURED OUT AND CHANGED IF THE MANUFACTURER GIVES US THE DATA
evita.alarmLimitsWrite = {
        'peakBreathingPressureHigh': {
            'code': None,
            'unit': 'mbar',
            'format': None,
            'description': None
            },
        'respiratoryMinuteVolumeLow': {
            'code': None,
            'unit': 'L/min',
            'format': None,
            'description': None
            },
        'respiratoryMinuteVolumeHigh': {
            'code': None,
            'unit': 'L/min',
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

evita.settingsRead = {
        "FiO2": {
            'code': '0x01',
            'unit': '%',
            'format': '_XXX_',
            'description': 'Insp. Oxygen'
            },
        "maximumInspiratoryFlow": {
            'code': '0x02',
            'unit': 'L/min',
            'format': 'XXX.X',
            'description': 'Max. insp. Flow'
            },
        "inspiredTidalVolume": {
            'code': '0x04',
            'unit': 'L',
            'format': 'X.XXX',
            'description': 'Insp. Tidal Volume'
            },
        'IEIPart': {
            'code': '0x07'
            'unit': None,
            'format': '_XX.X'
            'description': 'I: E I-Part'
            }
        'IEEPart': {
            'code': '0x08'
            'unit': None,
            'format': 'XXX.X'
            'description': 'I: E E-Part'
            }
        "frequencyIMVSIMV": {
            'code': '0x09',
            'unit': '1/min',
            'format': 'XXX.X',
            'description': 'Frequency IMV (SIMV)'
            },
        "frequencyIPPV": {
            'code': '0x0A',
            'unit': '1/min',
            'format': 'XXX.X',
            'description': 'Frequency IPPV'
            },
        "PEEP": {
            'code': '0x0B',
            'unit': 'mbar',
            'format': '_XX.X',
            'description': 'PEEP (CPAP)'
            },
        "intermittendPEEP": {
            'code': '0x0C',
            'unit': 'mbar',
            'format': '__XX_',
            'description': 'Intermittend PEEP'
            }, # UNCLEAR IF MISSPELLING IN DRAEGER MEDIBUS ICU DOCUMENT
        "BIPAPLowPressure": {
            'code': '0x0D',
            'unit': 'mbar',
            'format': '__XX_',
            'description': 'BIPAP low Pressure'
            },
        "BIPAPHighPressure": {
            'code': '0x0E',
            'unit': 'mbar',
            'format': '__XX_',
            'description': 'BIAP high Pressure'
            },
        "BIPAPLowTime": {
            'code': '0x0F',
            'unit': 'sec',
            'format': '_XX.X',
            'description': 'BIPAP low Time'
            },
        "BIPAPHighTime": {
            'code': '0x10',
            'unit': 'sec',
            'format': '_XX.X',
            'description': 'BIPAP high Time'
            },
        "apneaTime": {
            'code': '0x11',
            'unit': 'sec',
            'format': '__XX_',
            'description': 'Apnea Time'
            },
        "assistedSpontaneousBreathing": {
            'code': '0x12',
            'unit': 'mbar',
            'format': '__XX_',
            'description': 'Assisted spon. Breath.'
            },
        "maximumInspiredAirwayPressure": {
            'code': '0x13',
            'unit': 'mbar',
            'format': 'XXX.X',
            'description': 'Max. insp. Airway Pressure'
            },
        "triggerPressure": {
            'code': '0x15',
            'unit': 'mbar',
            'format': '_XX.X',
            'description': 'Trigger Pressure'
            },
        "tachyapneaFrequency": {
            'code': '0x16',
            'unit': '1/min',
            'format': '_XXX_',
            'description': 'Tachyapnea Frequency'
            },
        "tachyapneaDuration": {
            'code': '0x17',
            'unit': 'sec',
            'format': '_XXX_',
            'description': 'Tachyapnea Duration'
            },
        "flowTrigger": {
            'code': '0x29',
            'unit': 'L/min',
            'format': '__XX_',
            'description': 'Flow Trigger'
            },
        "ASBRamp": {
            'code': '0x2E',
            'unit': 'sec',
            'format': '__XX_',
            'description': 'ASB Ramp'
            }
}

# THIS WILL ALSO HAVE TO BE CHANGED ONCE WE GET INFO FROM THE MANUFACTURER
evita.settingsWrite = {
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

evita.measuredData = {
        'compliance': {
            'code': '0x07',
            'unit': 'L/bar',
            'format': '_XXX',
            'description': 'Compliance L/bar'
            },
        'resistance': {
            'code': '0x08',
            'unit': 'mbar/L/s',
            'format': 'XXX_',
            'description': 'Resistance'
            },
        'minimalAirwayPressure': {
            'code': '0x71',
            'unit': 'mbar',
            'format': '*_XX_',
            'description': 'Minimal Airway Pressure'
            },
        'occlusionPressure': {
            'code': '0x72',
            'unit': 'mbar',
            'format': 'XX.X',
            'description': 'Occlusion Pressure'
            },
        'meanBreathingPressure': {
            'code': '0x73',
            'unit': 'mbar',
            'format': '*_XX_',
            'description': 'Mean Breathing Press.'
            },
        'plateauPressure': {
            'code': '0x74',
            'unit': 'mbar',
            'format': '*_XX_',
            'description': 'Plateau Pressure'
            },
        'PEEPBreathingPressure': {
            'code': '0x78',
            'unit': 'mbar',
            'format': '*_XX_',
            'description': 'PEEP Breathing Press.'
            },
        'intrinsicPEEPBreathingPressure': {
            'code': '0x79',
            'unit': 'mbar',
            'format': 'XXX.X',
            'description': 'Intrinsic PEEP Breath. Press.'
            },
        'peakBreathingPressure': {
            'code': '0x79',
            'unit': 'mbar',
            'format': '*_XX_',
            'description': 'Peak Breathing Press.'
            },
        'trappedVolume': {
                'code': '0x81',
                'unit': 'mL',
                'format': '_XXX',
                'description': 'Trapped Volume'
                },
        'tidalVolume': {
                'code': '0x82',
                'unit': 'L',
                'format': 'X.XX',
                'description': 'Tidal Volume L'
                },
        'spontaneousRespiratoryRate': {
                'code': '0xB5',
                'unit': '1/min',
                'format': 'XXX_',
                'description': 'Spontaneous Respiratory Rate'
                },
        'spontaneousMinuteVolume': {
                'code': '0xB7',
                'unit': 'L/min',
                'format': 'XX.X',
                'description': 'Spontaneous Minute Volume'
                },
        'respiratoryMinuteVolume': {
                'code': '0xB9',
                'unit': 'L/min',
                'format': 'XX.X',
                'description': 'Respiratory Minute Volume'
                },
        'airwayTemperature': {
                'code': '0xC1',
                'unit': 'deg C',
                'format': '_XX_',
                'description': 'Airway Temperature'
                },
        'respiratoryRatePediatric': {
                'code': '0xD6',
                'unit': '1/min',
                'format': 'XXX_',
                'description': 'Resp. Rate (Vol./Flow)(Pediat)'
                }
        }

evita.realtimeData = {
        'airwayPressure': {
                'code': '0x00',
                'unit': 'mbar',
                'descriptioin': 'Airway Pressure'
                },
        'flow': {
                'code': '0x01',
                'unit': 'L/min',
                'descriptioin': 'Flow (insp./exp.)'
                },
        'respiratoryVolumeSinceInspiratoryBegin': {
                'code': '0x03',
                'unit': 'mL',
                'descriptioin': 'Resp. Volume sinc insp. Begin'
                },
        'expiratoryVolume': {
                'code': '0x24',
                'unit': 'mL',
                'descriptioin': 'Expiratory Volume'
                }
    }

evita.textMessages = {
        'modeIPPV': {
                'code': '0x01',
                'message': 'Mode IPPV'
                }
        'modeIPPVAssist': {
                'code': '0x02',
                'message': 'Mode IPPV/ASSIST'
                },
        'modeCPPV': {
                'code': '0x04',
                'message': 'Mode CPPV'
                },
        'modeCPPVAssist': {
                'code': '0x05',
                'message': 'Mode CPPV/ASSIST'
                },
        'modeSIMV': {
                'code': '0x06',
                'message': 'Mode SIMV'
                },
        'modeSIMVASB': {
                'code': '0x07',
                'message': 'Mode SIMV/ASB'
                },
        'modeSB': {
                'code': '0x08',
                'message': 'Mode SB'
                },
        'modeASB': {
                'code': '0x09',
                'message': 'Mode ASB'
                },
        'modeCPAP': {
                'code': '0x0A',
                'message': 'Mode CPAP'
                },
        'modeCPAPASB': {
                'code': '0x0B',
                'message': 'Mode CPAP/ASB'
                },
        'modeMMV': {
                'code': '0x0C',
                'message': 'Mode MMV'
                },
        'modeMMVASB': {
                'code': '0x0D',
                'message': 'Move MMV/ASB'
        'modeBIPAP': {
                'code': '0x0E',
                'message': 'Mode BIPAP'
                },
        'modeSynchronizeMaster': {
                'code': '0x0F',
                'message': 'Mode SYNCHRON MASTER'
                },
        'modeSynchronizeSlave': {
                'code': '0x10',
                'message': 'Mode SYNCHRON SLAVE'
                },
        'modeApneaVentilation': {
                'code': '0x11',
                'message': 'Mode APNEA VENTILATION'
                },
        'modeDS': {
                'code': '0x12',
                'message': 'Mode DS'
                },
        'modeBIPAP-SIMV': {
                'code': '0x18',
                'message': 'Mode BIPAP-SIMV'
                },
        'modeBIPAP-SIMVASB': {
                'code': '0x19',
                'message': 'Mode BIPAP-SIMV/ASB'
                },
        'modeBIPAP-APRV': {
                'code': '0x1A',
                'message': 'Mode BIPAP-APRV'
                }
        }
