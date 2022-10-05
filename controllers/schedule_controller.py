from flask import Blueprint, jsonify, request
from main import db
from models.schedule import Massage_Schedule
from schemas.schedule_schema import schedule_schema, schedules_schema
# from flask_jwt_extended import jwt_required

schedules = Blueprint('schedules', __name__, url_prefix="/schedules")


@schedules.route("/", methods=["GET"])
def get_schedules():
    # get all the schedules from the database
    schedules_list = Massage_Schedule.query.all()
    result = schedules_schema.dump(schedules_list)
    return jsonify(result)

@schedules.route("/<int:id>", methods=["GET"])
def get_schedule(id):
    #search schedule by id (primary key)
    schedule = Massage_Schedule.query.get(id)

    #check if we found an schedule
    if not schedule:
        return {"error": "schedule id not found"}

    #serialise the result in a single schedule schema
    result = schedule_schema.dump(schedule)
    return jsonify(result) 

#POST an schedule
@schedules.route("/", methods=["POST"])
# @jwt_required()
def create_schedule():
    #get the values from the request and load them with the single schema
    schedule_fields = schedule_schema.load(request.json)
    #create a new Massage_Schedule object
    schedule = Massage_Schedule(
        booking_id= schedule_fields["booking_id"],
        therapist_id= schedule_fields["therapist_id"],
        treatment_id= schedule_fields["treatment_id"]
    )

    db.session.add(schedule)
    #store in the database and save the changes 
    db.session.commit()

    return jsonify(schedule_schema.dump(schedule))

#DELETE and schedule
@schedules.route("/<int:id>", methods=["DELETE"])
# @jwt_required()
def delete_schedule(id):
    #search schedule by id (primary key)
    schedule = Massage_Schedule.query.get(id)
    #get a list of schedules filtering by the given criteria. first will return the first match instead of a returning a list
    #schedule = Massage_Schedule.query.filter_by(schedule_id=id).first()
    #check if we found an schedule
    if not schedule:
        return {"error": "schedule id not found"}

    # delete the schedule from the database
    db.session.delete(schedule)
    #save the changes in the database
    db.session.commit()

    return {"message": "Massage_Schedule removed successfully"}