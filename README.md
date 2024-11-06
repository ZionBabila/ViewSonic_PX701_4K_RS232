# Program to control the display

A python program to send commands to ViewSonic PX701-4K projector via serial connection (RS-232).

Tested on Windows 11.

## Installation and development

0. Using the command prompt, navigate to the directory containing this README.
1. `python --version` to check python version, should be 3.11 or later.
2. Have permissions to run scripts by running `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` in Powershell as adxmin.
3. `.\venv\Scripts\Activate.ps1` to activate the virtual environment.
4. `pip install -r requirements.txt` to install the required packages.

## Usage

- Find the serial port of the projector, it should be something like `COM4`.
- Run the script with `python main.py on --port COM4` to turn on the projector.
- Run the script with `python main.py off --port COM4` to turn off the projector.
- `deactivate` to deactivate the virtual environment.

## Notes

1. Use of crossover (null modem) cable required for use with control device if needed.