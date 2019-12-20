# Implementation of a Physical Unclonable Function (PUF) on a microprocessor

The objective of this project is the creation of a PUF on a microprocessor.
For that, we are using the STM32-Discovery Kit. We have two types of board: One with 32 KB of RAM and another one with 64 KB of RAM.

## Structure

+ __doc/__: Documentation needed for the project.
    + __datasheets/__: Datasheets and user manuals of the boards used.

+ __src/__: Source code files for the project

  + __Project/__: STM32 files to program the low memory boards.
  + __Project_HM/__: STM32 files to program the high memory boards.
  + __dump.py__: Python model to represent a memory dump.
  + __storer.py__: Python script to recieve and store data.
  + __jupyter/__: Jupyter files to handle and visualize the results.

+ __util/__: Scripts and tools for the project.
  + __tfg_tools__: Docker for jupyter.
  + __data_script__: Docker for storer script.
