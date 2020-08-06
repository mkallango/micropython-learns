python -m pip install esptool
pythom -m pip install adafruit-ampy
python -m esptool --port COM3 erase_flash
python -m esptool --port COM3 --baud 115200 write_flash --flash_mode dio --flash_size=detect 0x0 esp8266-20191220-v1.12.bin