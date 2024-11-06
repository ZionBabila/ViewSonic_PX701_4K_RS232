import serial
import time

# Set up the serial connection (adjust the port as needed)
ser = serial.Serial(
    port='COM4',  # Replace with your serial port (e.g., 'COM3', '/dev/ttyUSB0')
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=2  # Timeout for reading responses
)

def send_command(command):
    """Send a command to the display and print the response."""
    try:
        # Reset serial buffers before sending command
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        
        # Send command followed by carriage return and newline
        print(f"Sending command: {command.hex()}")
        ser.write(command + b'\r\n')
        time.sleep(1)  # Short delay to allow device to respond

        # Read response in a loop until data is available or timeout occurs
        start_time = time.time()
        response = b""
        while time.time() - start_time < 2:
            if ser.in_waiting > 0:
                response += ser.read(ser.in_waiting)
            time.sleep(0.1)
        
        if response:
            response_hex = response.hex()
            print("Response:", response_hex)
            return response_hex
        else:
            print("No response received.")
            return None
    except Exception as e:
        print("Error:", e)
        return None

def power_on():
    """Turn on the display."""
    print("Sending power ON command...")
    command = bytearray([0x35, 0x21, 0x30, 0x30, 0x31])  # Corresponds to '5!001'
    response = send_command(command)
    if response and ("2b" in response or "3e" in response):  # Accept '+' or '>'
        print("Power ON command acknowledged.")
    elif response and "2d" in response:  # Check for '-' (failure)
        print("Power ON command failed.")
    else:
        print("Unexpected response:", response)

def power_off():
    """Turn off the display (Standby mode)."""
    print("Sending power OFF command...")
    command = bytearray([0x35, 0x21, 0x30, 0x30, 0x30])  # Corresponds to '5!000'
    response = send_command(command)
    if response and ("2b" in response or "3e" in response):  # Accept '+' or '>'
        print("Power OFF command acknowledged.")
    elif response and "2d" in response:  # Check for '-' (failure)
        print("Power OFF command failed.")
    else:
        print("Unexpected response:", response)

if __name__ == "__main__":
    power_on()
    time.sleep(5)  # Wait a few seconds before turning off
    power_off()
    ser.close()  # Close the serial connection when done
