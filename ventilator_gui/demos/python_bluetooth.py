'''import asyncio
from bleak import BleakScanner
async def run():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)
loop = asyncio.get_event_loop()
loop.run_until_complete(run())'''

import asyncio
from bleak import discover
import subprocess
p = subprocess.Popen(["hciconfig"], stdout=subprocess.PIPE)
for line in p.stdout:
    line = line.decode('utf-8').replace('\t','')
    content = line.split(' ')
    for i in range(len(content)):
        if content[i] == 'Address:':
            print('Bluetooth MAC Address is: '+ content[i+1])
async def run():
    devices = await discover()
    for d in devices:
        print(d)
loop = asyncio.get_event_loop()
loop.run_until_complete(run())