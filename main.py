import serial
import serial.tools.list_ports
import time
import argparse

def list_serial_ports():
    print("Listing available serial ports...")
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(f"{port.device}: {port.description}")

def open_serial_connection(port, baud_rate):
    print(f"Attempting to open serial connection on port {port} at {baud_rate} baud...")
    try:
        ser = serial.Serial(port, baud_rate, timeout=1)
        if ser.isOpen():
            print(f"Successfully connected to {port} at {baud_rate} baud.")
            return ser
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return None

def send_command(ser, command):
    print(f"Sending command: {command.hex()}")
    try:
        ser.write(command)
        print("Command sent, waiting for response...")
        time.sleep(0.5)  # Wait for response
        response = ser.read_all()
        print(f"Received response: {response.hex() if response else 'No response'}")
        return response
    except serial.SerialTimeoutException:
        print("Error: Timeout when writing to serial port.")
    except Exception as e:
        print(f"Error sending command: {e}")

def close_serial_connection(ser):
    if ser:
        print("Closing serial connection...")
        ser.close()
        print("Serial connection closed.")

def main():
    print("Parsing command line arguments...")
    parser = argparse.ArgumentParser(description="ViewSonic PX701-4K Projector RS232 Command Line Control.")
    parser.add_argument("-l", "--list", action="store_true", help="List available serial ports")
    parser.add_argument("-p", "--port", help="Serial port (e.g., COM3, /dev/ttyUSB0)")
    parser.add_argument("-b", "--baud", type=int, default=9600, help="Baud rate (default: 9600)")
    subparsers = parser.add_subparsers(dest="action", help="Sub-command help")

    # Write command parser
    write_parser = subparsers.add_parser("write", help="Write command to the projector")
    write_parser.add_argument("command_bytes", nargs="+", help="Command bytes in hexadecimal format (e.g., 0xAA 0x00 0x01 0x34)")

    args = parser.parse_args()

    if args.list:
        list_serial_ports()
        return

    if not args.port or not args.action:
        print("Error: Port and action must be specified unless listing ports.")
        return

    print(f"Port: {args.port}, Baud Rate: {args.baud}, Action: {args.action}")

    if args.action == "write":
        try:
            # Convert command bytes from string to actual bytes
            command_packet = bytes(int(byte, 16) for byte in args.command_bytes)
            print(f"Generated command packet: {command_packet.hex()}")
        except ValueError as e:
            print(f"Error converting command bytes: {e}")
            return

        # Open the serial connection
        ser = open_serial_connection(args.port, args.baud)
        if not ser:
            print("Failed to open serial connection.")
            return

        # Send the command
        response = send_command(ser, command_packet)
        if response:
            print("Response:", response.hex())
        else:
            print("No response received from the projector.")

        # Close the connection
        close_serial_connection(ser)

if __name__ == "__main__":
    print("Starting ViewSonic PX701-4K Projector RS232 Command Line Control...")
    main()
    print("Program finished.")