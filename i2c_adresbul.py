import subprocess

def find_i2c_addresses():
    try:
        # Run the i2cdetect command to find I2C addresses
        result = subprocess.run(['i2cdetect', '-y', '1'], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    find_i2c_addresses()