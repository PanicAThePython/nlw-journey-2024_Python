from typing import Dict
class ParticipantConfirmer:
    def __init__(self, participant_repository) -> None:
        self.__participant_repository = participant_repository

    def confirm(self, participant_id) -> Dict:
        try:
            self.__participant_repository.update_participant_status(participant_id)
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