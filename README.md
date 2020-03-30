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
The MedibusInterface class contains the core MEDIBUS protocol commands for all Draeger devices. The Device class inherits from the MedibusInterface class (i.e. The Draeger Evita V500), which inherits all the commands from the communications interface and adds all the device-specific available settings, alarms, etc.

Reasoning: Since each ventilator will have device-specific commands, we want the communication interface to be modifiable on a per-device basis. However, we also want devices with common communication interfaces (MEDIBUS for Draeger) to share a common protocol. Unfortunately, the protocol between manufacturers can be so different as to make finding commonality useless, but the ventilator settings (and hence the UI) should be pretty similar.

## Tests to write (to be moved to ticket system)
- Software does not crash the ventilator if PC is powered off
- Software can communicate with ventilator for extended period of time (days)
- After writing settings to ventilator, settings are in fact changed

## Open Questions (port to ticket system)

Q: How should we deal with the different codepages? Should we add a field to data codes? Right now this information is not encoded. Currently only codepage 1 is implemented and this is going to be a problem.

Q: There is a slight difference in naming some commands between the MEDIBUS specification and the MEDIBUS for Intensive Care Devices. Which should take precedence / how should we name things? A couple of these have not been added for this reason (including the codepage 2 commands).

Q: Do we want to implement commands with arguments (it seems like the only function of this is to reduce the amount of information we get back - I think we only need to implement this if speed becomes a serious issue).

## Closed Questions (port to ticket system)
Q: Why does the MEDIBUS specification say that the data codes are 2 bytes long, but all the data bytes specified in the ICU device command sspecification have 1-byte long data codes? This is true for alarms as well. Do we need to add some known value to these to encode them? How do the two different codepages play into this (1 and 2)?
A: The raw data bytes corresponding to the hex codes are not sent, but the hex codes are themselves sent as ASCII characters. For example, for the data code '0x2F', whose binary representation is 0b00101111, only one byte of information is contained, but this is sent over the interface as ASCII '2' (0x32, 0b00110010) followed by ASCII 'F' (0x46, 0b01000110). This seems awkward and annoying, but it is what it is. The codepages are dealt with separately.

Q: How do we generate the checksum for the MEDIBUS commands?
A: I believe we take the integer sum of all the preceeding ascii characters (so for 'A', 65, for 'ESC', 27), and then the resultant sum, we represent in hexadecimal. So for 255, 'FF'. THEN, that hexadecimal character code is converted back into ascii, with the characters capitalized. So we now have two bytes, 0x70, 0x70, which represent together the two-byte checksum.

## Naming
All alarm names are camel-case concatenated from their descriptions in the MEDIBUS for Intensive Care Devices Specification (Draeger Intensive Care Device Commands below)

## Documentation
Draeger Serial MEDIBUS Protocol v. 4.0.3 (2007) https://drive.google.com/open?id=17cH-RRV5SITCA4QWiZ-h3vH5WjzPpc7X
Draeger Intensive Care Device Commands: https://drive.google.com/a/berkeley.edu/file/d/1wM04Sw83ycJRJdU-Gx0PgJyKrk5GGM0I/view?usp=sharing

Maquet Serial Communication Protocol v. 9 (2011) https://drive.google.com/a/berkeley.edu/file/d/1VXPmd_Q2SK1FDuTrS6ph-TM8n-kiCO6B/view?usp=sharing

