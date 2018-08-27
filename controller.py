from evdev import InputDevice, categorize, ecodes

#creates object 'gamepad' to store the data
#you can call it whatever you like
#identify your game controller by typing: ls -l /dev/input
# or: python -m evdev.evtest

gamepad = InputDevice('/dev/input/event4')

#prints out device info at start
print(gamepad)

#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
    print(categorize(event))
