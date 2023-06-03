import keyboard
from drone_commands import Commander
import time
import os

dir = os.path.dirname(__file__)
os.chdir(dir)

app = True

def main():
    drone_c = Commander(database_path="drone.db")    
    while app:

        if keyboard.is_pressed('t'):
            print("T")
            drone_c.state_okay = drone_c.takeoff()
            # drone takes off
            time.sleep(0.05)

        elif keyboard.is_pressed('l'):
            print("L")
            drone_c.state_okay = drone_c.land()
            # land the drone
            time.sleep(0.05)

        elif keyboard.is_pressed('right arrow'):
            print("Right arrow pressed")
            drone_c.state_okay = drone_c.move_to_next()
            # Goes to next position
            time.sleep(0.05)

        elif keyboard.is_pressed('left arrow'):
            print("Left arrow pressed")
            drone_c.state_okay = drone_c.move_to_previous()
            # goes to previous position
            time.sleep(0.05)

        if drone_c.state_okay != True:
            drone_c.land()

if __name__ == "__main__":
    main()