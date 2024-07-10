from typing import Dict
from src.drivers.email_sender import send_email
import uuid

class TripCreator:
    def __init__(self, trip_repository, emails_repository) -> None:
        self.__trip_repository = trip_repository
        self.__emails_repository = emails_repository

    def create(self, body) -> Dict:
        try:
            emails = body.get("emails_to_invite")

            trip_id = str(uuid.uuid4())
            # tirando os objetos do body e colocando em outro
            # é tipo o ...array do JS
            trip_infos = {**body, "id": trip_id}
            print(trip_infos)
            self.__trip_repository.create_trip(trip_infos)

            if emails:
                for email in emails:
                    self.__emails_repository.registry_email({
                        "email": email,
                        "trip_id": trip_id,
                        "id": str(uuid.uuid4()),
                    })

            send_email(
                [body["owner_email"]],
                f"http://localhost:3000/trips/{trip_id}/confirm"
            )

            return {
                "body": {
                    "id": trip_id,
                },
                "status_code": 201, #codigo para criado com sucesso
            }
        except Exception as exception:
            return {
                "body": {
                    "error": "Bad Request",
                    "message": str(exception),
                },
                "status_code": 400, #codigo de bad request
            }
