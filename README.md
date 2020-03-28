# VentilatorController

Software for remote control and data readout of ICU ventilators. 

## Specifications
1. System State readout<br/>
The software should be able to read out the current settings of the ventilator, including the alarm thresholds / settings, set tidal volume / PEEP / etc. 

2. System State write<br/>
The software should be able to change the settings of the ventilator, including 

3. Real-time data readout<br/>
Where available, the software should be able to read real-time data 

## Architecture
Ventilators are represented as an instance of the 'Device' class. These devices contain all the settings

## Naming
All alarm names are camel-case concatenated from their descriptions in the MEDIBUS for Intensive Care Devices Specification (Draeger Intensive Care Device Commands below)

## Current Work


## Documentation
Draeger Serial MEDIBUS Protocol v. 6.0.0 (2007) https://drive.google.com/open?id=17cH-RRV5SITCA4QWiZ-h3vH5WjzPpc7X
Draeger Intensive Care Device Commands: https://drive.google.com/a/berkeley.edu/file/d/1wM04Sw83ycJRJdU-Gx0PgJyKrk5GGM0I/view?usp=sharing

Maquet Serial Communication Protocol v. 9 (2011) https://drive.google.com/a/berkeley.edu/file/d/1VXPmd_Q2SK1FDuTrS6ph-TM8n-kiCO6B/view?usp=sharing

