from smbus2 import SMBus
from RPLCD.i2c import CharLCD

# Define I2C address and bus number
i2c_address = 0x27  # Change this to your I2C address
i2c_busnum = 1      # Change this to your I2C bus number if necessary

# Initialize the I2C interface
bus = SMBus(i2c_busnum)

# Define LCD column and row size for 20x4 LCD.
lcd_columns = 20
lcd_rows = 4

# Initialize the LCD using the I2C interface
lcd = CharLCD(i2c_expander='PCF8574', address=i2c_address, port=i2c_busnum,
              cols=lcd_columns, rows=lcd_rows, charmap='A00', auto_linebreaks=True)
lcd.clear()
lcd.cursor_pos = (0, 0) # ilk sayı satır, ikinci sayı sütun, 0enüst 3enalt
# Write "Merhaba" to the LCD.
lcd.write_string('Merhaba')
lcd.cursor_pos = (1, 0)
lcd.write_string('iyidir bea')

# Wait 5 seconds
import time
time.sleep(5)

# Clear the LCD screen
#lcd.clear()