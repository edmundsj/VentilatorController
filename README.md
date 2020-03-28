# VentilatorController

Software for remote control and data readout of ICU ventilators. 

## Specifications
1. System State readout<br/>
Read out the current settings of the ventilator, including the alarm thresholds / settings, set tidal volume / PEEP / etc. 

2. System State write<br/>
Change the settings of the ventilator, including tidal volume, PEEP, alarm thresholds, etc.

3. Real-time data readout<br/>
Where available, read real-time data  and display it in a UI similar to that of existing ventilators.

4. Alarm Pass-Through and Notification<br/>
Immediately notify the user of alarms on the device, and potentially aggregate these alarms into a single location where all ventilators can be viewed at-a-glance and selected to control.

## Goals
- Software should be as protocol-independent and device-independent as possible. Device-specific settings and commands should be separate from the implementation of the communication interface.

## Architecture
Ventilators are represented as an instance of the 'Device' class.

## Tests to write (to be moved to ticket system)
- Software does not crash the ventilator if PC is powered off
- Software can communicate with ventilator for extended period of time (days)
- After writing settings to ventilator, settings are in fact changed

## Open Questions
- Why does the MEDIBUS specification say that the data codes are 2 bytes long, but all the data bytes specified in the ICU device command sspecification have 1-byte long data codes? This is true for alarms as well. Do we need to add some known value to these to encode them? How do the two different codepages play into this (1 and 2). I suspect we just have to add a constant value for the second codepage, but the specification is unclear.
- How should we deal with the different codepages? Should we add a field to data codes?

## Naming
All alarm names are camel-case concatenated from their descriptions in the MEDIBUS for Intensive Care Devices Specification (Draeger Intensive Care Device Commands below)

## Documentation
Draeger Serial MEDIBUS Protocol v. 4.0.3 (2007) https://drive.google.com/open?id=17cH-RRV5SITCA4QWiZ-h3vH5WjzPpc7X
Draeger Intensive Care Device Commands: https://drive.google.com/a/berkeley.edu/file/d/1wM04Sw83ycJRJdU-Gx0PgJyKrk5GGM0I/view?usp=sharing

Maquet Serial Communication Protocol v. 9 (2011) https://drive.google.com/a/berkeley.edu/file/d/1VXPmd_Q2SK1FDuTrS6ph-TM8n-kiCO6B/view?usp=sharing

