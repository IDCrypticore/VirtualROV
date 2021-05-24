import os
import sys
import schedule
import time

# This script has to by run as super user (sudo python3 usb-state.py)

def release_battery():
    with open('/sys/class/regulator/regulator.13/state', 'r+') as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        f.write(content.replace('enabled', 'disabled'))

def charge_battery():
    with open('/sys/class/regulator/regulator.13/state', 'r+') as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        f.write(content.replace('disabled', 'enabled'))

# Search the state file for the word "enabled",
# If true it runs the release_battery definition to replace the word with "disabled"
# Else it runs the charge_battery definition to replace "disabled" with "enabled"

def check_state():
    with open('/sys/class/regulator/regulator.13/state', 'r+') as f:
        if 'enabled' in f.read():
            print('Releasing battery')
            release_battery()
        else:
            print('Charging battery')
            charge_battery()

# For every n minutes: schedule.every(n).minutes.do(check_state)
# For every n hour: schedule.every(n).hour.do(check_state)
# For every day at 12 or 00: schedule.every().day.at("00:00").do(check_state)
schedule.every(10).seconds.do(check_state)

while True:
    schedule.run_pending()
    time.sleep(1)
