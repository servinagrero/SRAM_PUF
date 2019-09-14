################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal.c \
/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_cortex.c \
/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_dma.c \
/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_flash.c \
/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_flash_ex.c \
/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_flash_ramfunc.c \
/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_gpio.c \
/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_pwr.c \
/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_pwr_ex.c \
/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_rcc.c \
/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_rcc_ex.c \
/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_tim.c \
/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_tim_ex.c 

OBJS += \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal.o \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_cortex.o \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_dma.o \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_flash.o \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_flash_ex.o \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_flash_ramfunc.o \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_gpio.o \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_pwr.o \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_pwr_ex.o \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_rcc.o \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_rcc_ex.o \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_tim.o \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_tim_ex.o 

C_DEPS += \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal.d \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_cortex.d \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_dma.d \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_flash.d \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_flash_ex.d \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_flash_ramfunc.d \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_gpio.d \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_pwr.d \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_pwr_ex.d \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_rcc.d \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_rcc_ex.d \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_tim.d \
./Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_tim_ex.d 


# Each subdirectory must supply rules for building sources it contributes
Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal.o: /home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -g3 -DUSE_HAL_DRIVER -DSTM32L152xB -DDEBUG -c -I../Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Device/ST/STM32L1xx/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"
Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_cortex.o: /home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_cortex.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -g3 -DUSE_HAL_DRIVER -DSTM32L152xB -DDEBUG -c -I../Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Device/ST/STM32L1xx/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_cortex.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"
Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_dma.o: /home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_dma.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -g3 -DUSE_HAL_DRIVER -DSTM32L152xB -DDEBUG -c -I../Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Device/ST/STM32L1xx/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_dma.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"
Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_flash.o: /home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_flash.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -g3 -DUSE_HAL_DRIVER -DSTM32L152xB -DDEBUG -c -I../Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Device/ST/STM32L1xx/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_flash.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"
Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_flash_ex.o: /home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_flash_ex.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -g3 -DUSE_HAL_DRIVER -DSTM32L152xB -DDEBUG -c -I../Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Device/ST/STM32L1xx/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_flash_ex.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"
Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_flash_ramfunc.o: /home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_flash_ramfunc.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -g3 -DUSE_HAL_DRIVER -DSTM32L152xB -DDEBUG -c -I../Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Device/ST/STM32L1xx/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_flash_ramfunc.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"
Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_gpio.o: /home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_gpio.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -g3 -DUSE_HAL_DRIVER -DSTM32L152xB -DDEBUG -c -I../Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Device/ST/STM32L1xx/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_gpio.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"
Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_pwr.o: /home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_pwr.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -g3 -DUSE_HAL_DRIVER -DSTM32L152xB -DDEBUG -c -I../Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Device/ST/STM32L1xx/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_pwr.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"
Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_pwr_ex.o: /home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_pwr_ex.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -g3 -DUSE_HAL_DRIVER -DSTM32L152xB -DDEBUG -c -I../Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Device/ST/STM32L1xx/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_pwr_ex.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"
Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_rcc.o: /home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_rcc.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -g3 -DUSE_HAL_DRIVER -DSTM32L152xB -DDEBUG -c -I../Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Device/ST/STM32L1xx/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_rcc.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"
Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_rcc_ex.o: /home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_rcc_ex.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -g3 -DUSE_HAL_DRIVER -DSTM32L152xB -DDEBUG -c -I../Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Device/ST/STM32L1xx/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_rcc_ex.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"
Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_tim.o: /home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_tim.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -g3 -DUSE_HAL_DRIVER -DSTM32L152xB -DDEBUG -c -I../Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Device/ST/STM32L1xx/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_tim.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"
Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_tim_ex.o: /home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Src/stm32l1xx_hal_tim_ex.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -g3 -DUSE_HAL_DRIVER -DSTM32L152xB -DDEBUG -c -I../Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Device/ST/STM32L1xx/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/CMSIS/Include -I/home/vinagrero/STM32Cube/Repository/STM32Cube_FW_L1_V1.9.0/Drivers/STM32L1xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/STM32L1xx_HAL_Driver/stm32l1xx_hal_tim_ex.d" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"

