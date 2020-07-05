import sys
import serial
ser = serial.Serial('/dev/ttyUSB0', 500000)

gyro_x_last_sec = []
gyro_y_last_sec = []
gyro_z_last_sec = []

def handle_serial_input():
    while(True):
        try:
            # read gyro values from serial port
            x = ser.readline().decode().strip()
            # split into the three values
            gyro_x, gyro_y, gyro_z = x.split(',')

            # store gyro values
            gyro_x_last_sec.append(float(gyro_x))
            gyro_y_last_sec.append(float(gyro_y))
            gyro_z_last_sec.append(float(gyro_z))

            # trim gyro arrays          -- yes I know this is horribly inefficent
            while len(gyro_x_last_sec) > 1000:
                gyro_x_last_sec.pop(0)
            while len(gyro_y_last_sec) > 1000:
                gyro_y_last_sec.pop(0)
            while len(gyro_z_last_sec) > 1000:
                gyro_z_last_sec.pop(0)
        except Exception as e:
            print(e, file=sts.stderr)


def get_last_second():
    if len(gyro_x_last_sec) < 1000:
        return False
    else:
        return [gyro_x_last_sec, gyro_y_last_sec, gyro_z_last_sec]




