#!/usr/bin/python3
import time
from huepy import *

print "\n"+"-"*60+"\n"

# Hue Alerts #
print bad("Bad alert!")
print good("Good alert!")
print info("Info alert!")
print run("Run alert!")
print que("Question alert!")
# Hue Alerts End #

print "\n"+"-"*60+"\n"
time.sleep(1)

# Hue Fonts #
print bg('Inverted Font')
print bold('Bold Font')
print italic('Italic Font')
print strike('Strike Font')
print under('Underline Font')
# Hue Fonts End #

print "\n"+"-"*60+"\n"
time.sleep(1)

# Hue Colors #
print white('White Text')
print grey('Grey Text')
print black('Black Text')
print cyan('Cyan Text')
print lightcyan('Light Cyan Text')
print blue('Blue Text')
print lightblue('Light Blue Text')
print green('Green Text')
print lightgreen('Light Green Text')
print purple('Purple Text')
print lightpurple('Light Purple Text')
print red('Red Text')
print lightred('Light Red Text')
print yellow('Yellow Text')
print orange('Orange Text')
# Hue Colors End #

print "\n"+"-"*60+"\n"
time.sleep(1)

# Hue Multi-Styles #
print bad(red('Bad alert, Red text!'))
print bad(orange(strike('Bad, Orange, Strike')))
# Hue Multi-Styles End #

print "\n"+"-"*60+"\n"
