from main import db

class Customer(db.Model):
    __tablename__ = "customers"

    customer_id = db.Column(db.Integer, primary_key=True)
    fist_name = db.Column(db.String(), nullable=False, unique=True)
    last_name = db.Column(db.String(), nullable=False, unique=True)
    phone_number = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    booking = db.relationship(
        "Booking",
        backref = "customers",
        cascade="all, delete"
    )