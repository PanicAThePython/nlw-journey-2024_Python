from sqlite3 import Connection
from typing import Dict, Tuple

class TripsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def create_trip(self, trip_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                insert into trips
                (id, destination, start_date, end_date, onwer_name, owner_email)
                values (?, ?, ?, ?, ?, ?)
            ''',
            (
                trip_infos["id"],
                trip_infos["destination"],
                trip_infos["start_date"],
                trip_infos["end_date"],
                trip_infos["onwer_name"],
                trip_infos["owner_email"],
            )
        )
        self.__conn.commit() #confirma q quer realizar a ação de cima
    
    def find_trip_by_id(self, trip_id: str) -> Tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                select * from trips where id = ?
            ''',
            (
                trip_id,
            )
        )
        trip = cursor.fetchone()
        return trip
    
    def update_trip_status(self, trip_id: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                update trips set status = 1 where id = ?
            ''',
            (
                trip_id,
            )
        )
        self.__conn.commit()