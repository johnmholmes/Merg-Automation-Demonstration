#welcome to the Merg Automation Sig demonstration code by j holmes
# This will only run once unless the last line of code"MergAuto1().statrt()"  is commented out#
import jarray
import jmri

class MergAuto1(jmri.jmrit.automat.AbstractAutomaton) :

    def init(self):
        # set up sensor numbers on complete route may not be called in this scriot though
        # infra red sensors
        self.S1 = sensors.provideSensor("DT1001")
        self.S2 = sensors.provideSensor("DT1002")
        self.S3 = sensors.provideSensor("DT1003")
        self.S4 = sensors.provideSensor("DT1004")
        self.S5 = sensors.provideSensor("DT1005")
        self.S6 = sensors.provideSensor("DT1006")
        self.S7 = sensors.provideSensor("DT1007")
        self.S8 = sensors.provideSensor("DT1008")
        self.S9 = sensors.provideSensor("DT1009")
        self.S10 = sensors.provideSensor("DT1010")
        # setup the routes
        self.r1 = sensors.provideSensor("ISroute1")
        self.r2 = sensors.provideSensor("ISroute2")
        self.r3 = sensors.provideSensor("ISroute3")

        # set loco address. For long address change "False" to "True"
        self.throttle = self.getThrottle(3, False)  
 
        return

    def handle(self):
        # first part of the automation
        # set loco to forward
        self.r1.setState(ACTIVE)# this is seting up the first route we will use 
        self.throttle.setIsForward(True)# sets the locothrotle for forwards
        print "Loco addeess 3 set to go forward"
        self.waitMsec(1000)# wait 1 second for layout to catch up, then set speed
        self.throttle.setSpeedSetting(0.15)#Slow start speed 15 for the loco adjust the speed to suit your loco
        self.waitSensorActive(self.S2)#at sensor S2 speed up to 35
        print "sensor S2 daccelerate 35"
        self.throttle.setSpeedSetting(0.35)
        print "going through station"
        self.waitSensorActive(self.S9)#sensor S9 decelerate
        print "sensor S9 decelerate 15"
        self.throttle.setSpeedSetting(0.15)
        self.waitSensorActive(self.S10)#sensor s10 stop
        print "Stop at first station 10 seconds"
        self.throttle.setSpeedSetting(0)#
        self.waitMsec(10000)
        print "Leaving station"  
        self.throttle.setSpeedSetting(.2)#
        self.waitSensorActive(self.S5)#sensor 5 decelerate
        print "sensor S5 decelerate 15" 
        self.throttle.setSpeedSetting(0.15)
        self.waitSensorActive(self.S6)#sensor S6 stop
        print "reached the end of the line" 
        self.throttle.setSpeedSetting(0)
        self.r1.setState(INACTIVE)#setting route to clear
        self.waitMsec(60000)           # wait for 1 seconds


        # second part of the automation going back to the start via route 2 i will not add the print statements 
        # for the following moves to keep the code easier to read print statements are good for your first attemp
        # to allow for debugging when something goes wrong



        self.r2.setState(ACTIVE)#setting route p2 active will change the turnouts
        self.throttle.setIsForward(False)# set the loco into reverse always leave at least 1 second before moving off
        self.waitMsec(1000)                
        self.throttle.setSpeedSetting(0.2)

        self.waitSensorActive(self.S10)
        self.throttle.setSpeedSetting(0.10)        
        
        self.waitSensorActive(self.S9)        
        self.throttle.setSpeedSetting(0)
        self.waitMsec(60000) 

        self.throttle.setSpeedSetting(0.30)

        self.waitSensorActive(self.S2)
        self.throttle.setSpeedSetting(0.15)


        self.waitSensorActive(self.S1)
        self.throttle.setSpeedSetting(0)

        self.r2.setState(INACTIVE)
        self.waitMsec(10000)  

        # Third part of the automation going to the siding via route 3 i will not add the print statements 


        self.r3.setState(ACTIVE)
        self.throttle.setIsForward(True)
        self.waitMsec(1000)                
        self.throttle.setSpeedSetting(0.2)

        self.waitSensorActive(self.S7)
        self.throttle.setSpeedSetting(0.10)        
        
        self.waitSensorActive(self.S8)        
        self.throttle.setSpeedSetting(0)
        self.waitMsec(10000) 

        self.r3.setState(INACTIVE)
        self.waitMsec(10000)    

        # Final part of the automation going back to the start via route 3 


        self.r3.setState(ACTIVE)
        self.throttle.setIsForward(False)
        self.waitMsec(1000)                
        self.throttle.setSpeedSetting(0.2)

        self.waitSensorActive(self.S2)
        self.throttle.setSpeedSetting(0.10)        
        
        self.waitSensorActive(self.S1)        
        self.throttle.setSpeedSetting(0)
        self.waitMsec(10000) 

        self.r3.setState(INACTIVE)
        self.waitMsec(10000)       

        return 0 # set to 0 to only run 1 time or 1 to run for ever        


# end of class definition

# start one of these up
MergAuto1().start()
