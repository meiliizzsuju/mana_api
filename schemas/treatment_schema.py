from main import ma
from marshmallow import fields


class TreatmentSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["treatment_id","treatment_name","treatment_description"]
    # massage_schedule = fields.List(fields.Nested(scheduleS),only=("schedule_id","booking_id","therapist_id"))


treatment_schema = TreatmentSchema()
#multiple
treatments_schema = TreatmentSchema(many=True)