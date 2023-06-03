import keyboard
from drone_commands import Commander, Database_Connection
from interface import Display
import time
import os

dir = os.path.dirname(__file__)
os.chdir(dir)

app = True

# tuple of (x, y, z)
demo_path = [
    (10, 0, 10)
]

def setup():
    database_path = "drone.db"
    __db_conn = Database_Connection(database_path)
    __positions = __db_conn.fetch_all_movements()

    pass


def main():
    drone_c = Commander(database_path="drone.db")
    setup()
    
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