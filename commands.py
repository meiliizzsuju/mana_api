from flask import Blueprint
from main import db
from main import bcrypt
from models.booking import Booking
from models.customer import Customer
from models.schedule import Massage_Schedule
from models.therapist import Therapist
from models.treatment import Treatment
from datetime import date
from time import gmtime, strftime

db_commands = Blueprint("db", __name__)
# print("check db ===================>",db)

@db_commands.cli.command('create')
def create_db():
    # Tell SQLAlchemy to create all tables for all models in the physical DB
    db.create_all()
    print('Tables created')

@db_commands.cli.command('drop')
def drop_db():
    # Tell SQLAlchemy to drop all tables
    db.drop_all()
    print('Tables dropped')

@db_commands.cli.command('seed')
def seed_db():

    # start Treatment
    treatment1 = Treatment(
        treatment_name = "Massage1",
        treatment_description = "A mix of stretching, firm pressure and deep rhythmic movements along energy lines throughout your body."
    )
    db.session.add(treatment1)
    treatment2 = Treatment(
        treatment_name = "Massage2",
        treatment_description = "Breaking up your scar tissue or stiffness with deep/remedial massage."
    )
    db.session.add(treatment2)
    db.session.commit()
    # commit Treatment done



    
    # start Therapist
    therapist1 = Therapist(
        name = "Nickky"
    )
    db.session.add(therapist1)
    therapist2 = Therapist(
        name = "Jaroen"
    )
    db.session.add(therapist2)
    db.session.commit()
    # commit Therapist done





    #  start Customer
    customer1 = Customer(
        fist_name = "Ticha",
        last_name = "Tin",
        phone_number = "04 09 998 847",
        email = "tt@gmail.com"
    )
    db.session.add(customer1)
    customer2 = Customer(
        fist_name = "Jin",
        last_name = "Lim",
        phone_number = "04 09 998 777",
        email = "jl@gmail.com"
    )
    db.session.add(customer2)
    db.session.commit()
    # commit Customer done


    #  start Booking
    booking1 = Booking(
        date = date(day = 1, month = 10,year = 2022 ),
        time = strftime("%H:%M:%S", gmtime()),
        massage_duration = "1 hr",
        customer_id = customer1.customer_id
    )
    db.session.add(booking1)
    db.session.commit()
    # commit Booking done


    # start Massage_Schedule 
    schedule1 = Massage_Schedule(
        booking_id = booking1.booking_id,
        therapist_id = therapist1.therapist_id,
        treatment_id = treatment1.treatment_id
    )
    db.session.add(schedule1)
    db.session.commit()

    
    print("tables seeded")