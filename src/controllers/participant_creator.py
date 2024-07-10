from typing import Dict
import uuid

class ParticipantCreator:
    def __init__(self, participant_repository, email_repository) -> None:
        self.__participant_repository = participant_repository
        self.__email_repository = email_repository

    def create(self, body, trip_id) -> Dict:
        try:
            participant_id = str(uuid.uuid4())
            email_id = str(uuid.uuid4())

            emails_infos = {
                "id": email_id,
                "email": body["email"],
                "trip_id": trip_id,
            }

            participant_infos = {
                "id": participant_id,
                "trip_id": trip_id,
                "emails_to_invite": email_id,
                "name": body["name"],
            }
            self.__email_repository.registry_email(emails_infos)
            self.__participant_repository.registry_participant(participant_infos)

            return {
                "body": {"participantId": participant_id},
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
