# Program to control the display

A python program to send commands to ViewSonic PX701-4K projector via serial connection (RS-232).

Tested on Windows 11.

## Development

1. `python -v` to check python version, should be 3.11 or later.
2. `pip install pyserial` to install the required package.
3. Powershell as admin, run `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` to allow activating the virtual env.
4. `.\venv\Scripts\Activate.ps1` to activate the virtual environment.
5. `pip install -r requirements.txt` to install the required packages.

## Usage

- Find the serial port of the projector, it should be something like `COM4`.
- Run the script with `python main.py on --port COM4` to turn on the projector.
- Run the script with `python main.py off --port COM4` to turn off the projector.
- `deactivate` to deactivate the virtual environment.
