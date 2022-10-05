from main import ma
from marshmallow import fields

class BookingSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["booking_id", "date", "time", "massage_duration","customer_id","customers"]
    # Schema is defined as a String, to avoid te circular import error 
    customers = fields.Nested("CustomerSchema", only=("fist_name","last_name", "phone_number","email"))

#single book schema
booking_schema = BookingSchema()
#multiple_schema
bookings_schema = BookingSchema(many=True)