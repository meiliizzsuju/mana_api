from flask import Blueprint, jsonify, request
from main import db
from models.booking import Booking
from schemas.booking_schema import booking_schema, bookings_schema
from datetime import date

bookings = Blueprint('bookings', __name__, url_prefix="/bookings")


@bookings.route("/", methods=["GET"])
def get_bookings():

    if request.query_string:
        # search for booking for today [today]
        if request.args.get('bydate') == 'today':
            today = date.today()
            filtered_bookings_list = Booking.query.filter_by(date= today)
            result = bookings_schema.dump(filtered_bookings_list)
            if len(result) <1 :
                result = {"message": "Nothing based on that searching criteria"}
                return jsonify(result), 200
            return jsonify(result), 200
        elif request.args.get('bydate'): #by specific date format [yyyy-mm-dd]
            filtered_bookings_list = Booking.query.filter_by(date= request.args.get('bydate'))
            result = bookings_schema.dump(filtered_bookings_list)
            if len(result) <1 :
                result = {"message": "Nothing based on that searching criteria"}
                return jsonify(result), 200
            return jsonify(result), 200
        else:
            return {"message": "Nothing based on that searching criteria"}
    
    # get all the bookings from the database
    bookings_list = Booking.query.all()
    result = bookings_schema.dump(bookings_list)
    return jsonify(result)

@bookings.route("/<int:id>", methods=["GET"])
def get_booking(id):
    #search booking by id (primary key)
    booking = Booking.query.get(id)

    #check if we found an booking
    if not booking:
        return {"error": "booking id not found"}

    #serialise the result in a single booking schema
    result = booking_schema.dump(booking)
    return jsonify(result) 

#POST an booking
@bookings.route("/", methods=["POST"])
# @jwt_required()
def create_booking():
    #get the values from the request and load them with the single schema
    booking_fields = booking_schema.load(request.json)
    #create a new Booking object
    booking = Booking(
        date = booking_fields["date"],
        time= booking_fields["time"],
        massage_duration= booking_fields["massage_duration"],
        customer_id= booking_fields["customer_id"],
    )

    db.session.add(booking)
    #store in the database and save the changes 
    db.session.commit()

    return jsonify(booking_schema.dump(booking))

#DELETE and booking
@bookings.route("/<int:id>", methods=["DELETE"])
# @jwt_required()
def delete_booking(id):
    #search booking by id (primary key)
    booking = Booking.query.get(id)
    #get a list of bookings filtering by the given criteria. first will return the first match instead of a returning a list
    #booking = Booking.query.filter_by(booking_id=id).first()
    #check if we found an booking
    if not booking:
        return {"error": "booking id not found"}

    # delete the booking from the database
    db.session.delete(booking)
    #save the changes in the database
    db.session.commit()

    return {"message": "Booking removed successfully"}