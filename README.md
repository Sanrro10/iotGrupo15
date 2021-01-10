# iotGrupo15

Esta aplicación será una demo del sistema de almacenamiento y descontaminación de comida para personas vulnerables que describimos en clase.

## Procedimiento

La raspberry con función de sensor, detectará el pulso de un botón para simular que se abren las puertas del frigorífico o armario (se simulará mediante un electromagnet y un magnetic switch). En cuanto se cierren las puertas comenzará un contador de 5 segundos (epara el correcto uso en la vida real habría que cambiar este parámetro a 48 horas).
Cuando se complete este se enviará una señal a la raspberry avisadora, que cuando se complete, sonará un pitido. A partir de este momento, se podrá abrir con el botón en el avisador.
La raspberry sensor recoje datos y los manda a una InfluxBD en Grafana.

## Comenzando 🚀

_A continuación, se explican los pasos a seguir para la correcta utilización de la aplicación._


### Pre-requisitos 📋

Para el funcionamiento correcto de la aplicación, es necesario disponer de:
  - Dos Raspberry Pi (https://www.raspberrypi.org/)
  - Dos Grove hat (https://wiki.seeedstudio.com/Grove_Base_Kit_for_Raspberry_Pi/)
  - Dos Botones (https://wiki.seeedstudio.com/Grove-Button/)
  - Una Led Bar (https://wiki.seeedstudio.com/Grove-LED_Bar/)
  - Un magnetic switch (https://wiki.seeedstudio.com/Grove-Magnetic_Switch/)
  - Un buzzer (https://wiki.seeedstudio.com/Grove-Buzzer/)
  - Imán electrónico (https://wiki.seeedstudio.com/Grove-Electromagnet/
  - Cables PWM
Este proyecto depende de las siguientes librerias y sus dependencias:
  AMBAS RASPIS:
    - [Grove]: https://github.com/Seeed-Studio/grove.py
    - [Pybluez]: https://github.com/pybluez/pybluez
  TAN SOLO EL FRIGORIFICO:
   - [Grafana]: https://github.com/grafana/grafana
   - [Influxdb]: https://github.com/influxdata/influxdb
Además,  habrá que vincular las Raspberrys a usar mediante bluetooth como se presenta a continuación:
  https://bluedot.readthedocs.io/en/latest/pairpipi.html
 
  
### Instalación 🔧

_Clonar repositorio_
  Primero habrá que clonar el repositorio de github desde este link:
```
    https://github.com/Sanrro10/iotGrupo15/
```
  En caso de querer clonar desde la consola, utilizaremos estos comandos:
```
  git remote add origin https://github.com/Sanrro10/iotGrupo15.git
  git push -u origin master
  ```
 _Instalación física de los componentes_
  Componentes Raspberry frigorifico:
    Electromagnet: PIN 12
    Magnetic Switch: PIN 18
    Botón: PIN 5
   Componentes Raspberry avisador
    Buzzer: PIN 12
    Botón: PIN 5
    
En una Raspberry, que hará de sensor, tendremos conectados un botón, el imán electrónico y un magnetic switch e instalaremos el código correspondiente al sensor: frigo.py. 
En la otra, el avisador, conectaremos el resto de componentes e instalaremos el código de la carpeta avisador: avisador.py.
Ejecutamos el código de ambas y las conectamos por bluetooth.
En una simulación más cercana a una aplicación real de este proyecto, ambos programas estarán en crontab puesto que pertenecerian a dispositivos sin interfaces dedicados exclusivamente a este programa, para esto abrimos crontab con el comando crontab -e  y en el bloque final escribimos el comando @reboot python3 ruta-del-archivo.

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Python](https://es.python.org) - Lenguaje de programación.
* [JupyterLab](https://jupyter.org) - Framework



## Autores ✒️

* **Marcos Barcina**  [marcosbarcina@opendeusto.es]
* **Danel Rey**  [danel.rey@opendeusto.es]
* **Iñigo Gonzalez de San Román** [i.glzsr@opendeusto.es]
