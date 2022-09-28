from machine import Pin, Timer
from time import sleep, ticks_ms

cycle = 60 * 60                # full cycle length in minutes * 60
duty_time = 15 * 60            # time of working in minutes * 60

GREEN = Pin(13, Pin.OUT)    # onboard LED
RELAY = Pin(12, Pin.OUT)    # onboard relay

on = Timer(0)
off = Timer(-1)

# off.deinit()
# on.deinit()

def working(x):
    RELAY.on()
    GREEN.off()     # inverted
    print('on:  {}'.format(int(ticks_ms()/1000)))

def waiting(x):
    RELAY.off()
    GREEN.on()      # inverted
    print('off: {}'.format(int(ticks_ms()/1000)))

on.init(period=cycle * 1000,
        mode=Timer.PERIODIC,
        callback=working)

sleep(duty_time)

off.init(period=cycle * 1000,
         mode=Timer.PERIODIC,
         callback=waiting)
