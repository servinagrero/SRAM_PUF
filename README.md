# Implementación de una Función Física Inclonable en un microcontrolador

El objetivo de este proyecto es crear una PUF utilizando la memoria SRAM de un microcontrolador, en concreto, dos modelos de la empresa STM.

La memoria que detalla todo lo relacionado con este proyecto se encuentra en el directorio `paper`. Para ver los resultados y leer un resumen del proyecto finalizado, mirar las diapositivas que se encuentran en el directorio `presentation`. 

> Las diapositivas están escritas en Rmarkdown y tendrán que ser compiladas para poder verlas en formato reveal.js


## Estructura

+ `doc/`: Datasheets e información del hardware utilizado.

+ `src/`: Código fuente de todo lo relacionado con el proyecto

  + `Project/`: Programación para las placas de 32 KB.
  + `Project_HM/`: Programación para las placas de 64 KB.
  + `dump.py`: Python model to represent a memory dump.
  + `storer.py`: Python script to recieve and store data..

+ `util/`: Scripts y utilidades varias para agilizar procesos.
  + `exporter`: Scripts para exportar y formatear dados desde MongoDB.
  
+ `paper/`: Ficheros de LaTeX para la memoria final del proyecto

+ `presentation/`: Ficheros de Rmarkdown para mostrar el resultado del proyecto.
