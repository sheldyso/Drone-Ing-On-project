import sqlite3 as sq3
import numpy as np
#import timeit
import os
import robomaster
from robomaster import robot
import multiprocessing as mp
import keyboard

# Note - Robomaster only works on python version 3.8.x

# ====================================================
# --- Configs ---

path = os.path.dirname(__file__)
os.chdir(path)


# ====================================================

class Database_Connection():
    def __init__(self, path : str) -> None:
        # Unity has axis:
        # X = forward
        # Y = up
        # Z = left
        self.__fetch_query = "SELECT xPos, yPos, zPos FROM dronePos"
        self.__connection = sq3.connect(path) #"../Unity/Python API testing/Assets/Scripts/drone.db"
        self.__cur = self.__connection.cursor()

    def fetch_all_movements(self) -> list:
        res = self.__cur.execute(self.__fetch_query)
        move_list = res.fetchall()
        # Flip y and z
        move_list = [(i[0], i[2], i[1]) for i in move_list]
        return move_list
    
    def fetch_one(self):
        res = self.__cur.execute(self.__fetch_query)
        list_items = res.fetchall()
        element = list_items[-1] # Get last element
        return list(element)[1:] # Slicing out the move_id as it is irrelevant. Returns most recent x, y, z pos in database

    def flush_database(self):
        self.__cur.execute("DELETE FROM dronePos")

class Commander():
    """
    # Drone Command Controller
    For the University of Gloucestershire Drone-ing on project.

    ## Description
    
    """
    def __init__(self, database_path : str = None) -> None:
        self.__drone = robot.Drone()
        self.__okay = self.__drone.initialize()
        self.__drone_flight = self.__drone.flight
        #self.__drone_camera = self.__drone.camera
        #self.__drone_battery = self.__drone.battery
        self.state_okay = True
        #self.__db_conn = Database_Connection()
        self.__w_pool = mp.Pool(2)
        self.old_xpos = 0.0
        self.old_ypos = 0.0
        self.old_zpos = 0.0
        self.x_pos = 0.0
        self.y_pos = 0.0
        self.z_pos = 0.0
        if database_path != None:
            self.__db_conn = Database_Connection(database_path)
            self.__positions = self.__db_conn.fetch_all_movements()
            self.current_index = 1

        self.is_airborn : bool = False
        self.is_grounded : bool = True

    def move_to_next(self) -> bool:
        """Move to next position in the coordinate space.
        Returns true if succesful"""
        #get positions
        xyz = self.__positions[self.current_index]
        x = xyz[0] * 25
        y = xyz[1] * 25
        # Hold 30 cm above ground
        z = 1
        successful = self.__drone_flight.go(x , y , z , speed=50 , mid=None , retry=False).wait_for_completed()
        if successful == True:
            self.current_index += 1
        
        return successful
        

    def move_to_previous(self) -> bool:
        """Move to previous position in the coordinate space.
        Returns true if succesful"""
        if self.current_index != 0:
            self.current_index -= 1
            xyz = self.__positions[self.current_index]
            x = xyz[0]
            y = xyz[1]
            # Hold 30 cm above ground
            z = 1
            successful = self.__drone_flight.go(x , y , z , speed=10 , mid=None , retry=True).wait_for_completed()
            return successful



    def takeoff(self) -> bool:
        """Returns True if completed and False for action timeout"""
        successful = self.__drone_flight.takeoff().wait_for_completed()
        self.is_grounded = False
        self.is_airborn = True
        return successful

    def land(self):
        """Returns True if completed and False for action timeout"""
        successful = self.__drone_flight.land().wait_for_completed()
        self.is_grounded = True
        self.is_airborn = False
        return successful
        
#db_conn = Database_Connection()
#print(db_conn.fetch_all_movements())