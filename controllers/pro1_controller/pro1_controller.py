from controller import Robot
import math
timestep=32

robot=Robot()
flag = 0

motorRPC =robot.getDevice("RPC")
motorRPF=robot.getDevice("RPF")
motorRMC= robot.getDevice("RMC")
motorRMF= robot.getDevice("RMF")
motorRAC= robot.getDevice("RAC")
motorRAF= robot.getDevice("RAF")

motorLPC= robot.getDevice("LPC")
motorLPF= robot.getDevice("LPF")
motorLMC= robot.getDevice("LMC")
motorLMF= robot.getDevice("LMF")
motorLAC= robot.getDevice("LAC")
motorLAF= robot.getDevice("LAF")

while robot.step(timestep) != -1:
    if(flag%10==0):
        motorRPC.setPosition(-0.1)
        motorLPC.setPosition(-0.1)
        
    elif(flag%10==2):
        motorRPF.setPosition(-0.1)
        motorLPF.setPosition(-0.1)    
        
    elif(flag%10==4):
        motorRMC.setPosition(-0.1) 
        motorLMC.setPosition(-0.1) 
        
    elif(flag%10==6):
        motorRMF.setPosition(-0.1)
        motorLMF.setPosition(-0.1)
        
    elif(flag%10==6):
        motorRAC.setPosition(-0.1)
        motorLAC.setPosition(-0.1)
        
    elif(flag%10==6):
        motorRAF.setPosition(-0.1)
        motorLAF.setPosition(-0.1)
        
    elif(flag%10==7):
        motorRPC.setPosition(0.2)  
        motorRPF.setPosition(0.2)
        motorRMC.setPosition(0.2)
        motorRMF.setPosition(0.2)
        motorRAC.setPosition(0.2)
        motorRAF.setPosition(0.2)
        
        motorLPC.setPosition(0.2)  
        motorLPF.setPosition(0.2)
        motorLMC.setPosition(0.2)
        motorLMF.setPosition(0.2)
        motorLAC.setPosition(0.2)
        motorLAF.setPosition(0.2)
        
       
    flag += 1
    
    
    
