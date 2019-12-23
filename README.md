# Implementation of a Physical Unclonable Function (PUF) on a microprocessor

The objective of this project is the creation of a PUF on a microprocessor.
For that, we are using the STM32-Discovery Kit. We have two types of board: One with 32 KB of RAM and another one with 64 KB of RAM.

## Structure

+ `doc/`: Documentation needed for the project.
    + `datasheets/`: Datasheets and user manuals of the boards used.

+ `src/`: Source code files for the project

  + `Project/`: STM32 files to program the low memory boards.
  + `Project_HM/`: STM32 files to program the high memory boards.
  + `dump.py`: Python model to represent a memory dump.
  + `storer.py`: Python script to recieve and store data.
  + `jupyter/`: Jupyter files to handle and visualize the results.
  + `dash/`: Dash files to visualize the data.

+ `util/`: Scripts and tools for the project.
  + `tfg_tools`: Docker for jupyter.
  + `data_script`: Docker for storer script.
