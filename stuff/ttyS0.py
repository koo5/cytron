import serial, time

a=serial.Serial("/dev/ttyS0",timeout=0)

def pause():
    time.sleep(0.5)
    pass

def bit(b):
    a.setRTS(1)
    pause()
    a.setDTR(not b)
    pause()
    a.setRTS(0)
    pause()
    a.setBreak(0)
    pause()
    a.setBreak(1)
    pause()

while 1:
    t = int(time.time())
    for i in range(0,8):
	bit(t&(1<<i))
    pause()
