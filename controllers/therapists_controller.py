from flask import Blueprint, jsonify, request
from main import db
from models.therapist import Therapist
from schemas.therapist_schema import therapist_schema, therapists_schema
# from flask_jwt_extended import jwt_required

therapists = Blueprint('therapists', __name__, url_prefix="/therapists")


@therapists.route("/", methods=["GET"])
def get_therapists():
    # get all the therapists from the database
    therapists_list = Therapist.query.all()
    result = therapists_schema.dump(therapists_list)
    return jsonify(result)

@therapists.route("/<int:id>", methods=["GET"])
def get_therapist(id):
    #search therapist by id (primary key)
    therapist = Therapist.query.get(id)

    #check if we found an therapist
    if not therapist:
        return {"error": "therapist id not found"}

    #serialise the result in a single therapist schema
    result = therapist_schema.dump(therapist)
    return jsonify(result) 

#POST an therapist
@therapists.route("/", methods=["POST"])
# @jwt_required()
def create_therapist():
    #get the values from the request and load them with the single schema
    therapist_fields = therapist_schema.load(request.json)
    #create a new Therapist object
    therapist = Therapist(
        name = therapist_fields["name"]
    )

    db.session.add(therapist)
    #store in the database and save the changes 
    db.session.commit()

    return jsonify(therapist_schema.dump(therapist))

#DELETE and therapist
@therapists.route("/<int:id>", methods=["DELETE"])
# @jwt_required()
def delete_therapist(id):
    #search therapist by id (primary key)
    therapist = Therapist.query.get(id)
    #get a list of therapists filtering by the given criteria. first will return the first match instead of a returning a list
    #therapist = Therapist.query.filter_by(therapist_id=id).first()
    #check if we found an therapist
    if not therapist:
        return {"error": "therapist id not found"}

    # delete the therapist from the database
    db.session.delete(therapist)
    #save the changes in the database
    db.session.commit()

    return {"message": "Therapist removed successfully"}