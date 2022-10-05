
Endpoint
URL Path: /customer
HTTP Request Verb: Post: to add new contact information for new customer
HTTP Request Verb: Get: to all customers and contact information

Endpoint
URL Path: /customers/id
HTTP Request Verb: Get: to return contact details of specific customer by id
HTTP Request Verb: Delete:  to delete contact details of specific customer by id
Error message: if id does not exist returns error message ‘customer id not found’

Endpoint
URL Path:/customers/first_name=
HTTP Request Verb: Get: returns customer id and info by filtering by first name 
Error message:  if name does not exist returns error message ‘no customer based on that search criteria’

Endpoint
URL Path:/customers/last_name=
HTTP Request Verb: Get: returns customer id and info by filtering by last name 
Error message:  if name does not exist returns error message ‘no customer based on that search criteria’

Endpoint
URL Path:/customers/email=
HTTP Request Verb: Get: returns customer id and info by filtering by email 
Error message:  if email does not exist returns error message ‘no customer based on that search criteria’



Endpoint
URL Path: /bookings
HTTP Request Verb: Post:  create a new booking by adding booking fields 
HTTP Request Verb: Get:  return all  bookings and booking info

Endpoint
URL Path: /bookings/id
HTTP Request Verb: Get:  return booking by id  
HTTP Request Verb: Delete:  delete booking by id  
Error message:  if no bookings by id returns ‘booking id not found’

Endpoint
URL Path: /bookings?bydate=today
HTTP Request Verb: Get: returns booking by current date
Error message: if no bookings on current date returns ‘nothing based on that search criteria’

Endpoint
URL Path: /bookings?bydate=YYYY=MM-DD
HTTP Request Verb: Get:  returns bookings by date 
Error message:  if no bookings on date returns ‘nothing based on that search criteria’

Endpoint
URL Path: /therapists
HTTP Request Verb: Post:  create a new therapists by adding  therapists fields
HTTP Request Verb: Get:  return all  therapists 
 
Endpoint
URL Path: /therapists/id
HTTP Request Verb: Get:  return  therapists by id  
HTTP Request Verb: Delete:  delete  therapists by id  
Error message:  if no therapists by id found returns ‘ therapists id not found’

Endpoint
URL Path: /treatments
HTTP Request Verb: Get: returns all treatments and treatment info
HTTP Request Verb: Post: create new treatment and add  treatment info


Endpoint
URL Path: /treatments/id
HTTP Request Verb: Get:  returns treatments and treatment info by id
HTTP Request Verb: Delete:  deletes treatment and treatment info by id 
Error message:  if no treatment id is found returns ‘treatment not found’

Endpoint
URL Path: /schedules
HTTP Request Verb: Get: returns all schedules and schedule info
HTTP Request Verb: Post: create new schedules and add  schedule info

Endpoint
URL Path: /schedules/id
HTTP Request Verb: Get:  returns schedules and schedule info by id
HTTP Request Verb: Delete:  deletes schedules and schedule info by id 
Error message:  if no schedule id is found returns ‘schedule id not found’


**R7	Detail any third party services**

Flask Blueprint - moduralises program code, adds URL prefix to create relevant path for browser

Flask Jsonify - converts data and objects into json format 

Flask Request - works in pairs where  calls  modularised objects and data that is received to the end point

Marshmallow - used to validate data and serialise objects into json format for webserver api

SQLAlchemy - An ORM for Python code to perform tasks with a database

Psycopg2 - used with python to adapt code for PostgeSQL database
