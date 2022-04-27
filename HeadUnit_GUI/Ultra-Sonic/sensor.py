#!/usr/bin/python3

"""
    Program: HC-SR04 Sensor Demo (sensor.py)
    Author:  M. Heidenreich, (c) 2020
    Description:
    
    This code is provided in support of the following YouTube tutorial:
    https://youtu.be/JvQKZXCYMUM
    This example shows how to use the HC-SR04 sensor to activate a buzzer
    with Raspberry Pi.
    THIS SOFTWARE AND LINKED VIDEO TOTORIAL ARE PROVIDED "AS IS" AND THE
    AUTHOR DISCLAIMS ALL WARRANTIES INCLUDING ALL IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""

from signal import signal, SIGTERM, SIGHUP, pause
from time import sleep
from gpiozero import DistanceSensor, Buzzer

sensor = DistanceSensor(echo=20, trigger=21)
buzzer = Buzzer(24)

def safe_exit(signum, frame):
    exit(1)

try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)

    sensor.when_in_range = buzzer.on
    sensor.when_out_of_range = buzzer.off

    pause()

except KeyboardInterrupt:
    pass

finally:
    buzzer.close()
    sensor.close()
