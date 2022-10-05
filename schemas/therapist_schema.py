from main import ma
from marshmallow import fields

class TherapistSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["therapist_id", "name"]


#just the single schema for log in purposes
therapist_schema = TherapistSchema()
therapists_schema = TherapistSchema(many=True)
