from typing import Dict
import uuid

class ActivityCreator:
    def __init__(self, activity_repository) -> None:
        self.__activity_repository = activity_repository

    def create(self, body, trip_id) -> Dict:
        try:
            activity_id = str(uuid.uuid4())
            activity_infos = {
                "id": activity_id,
                "trip_id": trip_id,
                "title": body["title"],
                "occurs_at": body["occurs_at"],
            }
            self.__activity_repository.registry_activity(activity_infos)

            return {
                "body": {"activityId": activity_id},
                "status_code": 201 #created
            }
        except Exception as exception:
            return {
                "body": {
                    "error": "Bad Request",
                    "message": str(exception),
                },
                "status_code": 400, #codigo de bad request
            }
