from main import ma
from marshmallow import fields


class ScheduleSchema(ma.Schema):
    class Meta:
        ordered=True
        fields = ["schedule_id", "booking_id","bookings", "therapist_id", "therapists", "treatment_id","treatments"]
    bookings = fields.Nested("BookingSchema", only=("date", "time", "massage_duration","customer_id","customers"))
    therapists = fields.Nested("TherapistSchema", only=("name",))
    treatments = fields.Nested("TreatmentSchema", only=("treatment_name","treatment_description"))



schedule_schema = ScheduleSchema()
schedules_schema = ScheduleSchema(many=True)
