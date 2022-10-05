from main import db

class Booking(db.Model):
    __tablename__="bookings"
    booking_id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date())
    time = db.Column(db.Time())
    massage_duration = db.Column(db.String())
    # FK
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.customer_id"))
    massage_schedule = db.relationship(
        "Massage_Schedule",
        backref = "bookings",
        cascade="all, delete"
    )