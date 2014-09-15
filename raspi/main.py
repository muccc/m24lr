#!/usr/bin/env python
# Sample script for reading data from the M24LR-discovery board

# i2c addresses
temp_sensor_address = 0x39
eeprom_address = 0x53

# import libraries
import smbus as smbus

#configure I2C bus for functions
i2c = smbus.SMBus(1)

# read temperature
hi = i2c.read_byte_data( temp_sensor_address, 0 )
lo = i2c.read_byte_data( temp_sensor_address, 2 )
if hi > 0:
    temp = hi + lo * 1.0/256.0
else:
    temp = hi - lo * 1.0/256.0
print 'M24LR at address 0x{0:02x} READ {1:2.2f}'.format(temp_sensor_address, temp )

print '  '

#read eeprom
print 'M24LR at address 0x{0:02x} READ '.format(eeprom_address )
b = 0x00
while b != 0xFE:
    print chr(b)
    b = i2c.read_byte(eeprom_address)
