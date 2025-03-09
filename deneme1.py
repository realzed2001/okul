import Adafruit_CharLCD as LCD
import Adafruit_GPIO.I2C as I2C

# Define I2C address and bus number
i2c_address = 0x27  # Change this to your I2C address
i2c_busnum = 1      # Change this to your I2C bus number if necessary

# Initialize the I2C interface
i2c = I2C.get_i2c_device(i2c_address, busnum=i2c_busnum)

# Define LCD column and row size for 20x4 LCD.
lcd_columns = 20
lcd_rows = 4

# Initialize the LCD using the I2C interface
lcd = LCD.Adafruit_CharLCDBackpack(address=i2c_address, busnum=i2c_busnum)

# Write "Merhaba" to the LCD.
lcd.clear()
lcd.message('Merhaba')

# Wait 5 seconds
import time
time.sleep(5)

# Clear the LCD screen
 