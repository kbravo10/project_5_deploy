from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
import re



from config import db, bcrypt

# Models go here!

#create a class doctor
class Doctor(db.Model, SerializerMixin):
    __tablename__ = 'doctors'
    serialize_rules =['-clients.doctor',]

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    number = db.Column(db.String)

    clients = db.relationship('Client', backref = 'doctor')

    @validates('name')
    def validates_name(self, key, doctors):
        if len(doctors) != 0:
            return doctors
    
    @validates('email')
    def validates_email(self, key, doctors):
         if re.match(r"[^@]+@[^@]+\.[^@]+", doctors):
            return doctors

    def __repr__(self):
        return f'doctor: {self.name}, email: {self.email}, \nclients: {self.clients}'

#create a class client
class Client(db.Model, SerializerMixin):
    __tablename__ = 'clients'

    serialize_rules =['-doctor.clients', '-medications.clients', '-reports.client',]


    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable = False)
    age = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String)
    bio = db.Column(db.String)

    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    medications = db.relationship('Med_times', back_populates = 'clients')
    reports = db.relationship('Report', backref = 'client')

    @validates('name')
    def validates_name(self, key, clients):
        if len(clients) != 0:
            return clients

    @validates('age')
    def validates_age(self, key, clients):
        if 0 < clients < 120:
            return clients

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}, age: {self.age}, doctor id: {self.doctor_id}'

#create a class medication
class Medication(db.Model, SerializerMixin):
    __tablename__ = 'medications'
    serialize_rules =['-clients.medications',]

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, unique = True, nullable= False)
    medication_use = db.Column(db.String, nullable=False)

    clients = db.relationship('Med_times', back_populates='medications')

    @validates('name')
    def validate_name(self, key, medications):
        if len(medications) != 0:
            return medications
    
    @validates('medication_use')
    def validates_med_use(self, key, medications):
        if len(medications) > 8:
            return medications


    def __repr__(self):
        return f'name: {self.name}, usage: {self.medication_use}, clients: {self.clients}'


#create a class med times
class Med_times(db.Model, SerializerMixin):
    __tablename__ = 'med_times'
    serialize_rules =['-employee.med_times', '-clients.med_times', 
                      '-medications.med_times', '-clients.medications', '-medications.clients']

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    time_slot = db.Column(db.String, nullable=False)
    amount = db.Column(db.String)

    signed_off = db.Column(db.Integer, db.ForeignKey('employees.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    medication_id = db.Column(db.Integer, db.ForeignKey('medications.id'))
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    clients = db.relationship('Client', back_populates = 'medications')
    medications = db.relationship('Medication', back_populates = 'clients')

#create a class inventory
class Inventory(db.Model, SerializerMixin):
    __tablename__ = 'inventories'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    inventory = db.Column(db.String)
    count_inventory = db.Column(db.Integer)
    instructions = db.Column(db.String)

    @validates('inventory')
    def validate_inventory(self, key, inventories):
        if len(inventories) != 0:
            return inventories

    @validates('count_inventory')
    def validate_inv_count(self, key, inventories):
        if 0 <= inventories:
            return inventories
        else:
            return ValueError('number must be positive')
    
    @validates('instructions')
    def validate_instructions(self, key, inventories):
        if 10 < len(inventories) and inventories != None:
            return inventories
        else:
            return ValueError('Null or length to short')

#create a class Reports
class Report(db.Model, SerializerMixin):
    __tablename__ = 'reports'
    serialize_rules =['-employee.reports', '-client.reports']

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    type_of_report = db.Column(db.String, nullable=False)
    context = db.Column(db.String, nullable=False)

    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    client_name = db.Column(db.String, db.ForeignKey('clients.name'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('type_of_report')
    def validate_type(self, key, reports):
        if len(reports) != 0:
            return reports
    
    @validates('context')
    def validate_context(self, key, reports):
        if len(reports) > 25:
            return reports



#create a class employee
class Employee(db.Model, SerializerMixin):
    __tablename__ = 'employees'
    serialize_rules =['-med_times.employee', '-reports.employee']

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable = False)
    username = db.Column(db.String, unique=True, nullable = False)
    _password_hash = db.Column(db.String, nullable=False)
    admin = db.Column(db.Integer)
    number = db.Column(db.String)

    med_times = db.relationship('Med_times', backref = 'employee')
    reports = db.relationship('Report', backref = 'employee')


    @validates('name')
    def validates_name(self, key, employees):
        if len(employees) != 0:
            return employees
    
    @validates('_password_hash')
    def validates_password(self, key, employees):
        if len(employees) != 0:
            return employees

    @validates('username')
    def validates_email(self, key, employees):
         if re.match(r"[^@]+@[^@]+\.[^@]+", employees):
            return employees

    @hybrid_property
    def password_hash(self):
        return AttributeError()
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
