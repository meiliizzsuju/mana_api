from wsgiref import validate
from main import ma

class CustomerSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["customer_id", "fist_name", "last_name", "phone_number","email"]


customer_schema = CustomerSchema()
#multiple schema not necessary right now
customers_schema = CustomerSchema(many=True)