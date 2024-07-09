from typing import Dict
class TripConfirmer:
    def __init__(self, trip_repository) -> None:
        self.__trip_repository = trip_repository

    def confirm(self, trip_id) -> Dict:
        try:
            self.__trip_repository.update_trip_status(trip_id)
            return {
                "body": None,
                "status_code": 204 #no content
            }
        except Exception as exception:
            return {
                "body": {
                    "error": "Bad Request",
                    "message": str(exception),
                },
                "status_code": 400, #codigo de bad request
            }