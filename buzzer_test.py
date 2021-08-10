from time import sleep
import gpiozero as zero
#from gpiozero.tones import Tone

#range = 60
buzzer = zero.Buzzer(21)
buzzer.on()

while True:
#	buzzer.beep()
#	buzzer.play(Tone.from_midi(range))
#	range += 1
	buzzer.toggle()
	sleep(.1)
