import time
from grove.factory import Factory
from grove_button import GroveButton
import bluetooth
buttonNotPressed = False
buzzer = Factory.getGpioWrapper("Buzzer", 12)
button = GroveButton(5)


def on_press(t):
    global buttonNotPressed
    if(buttonNotPressed):
        buttonNotPressed = False
        client.send("Abre")
    else:
        print("El frigorifico no esta listo para ser avierto. Espere a que su avisador suene")
    
button.on_press = on_press


def on_bluetooth():
    global buttonNotPressed
    buzzer.on()
    time.sleep(1)
    buttonNotPressed = True
    while buttonNotPressed:
        time.sleep(1)
        print("Sleep")
    buttonNotPressed = False
    buzzer.off()
        
    
    waitBluetooth()
def waitBluetooth():
    print("Esperando a recibir el aviso de recogida...")
    while 1:
        data = client.recv(1024)
        if data:
            print("Aviso recibido!")
            break
    
    on_bluetooth();
        
def setupBluetooth():
    hostMACAddress = 'B8:27:EB:20:6C:D7'
    port = 1
    backlog = 1
    s1 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s1.bind((hostMACAddress, port))
    s1.listen(backlog)    
    try:
        cliente, clientInfo = s1.accept()
    except:
        print("Closing socket")
        cliente.close()
        s1.close()  
    global s
    global client
    global noBluetooth
    noBluetooth = False
    s = s1
    client = cliente
    
def main(): 
    setupBluetooth()
    waitBluetooth()
    
    
    
if __name__ == '__main__':
    main()