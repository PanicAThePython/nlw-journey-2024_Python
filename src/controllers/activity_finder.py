from typing import Dict

class ActivityFinder:
    def __init__(self, activity_repository) -> None:
        self.__activity_repository = activity_repository

    def find_activities_from_trip(self, trip_id: str) -> Dict:
        try:
            activities = self.__activity_repository.find_activities_from_trip(trip_id)
            
            formatted_activities = []

            for act in activities:
                formatted_activities.append({
                    "id": act[0],
                    "title": act[2],
                    "occurs_at": act[3],
                })
                        
            return {
                "body": {
                    "participants": formatted_activities
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
