from typing import Dict

class ParticipantsFinder:
    def __init__(self, participant_repository) -> None:
        self.__participant_repository = participant_repository

    def find_participants_from_trip(self, trip_id: str) -> Dict:
        try:
            participants = self.__participant_repository.find_participants_from_trip(trip_id)
            
            formatted_participants = []

            for p in participants:
                formatted_participants.append({
                    "id": p[0],
                    "name": p[1],
                    "is_confirmed": p[2],
                    "email": p[3],
                })
                #tá com o objt desse jeito por causa do JOIN
                        
            return {
                "body": {
                    "participants": formatted_participants
                },
                "status_code": 200
            }
        except Exception as exception:
            return {
                "body": {
                    "error": "Bad Request",
                    "message": str(exception),
                },
                "status_code": 400, #codigo de bad request
            }
