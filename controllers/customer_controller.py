from queue import Empty
from flask import Blueprint, jsonify, request
from main import db
from models.customer import Customer
from schemas.customer_schema import customer_schema, customers_schema
# from flask_jwt_extended import jwt_required

customers = Blueprint('customers', __name__, url_prefix="/customers")


@customers.route("/", methods=["GET"])
def get_customers():
    # if we have a query string
    if request.query_string:
        if request.args.get('fist_name'):
            filtered_customers_list = Customer.query.filter_by(fist_name= request.args.get('fist_name'))
            result = customers_schema.dump(filtered_customers_list)
            if len(result) <1 :
                result = {"message": "No customers based on that searching criteria"}
                return jsonify(result), 200
            return jsonify(result), 200
        elif request.args.get('last_name'):
            filtered_customers_list = Customer.query.filter_by(last_name= request.args.get('last_name'))
            result = customers_schema.dump(filtered_customers_list)
            if len(result) <1 :
                result = {"message": "No customers based on that searching criteria"}
                return jsonify(result), 200
            return jsonify(result), 200
        elif request.args.get('email'):
            filtered_customers_list = Customer.query.filter_by(email= request.args.get('email'))
            result = customers_schema.dump(filtered_customers_list)
            if len(result) <1 :
                result = {"message": "No customers based on that searching criteria"}
                return jsonify(result), 200
            return jsonify(result), 200
        else:
            return {"message": "No customer based on that searching criteria"}

    # get all the customers from the database
    customers_list = Customer.query.all()
    result = customers_schema.dump(customers_list)
    return jsonify(result)

@customers.route("/<int:id>", methods=["GET"])
def get_customer(id):
    #search customer by id (primary key)
    customer = Customer.query.get(id)

    #check if we found an customer
    if not customer:
        return {"error": "customer id not found"}

    #serialise the result in a single customer schema
    result = customer_schema.dump(customer)
    return jsonify(result) 

#POST an customer
@customers.route("/", methods=["POST"])
# @jwt_required()
def create_customer():
    #get the values from the request and load them with the single schema
    customer_fields = customer_schema.load(request.json)
    #create a new Customer object
    customer = Customer(
        fist_name= customer_fields["fist_name"],
        last_name= customer_fields["last_name"],
        phone_number= customer_fields["phone_number"],
        email= customer_fields["email"]
    )

    db.session.add(customer)
    #store in the database and save the changes 
    db.session.commit()

    return jsonify(customer_schema.dump(customer))

#DELETE and customer
@customers.route("/<int:id>", methods=["DELETE"])
# @jwt_required()
def delete_customer(id):
    #search customer by id (primary key)
    customer = Customer.query.get(id)
    #get a list of customers filtering by the given criteria. first will return the first match instead of a returning a list
    #customer = Customer.query.filter_by(customer_id=id).first()
    #check if we found an customer
    if not customer:
        return {"error": "customer id not found"}

    # delete the customer from the database
    db.session.delete(customer)
    #save the changes in the database
    db.session.commit()

    return {"message": "Customer removed successfully"}