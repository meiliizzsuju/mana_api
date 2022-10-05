from main import db

class Therapist(db.Model):
    __tablename__ = "therapists"

    therapist_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    massage_schedule = db.relationship(
        "Massage_Schedule",
        backref= "therapists",
        cascade="all, delete"
    )