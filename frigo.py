import time
from grove.factory import Factory
from grove_button import GroveButton
from grove_switch import GroveSwitch
import bluetooth
import datetime
import psutil
from influxdb import InfluxDBClient

vacio = False

# influx configuration - edit these
ifuser = "grupo15"
ifpass = "grupo15"
ifdb   = "proyecto"
ifhost = "grupo15"
ifport = 8086
measurement_name = "system"


magnet = Factory.getGpioWrapper("Electromagnet", 12)
switch = GroveSwitch(18)
button = GroveButton(5)

def on_press(t):
    if(switch.state):
        magnet.off()
        print("Electromagnet apagado")
    else:
        magnet.on()
        global vacio
        vacio = False
        print("Electromagnet encendido")
button.on_press = on_press

def waitWhileClosed():
    starting_time = time.time()
    final_time = starting_time + 5
    seguir = True
    print("Starting at: " + time.ctime(starting_time))
    print("Finishing at: " + time.ctime(final_time))    
    while seguir:
        current_time = time.time()
        if(current_time >= final_time):
            s.send("Tiempo Completado")
            # take a timestamp for this measurement
            timestamp = datetime.datetime.utcnow()

            # collect some stats from psutil
            disk = psutil.disk_usage('/')
            mem = psutil.virtual_memory()

            # format the data as a single measurement for influx
            body = [
                {
                    "measurement": measurement_name,
                    "time": timestamp,
                    "fields": {
                        "disk_percent": disk.percent,
                        "disk_free": disk.free,
                        "disk_used": disk.used,
                        "mem_percent": mem.percent,
                        "mem_free": mem.free,
                        "mem_used": mem.used,
                    }
                }
            ]

            # connect to influx
            ifclient = InfluxDBClient(ifhost,ifport,ifuser,ifpass,ifdb)

            # write the measurement
            ifclient.write_points(body)
            esperar = True
            while esperar:
                data = s.recv(1024)
                if data:
                    print("Frigorífico abierto por el avisador")
                    magnet.off()
                    seguir = False
                    esperar = False
                    waitButton()
                    break
        elif(switch.state == False):
            print("Frigorífico abierto")
            waitWhileOpened()  
            seguir = False
        
        
def waitWhileOpened():
    opened = True
    while opened:
        print("Esperando a que se cierre")
        time.sleep(3)
        if(switch.state):
            opened = False
    print("Frigorífico cerrado")
    waitWhileClosed()
        
def waitButton():
    global vacio
    vacio = True
    print("--------------------------------------------------------------------")
    print("Frigorífico vacío. Se esperará a que se llene y se cierre con seguro")
    while vacio:
        time.sleep(1)
    waitWhileOpened()
def setupBluetooth():
    serverMACAddress = 'B8:27:EB:20:6C:D7'
    port = 1
    while True:    
        try:
            s1 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            s1.connect((serverMACAddress, port))
        except:
            continue 
        break
    global s
    s = s1

def main():
    setupBluetooth()    
    magnet.on()
    waitWhileClosed()
    
    
    
if __name__ == '__main__':
    main()