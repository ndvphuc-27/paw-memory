import keyboard
import sys
import time

pressed = False

# define hotkey pressed method
def setPressed():
    global pressed
    pressed = not pressed

# define hotkey
keyboard.add_hotkey("alt + a", setPressed) # You can change the hotkey combinaion

def main():
    currentTime = 0.0
    if len(sys.argv) < 2:
        print("Usage: py spambot.py <message> [ -d <delay in seconds> | -t <exit time in seconds> ]") # Provide the user with usage information
        return
    delay = 0.25
    exitTime = None
    if "-d" in sys.argv:
        try:
            if float(sys.argv[sys.argv.index("-d") + 1]) >= 0.01:
                delay = float(sys.argv[sys.argv.index("-d") + 1])
            else:
                print("Delay can't be lower than 0.01")
                return
            
        except:
            print("Only float values are allowed for delay attribute!") # Exit if the user didn't provide a valid number
            return

    if "-t" in sys.argv:
        try:
            exitTime = float(sys.argv[sys.argv.index("-t") + 1])
        except:
            print("Only float values are allowed for exit time attribute!") # Exit if the user didn't provide a valid number
            return

    msg = str(sys.argv[1]) + "\n"
    global pressed
    if exitTime is not None:
        exitTime -= delay
    while True:
        while pressed: # When the user has pressed the hotkey
            if exitTime is not None: # If user has got an exit time, bot exits when time is reached
                if currentTime <= exitTime:
                    keyboard.write(msg)
                    time.sleep(delay)
                    currentTime += delay
                else:
                    exit(code=0) # If user didn't enter exit time, bot spam till the user presses the hotkey again
            else:
                keyboard.write(msg)
                time.sleep(delay)


if __name__ == "__main__":
    main()