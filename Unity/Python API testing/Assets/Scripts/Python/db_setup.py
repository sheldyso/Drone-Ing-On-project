from sqlalchemy import create_engine, MetaData, Float, Integer, Table, Column
import os

__path = os.path.dirname(__file__)
os.chdir(__path)

def __main():
    engine = create_engine(f'sqlite:///../drone.db')
    md = MetaData()
    drone_position = Table(
        "dronePos", md,
        Column('move_id', Integer, primary_key = True),
        Column('xPos', Float),
        Column('yPos', Float),
        Column('zPos', Float),
    )
    md.create_all(engine)

if __name__ == '__main__':
    __main()