from main import db

class Treatment(db.Model):

    __tablename__="treatments"

    treatment_id = db.Column(db.Integer, primary_key = True)
    treatment_name = db.Column(db.String())
    treatment_description = db.Column(db.String(1000))
    massage_schedule = db.relationship(
        "Massage_Schedule",
        backref= "treatments",
        cascade="all"
    )


