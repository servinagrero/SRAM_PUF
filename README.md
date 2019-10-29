# Implementation of a Physical Unclonable Function (PUF) on a microprocessor

El objetivo de este proyecto es la creación de una Función Física Inclonable en un microprocesador.
Para ello se utiliza la placa de desarrollo STM32-Discovery Kit (STM32L152r6).

## Structure

+ __doc/__: Documentation needed for the project.
    + __datasheets/__: Datasheets and user manuals of the boards used.
    
+ __src/__: Source code files for the project.
  + __Project/__: STM32 files to program the board.
  + __dump.py__: Python model to represent a memory dump.
  + __storer.py__: Python script to recieve and store data. 
  + __jupyter/__: Jupyter files to handle and visualize the results. 
