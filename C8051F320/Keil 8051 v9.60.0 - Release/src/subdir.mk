################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
A51_UPPER_SRCS += \
../src/SILABS_STARTUP.A51 

C_SRCS += \
../src/USBXpress_Voltmeter_main.c \
../src/descriptor.c 

OBJS += \
./src/SILABS_STARTUP.OBJ \
./src/USBXpress_Voltmeter_main.OBJ \
./src/descriptor.OBJ 


# Each subdirectory must supply rules for building sources it contributes
src/%.OBJ: ../src/%.A51 src/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: Keil 8051 Assembler'
	AX51 "@$(patsubst %.OBJ,%.__ia,$@)" || $(RC)
	@echo 'Finished building: $<'
	@echo ' '

src/%.OBJ: ../src/%.c src/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: Keil 8051 Compiler'
	C51 "@$(patsubst %.OBJ,%.__i,$@)" || $(RC)
	@echo 'Finished building: $<'
	@echo ' '

src/USBXpress_Voltmeter_main.OBJ: C:/SiliconLabs/SimplicityStudio/v5/developer/sdks/8051/v4.3.1/Device/C8051F320/inc/SI_C8051F320_Register_Enums.h C:/SiliconLabs/SimplicityStudio/v5/developer/sdks/8051/v4.3.1/Device/shared/si8051Base/si_toolchain.h C:/Users/konra/SimplicityStudio/v5_workspace/USBXpressVoltmeter/src/efm8_usbxpress.h C:/Users/konra/SimplicityStudio/v5_workspace/USBXpressVoltmeter/src/descriptor.h C:/SiliconLabs/SimplicityStudio/v5/developer/sdks/8051/v4.3.1/Device/shared/si8051Base/stdint.h C:/SiliconLabs/SimplicityStudio/v5/developer/sdks/8051/v4.3.1/Device/C8051F320/inc/SI_C8051F320_Defs.h C:/SiliconLabs/SimplicityStudio/v5/developer/sdks/8051/v4.3.1/Device/shared/si8051Base/stdbool.h

src/descriptor.OBJ: C:/Users/konra/SimplicityStudio/v5_workspace/USBXpressVoltmeter/src/descriptor.h C:/Users/konra/SimplicityStudio/v5_workspace/USBXpressVoltmeter/src/efm8_usbxpress.h C:/SiliconLabs/SimplicityStudio/v5/developer/sdks/8051/v4.3.1/Device/shared/si8051Base/stdint.h C:/SiliconLabs/SimplicityStudio/v5/developer/sdks/8051/v4.3.1/Device/shared/si8051Base/stdbool.h C:/SiliconLabs/SimplicityStudio/v5/developer/sdks/8051/v4.3.1/Device/shared/si8051Base/si_toolchain.h


