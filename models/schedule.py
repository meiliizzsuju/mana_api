from main import db

class Massage_Schedule(db.Model):
    __tablename__ = "massage_schedule"

    schedule_id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey("bookings.booking_id"), nullable=False)
    therapist_id = db.Column(db.Integer, db.ForeignKey("therapists.therapist_id"), nullable=False)
    treatment_id = db.Column(db.Integer, db.ForeignKey("treatments.treatment_id"), nullable=False)