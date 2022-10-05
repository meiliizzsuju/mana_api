from flask import Blueprint, jsonify, request
from main import db
from models.treatment import Treatment
from schemas.treatment_schema import treatment_schema, treatments_schema
# from flask_jwt_extended import jwt_required

treatments = Blueprint('treatments', __name__, url_prefix="/treatments")


@treatments.route("/", methods=["GET"])
def get_treatments():
    # get all the treatments from the database
    treatments_list = Treatment.query.all()
    result = treatments_schema.dump(treatments_list)
    return jsonify(result)

@treatments.route("/<int:id>", methods=["GET"])
def get_treatment(id):
    #search treatment by id (primary key)
    treatment = Treatment.query.get(id)

    #check if we found an treatment
    if not treatment:
        return {"error": "treatment id not found"}

    #serialise the result in a single treatment schema
    result = treatment_schema.dump(treatment)
    return jsonify(result) 

#POST an treatment
@treatments.route("/", methods=["POST"])
# @jwt_required()
def create_treatment():
    #get the values from the request and load them with the single schema
    treatment_fields = treatment_schema.load(request.json)
    #create a new Treatment object
    treatment = Treatment(
        # treatment_id = treatment_fields["treatment_id"],
        treatment_name = treatment_fields["treatment_name"],
        treatment_description= treatment_fields["treatment_description"]
    )

    db.session.add(treatment)
    #store in the database and save the changes 
    db.session.commit()

    return jsonify(treatment_schema.dump(treatment))

#DELETE and treatment
@treatments.route("/<int:id>", methods=["DELETE"])
# @jwt_required()
def delete_treatment(id):
    #search treatment by id (primary key)
    treatment = Treatment.query.get(id)
    #get a list of treatments filtering by the given criteria. first will return the first match instead of a returning a list
    #treatment = Treatment.query.filter_by(treatment_id=id).first()
    #check if we found an treatment
    if not treatment:
        return {"error": "treatment id not found"}

    # delete the treatment from the database
    db.session.delete(treatment)
    #save the changes in the database
    db.session.commit()

    return {"message": "Treatment removed successfully"}