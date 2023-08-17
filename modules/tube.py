from pybricks.nxtdevices import ColorSensor                                
from pybricks.parameters import Port

tube_sensor_verification = ColorSensor(Port.S4)

def tube():
    verification = tube_sensor_verification.reflection()
    if verification > 0:
        print("Tube is 15cm high")
        return True
    else:
        print("Tube is 10cm high")
        return False
    
def hight_tube():
    key = ''
    
    if tube() == True:
        return key = '15'
    
    else:
        return key = '10'