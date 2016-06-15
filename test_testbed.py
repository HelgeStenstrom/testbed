import testbed
import unittest
import io


class MyTestCase(unittest.TestCase):

    def setUp(self):
        fd = io.StringIO(exampleFile)
        self.parser = testbed.parser(fd)


    def testGetSections(self):
        sections = self.parser.getSections()
        self.assertTrue("BG1" in sections)
        self.assertTrue("SG1" in sections)

    def testPutSections(self):
        outputFd  = io.StringIO()
        self.parser.putFile(outputFd)
        outputFd.seek(0)
        for line in outputFd.readlines():
            #print(line)
            pass

    def testWriteSections(self):
        with open("aConfig.ini", 'w') as configfile:
            self.parser.config.write(configfile)


exampleFile = """# -*- conf -*-

[TestbedInfo]
TestbedType=RxTb
OperatingBand = 3
Scope = Ru

# PSG Uplink Signal/Interferer for frequencies above 3GHz
[SG1]
InstrumentType=PSG
InstrumentIdString=E8257D
InstrumentTag=E8257D
GPIBAddress=TCPIP::10.83.11.xx
GPIB488Compliant=TRUE
ErrorHandling=No
Handshake=Polling
SubSystem=1
Communicator=Stubbed

# Sa FSU used for Noise source control for Noise Figure test case
[SA1]
InstrumentType=FSG
InstrumentIdString=FSG-13
GPIBAddress=TCPIP::10.83.11.70
GPIB488Compliant=TRUE
ErrorHandling=No
Handshake=Polling
SubSystem=1
Communicator=stubbed

# PSG Uplink Signal/Interferer for frequencies above 3GHz
[BG1]
InstrumentType=PSG
InstrumentIdString=E8257D
InstrumentTag=E8257D
GPIBAddress=TCPIP::10.83.11.xx
GPIB488Compliant=TRUE
ErrorHandling=No
Handshake=Polling
SubSystem=1
Communicator=VISA
#Communicator=Stubbed

# SMU Uplink Signal/Interferer for frequencies below 3GHz
[SG2]
InstrumentType=SMU
InstrumentIdString=SMU200A
InstrumentTag=SMU200A
GPIBAddress=TCPIP::10.83.11.152
GPIB488Compliant=TRUE
ErrorHandling=No
Handshake=Polling
SubSystem=1
Communicator=VISA
#Communicator=Stubbed

# SMU Uplink Signal/Interferer for frequencies below 3GHz
[BG2]
InstrumentType=SMU
InstrumentIdString=SMU200A
InstrumentTag=SMU200A
GPIBAddress=TCPIP::10.83.11.152
GPIB488Compliant=TRUE
ErrorHandling=No
Handshake=Polling
SubSystem=1
Communicator=VISA
#Communicator=Stubbed

# SMU Uplink Signal/Interferer for frequencies below 3GHz
[SG3]
InstrumentType=SMU
InstrumentIdString=SMU200A
InstrumentTag=SMU200A
GPIBAddress=TCPIP::10.83.11.yy
GPIB488Compliant=TRUE
ErrorHandling=No
Handshake=Polling
SubSystem=2
Communicator=VISA
#Communicator=Stubbed

# SMU Uplink Signal/Interferer for frequencies below 3GHz
[BG3]
InstrumentType=SMU
InstrumentIdString=SMU200A
InstrumentTag=SMU200A
GPIBAddress=TCPIP::10.83.11.yy
GPIB488Compliant=TRUE
ErrorHandling=No
Handshake=Polling
SubSystem=2
Communicator=VISA
#Communicator=Stubbed

# NRP2 power meter these are dual ports containing both CH A and CH B
[PM1]
InstrumentType=NRP
InstrumentIdString=NRP
InstrumentTag=NRP
GPIBAddress=TCPIP::10.83.11.yy
GPIB488Compliant=TRUE
ErrorHandling=No
Handshake=Polling
SubSystem=1
Communicator=Stubbed

# NRP2 power meter these are dual ports containing both CH A and CH B
[PM2]
InstrumentType=NRP
InstrumentIdString=NRP
InstrumentTag=NRP
GPIBAddress=TCPIP::10.83.11.yy
GPIB488Compliant=TRUE
ErrorHandling=No
Handshake=Polling
SubSystem=2
Communicator=Stubbed


# *IDN? = *IDN? = "ERICSSON,ICS4813,S/N 1,R3A" in StubbedDefaults.ini
# In "real life" InstrumentId should be the same as the "InstrumentTag"
# Switch Box - Main Unit
[SC1]
InstrumentType=Ics4813
InstrumentTag=RxMAIN.1862.R3
#InstrumentIdString=LTN_214_1862_1.R3A
InstrumentIdString=Ics4813
I2C=1
SubSystem=1
IpAddr=10.83.11.zz
IPport=23
GPIB488Compliant=FALSE
Communicator=Stubbed

# *IDN? = *IDN? = "ERICSSON,ICS4813,S/N 1,R3A" in StubbedDefaults.ini
# In "real life" InstrumentId should be the same as the "InstrumentTag"
# Switch Box - Filter Unit
[SC2]
InstrumentType=Ics4813
InstrumentTag=RxFILTER.2158.R1A
#InstrumentIdString=1_LTN2142158_7
InstrumentIdString=Ics4813
GPIBAddress=GPIB2::11
IPport=23
GPIB488Compliant=FALSE
Communicator=Stubbed

# # The dot box for blocking
# [SC3]
# InstrumentType=Ics4813
# #InstrumentTag=LTN2142232_1
# InstrumentTag=DOT.R1
# InstrumentIdString=Ics4813
# #I2C=1
# SubSystem=1
# IpAddr=10.83.11.xx
# IPport=23
# GPIB488Compliant=FALSE
# Communicator=Stubbed




# Switch Box - 4-port-box
#[SC3]
#InstrumentType=Ics4813
#InstrumentTag=ExtDuplex
#InstrumentIdString=Ics4813
#InstrumentIdString=Ics4813
#GPIBAddress=GPIB2::14
#IPport=23
#GPIB488Compliant=FALSE
#Communicator=Stubbed

# different id string when stubbed
[PA1]
InstrumentType=EmBbs3g6ehm
InstrumentIdString=EMBBS3G6EHM
GPIBAddress=GPIB2::30
GPIB488Compliant=TRUE
Handshake=No
Communicator=Stubbed
#Communicator=VISA


## Env control of Power supply
[PS1]
InstrumentType=N5700
InstrumentIdString=N5768A
GPIBAddress=GPIB2::5
GPIB488Compliant=TRUE
Handshake=Polling
ErrorHandling=No
Communicator=Stubbed
#Communicator=VISA

## Env control of Power supply
[PS3]
InstrumentType=N5700
InstrumentIdString=N5768A
GPIBAddress=GPIB2::X
SubSystem=2
GPIB488Compliant=TRUE
Handshake=Polling
ErrorHandling=No
Communicator=Stubbed
#Communicator=VISA

## Env control of Climate chamber (Vc supports humidity, Vt does not)
[CC1]
InstrumentType=VT7200
InstrumentIdString=VT7200
GPIBAddress=GPIB9::5
GPIBSecondaryAddress=GPIB9::4
GPIB488Compliant=FALSE
Handshake=Polling
ErrorHandling=No
Communicator=STUBBED
#Communicator=ASCII





#just for calibration tests
[NWA1]
InstrumentType=N5230A
InstrumentIdString=N5230A
#I2C=1
SubSystem=1
IpAddr=10.67.1.78
IPport=23
GPIB488Compliant=FALSE
Communicator=Stubbed
CalibrationOnly = TRUE

"""

if __name__ == '__main__':
    unittest.main()
