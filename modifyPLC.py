from pymodbus.client.sync import ModbusTcpClient

# Create a Modbus client
client = ModbusTcpClient('10.10.10.5', port=502)

# Connect to the PLC
client.connect()

# Write the value of 1 to register 0
result = client.write_registers(0, [1], unit=1)

# Disconnect from the PLC
client.close()
