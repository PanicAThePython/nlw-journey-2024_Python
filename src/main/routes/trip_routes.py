from flask import jsonify, Blueprint, request

trip_routes_bp = Blueprint("trip_routes", __name__)

#importacao de controllers
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_confirmer import TripConfirmer
from src.controllers.trip_finder import TripFinder

from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder

from src.controllers.activity_creator import ActivityCreator
from src.controllers.activity_finder import ActivityFinder

from src.controllers.participants_finder import ParticipantsFinder
from src.controllers.participant_confirmer import ParticipantConfirmer
from src.controllers.participant_creator import ParticipantCreator

#importacao de repos
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.activities_repository import ActivitiesRepository
from src.models.repositories.participants_repository import ParticipantsRepository

#importanto gerente conexoes
from src.models.settings.db_connection_handler import db_connection_handler

@trip_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    conn = db_connection_handler.get_connection()
    trip_repository = TripsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = TripCreator(trip_repository, emails_repository)

    response = controller.create(request.json)

    return jsonify(response["body"]), response["status_code"]

@trip_routes_bp.route("/trips/<tripId>", methods=["GET"])
def find_trip(tripId):
    conn = db_connection_handler.get_connection()
    trip_repository = TripsRepository(conn)

    controller = TripFinder(trip_repository)

    response = controller.find_trip_details(trip_id=tripId)

    return jsonify(response["body"]), response["status_code"]

@trip_routes_bp.route("/trips/<tripId>/confirm", methods=["GET"])
def confirm_trip(tripId):
    conn = db_connection_handler.get_connection()
    trip_repository = TripsRepository(conn)

    controller = TripConfirmer(trip_repository)

    response = controller.confirm(trip_id=tripId)
    return jsonify(response["body"]), response["status_code"]

@trip_routes_bp.route("/trips/<tripId>/links", methods=["POST"])
def create_trip_link(tripId):
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    controller = LinkCreator(link_repository)

    response = controller.create(request.json, trip_id=tripId)
    return jsonify(response["body"]), response["status_code"]

@trip_routes_bp.route("/trips/<tripId>/links", methods=["GET"])
def find_trip_link(tripId):
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    controller = LinkFinder(link_repository)

    response = controller.find(trip_id=tripId)
    return jsonify(response["body"]), response["status_code"]

@trip_routes_bp.route("/trips/<tripId>/invites", methods=["POST"])
def invite_to_trip(tripId):
    conn = db_connection_handler.get_connection()
    email_repository = EmailsToInviteRepository(conn)
    participant_repository = ParticipantsRepository(conn)

    controller = ParticipantCreator(participant_repository, email_repository) 

    response = controller.create(request.json, trip_id=tripId)
    return jsonify(response["body"]), response["status_code"]   

@trip_routes_bp.route("/trips/<tripId>/activities", methods=["POST"])
def create_activity(tripId):
    conn = db_connection_handler.get_connection()
    activity_repository = ActivitiesRepository(conn)

    controller = ActivityCreator(activity_repository) 

    response = controller.create(request.json, trip_id=tripId)
    return jsonify(response["body"]), response["status_code"]   

@trip_routes_bp.route("/trips/<tripId>/participants", methods=["GET"]) #o nome disso é blueprint
def get_trip_participants(tripId):
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantsRepository(conn)

    controller = ParticipantsFinder(participant_repository)

    response = controller.find_participants_from_trip(trip_id=tripId)
    return jsonify(response["body"]), response["status_code"]   

@trip_routes_bp.route("/trips/<tripId>/activities", methods=["GET"])
def get_trip_activities(tripId):
    conn = db_connection_handler.get_connection()
    activity_repository = ActivitiesRepository(conn)

    controller = ActivityFinder(activity_repository)

    response = controller.find_activities_from_trip(trip_id=tripId)
    return jsonify(response["body"]), response["status_code"]   

@trip_routes_bp.route("/participants/<participantId>/confirm", methods=["PATCH"])
def confirm_participant(participantId):
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantsRepository(conn)

    controller = ParticipantConfirmer(participant_repository)

    response = controller.confirm(participant_id=participantId)
    return jsonify(response["body"]), response["status_code"]
