
import os
import time
import schedule

def put():
    with open('/home/crypticore/putnam/jumbo', 'r+') as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        f.write(content.replace('enabled', 'disabled'))

def nam():
    with open('/home/crypticore/putnam/jumbo', 'r+') as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        f.write(content.replace('disabled', 'enabled'))

def putnam():
    with open('/home/crypticore/putnam/jumbo', 'r+') as f:
        if 'enabled' in f.read():
            print('Releasing battery')
            put()
        else:
            print('Charging battery')
            nam()

# For every n minutes: schedule.every(n).minutes.do(putnam)
# For every n hour: schedule.every(n).hour.do(putnam)
# Every day at 12 or 00: schedule.every().day.at("00:00").do(putnam)
schedule.every(10).seconds.do(putnam)

while True:
    schedule.run_pending()
    time.sleep(1)
