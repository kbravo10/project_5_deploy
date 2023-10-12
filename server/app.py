#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session, make_response, jsonify
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import Doctor, Client,Med_times,Medication,Inventory,Employee,Report

#allow the user to make an account
class Signup(Resource):
    def post(self):
        try:
            json = request.get_json()
            new_employee = Employee(
                name = json['name'],
                username = json['username'],
                admin = 0 
            )
            new_employee.password_hash = json['password']

            db.session.add(new_employee)
            db.session.commit()
            session['user_id'] = new_employee.id
            user_dict = {
                "name": new_employee.name,
                "username": new_employee.username,
                "id": new_employee.id,
            }
            return user_dict, 201
        except Exception:
            return {'errors': 'Unprocessable Entity'}, 422
   
    
#check if user logged in
class CheckSession(Resource):
    def get(self):
        user = Employee.query.filter(Employee.id == session.get("user_id")).first()
        if user:
            user_info = {
                'username': user.username,
                'name': user.name, 
                'id': user.id
            }
            return user.to_dict(), 200
        else:
            return {'errors': 'Unathorized'}, 401 

#login the user
class Login(Resource):
    def post(self):
        user = request.get_json()
        user_info = Employee.query.filter(Employee.username == user['username']).first()
        if user_info:
            if user_info.authenticate(user['password']) == True:
                user_dict = {
                    'name': user_info.name,
                    'id': user_info.id,
                }
                session["user_id"] = user_info.id
                return user_dict, 200
            else:
                return {"errors":"Unathorized"}, 401
        else:
                return {"errors":"Unathorized"}, 401



#logout route
class Logout(Resource):
    def delete(self):
        if session.get('user_id'):
            session['user_id'] = None
            return{}, 204
        else:
            return {"errors":"Unathorized"}, 401

#inventoury route
@app.route('/inventory')
def inventory():
    inventory = Inventory.query.all()
    if inventory:
        inventory_dict = [inv.to_dict() for inv in inventory]
        return inventory_dict, 200
    else:
        return {}, 204

class InventoryId(Resource):
    def patch(self, id):
        json = request.get_json()
        record = Inventory.query.filter(Inventory.id == id).first()
        if record:
            if json['action'] == 'decrease':
                record.count_inventory = record.count_inventory - 1
            else:
                record.count_inventory = 10
            db.session.add(record)
            db.session.commit()
            return {},204
        else:
            return {}, 200


#medication schedule route
class MedicationTimes(Resource):
    def get(self):
        med_times = Med_times.query.order_by(Med_times.time_slot).all()
        med_times_dict = [mt.to_dict() for mt in med_times]
        client = Client.query.all()
        client_basic_name = [c.name for c in client]
        medication = Medication.query.all()
        med_name = [m.name for m in medication]
        med_time_response = {
            'med_time': med_times_dict,
            'client_name': client_basic_name,  
            'med_names' : med_name
        }
        return med_time_response , 200
    def post(self):
        json = request.get_json()
        try:
            client = Client.query.filter(Client.name == json['client_name']).first()
            client_id = client.id
            med = Medication.query.filter(Medication.name == json['medication_name']).first()
            medication_id = med.id
            time = ""
            if int(json['time_slot']) < 10:
                time = '0' + json['time_slot'] + ':00'
            else:
                time = json['time_slot'] + ':00'
            new_time_slot = Med_times(
                time_slot = time,
                amount = 'NA',
                signed_off = '------Not Signed Off------',
                client_id = client_id,
                medication_id = medication_id
            )
            db.session.add(new_time_slot)
            db.session.commit()
            return {},205
        except Exception:
            return {'errors': 'Unprocessable Entity'}, 422

class MedicationTimesId(Resource):
    def get(self, id):
        med_time=Med_times.query.filter(Med_times.id == id).first()
        med_time_dict = med_time.to_dict()
        return med_time_dict, 200 
    def patch(self, id):
        record = Med_times.query.filter(Med_times.id == id).first()
        record.signed_off = request.get_json()['signed_off']
        request_dict = record.to_dict()
        db.session.add(record)
        db.session.commit()
        return {}, 204
    def delete(self, id):
        record = Med_times.query.filter(Med_times.id == id).first()
        db.session.delete(record)
        db.session.commit()
        return {'message': 'DELETE SUCCESSFUL'}, 200

@app.route('/clients')
def clients():
    clients = Client.query.all()
    client_dict = [c.to_dict() for c in clients]    
    return client_dict,200
    
class ClientID(Resource):
    def get(self, id):
        client = Client.query.filter(Client.id == id).first()
        medications = []
        for meds in client.medications:
            medications.append(meds.medications.name)
        client_dict = {
            'id': client.id,
            'name': client.name,
            'age': client.age,
            'image': client.image,
            'bio' : client.bio,
            'doctor': client.doctor.name,
            'doctor_phone': client.doctor.number,
            'doctor_id': client.doctor_id,
            'medications': medications,
        }
        return client_dict, 200 

@app.route('/doctors')
def doctors():
    doctors = Doctor.query.all()
    doctor_dict = [doc.to_dict() for doc in doctors]
    return doctor_dict,200

class DoctorId(Resource):
    def get(self, id):
        doctor = Doctor.query.filter(Doctor.id == id).filter()
        return doctor.to_dict(), 200

@app.route('/medications')
def medications():
    medications = Medication.query.all()
    medications_dict = [med.to_dict() for med in medications]
    return medications_dict, 200


@app.route('/employees')
def employees():
    if session.get('user_id'):
        user = Employee.query.filter(Employee.id == session['user_id']).first()
        if user.admin == 1:
            employees = Employee.query.all()
            employee_dict = [employee.to_dict() for employee in employees]
            return employee_dict, 200
        else:
            return {'errors': 'Access denied'}, 404
    return {'errors': 'Access denied'}, 404


class Reports(Resource):
    def get(self):
        report = Report.query.all()
        report_dict = [r.to_dict() for r in report]
        client = Client.query.all()
        client_name = [c.name for c in client]
        reports_response = {
            'report': report_dict,
            'client_name': client_name,
        }
        return reports_response, 200
    def post(self):
        json = request.get_json()
        try: 
            client_name = Client.query.filter(Client.name == json['client_name']).first()
            new_report = Report(
                type_of_report= json['type_of_report'],
                context= json['context'],
                client_name= client_name.name,
                employee_id= session.get('user_id')
            )
            db.session.add(new_report)
            db.session.commit()
            return {'message': 'object created'}, 201
        except Exception:
            return {'errors': 'Unprcessible '}
class ReportId(Resource):
    def get(self, id):
        report = Report.query.filter(Report.id == id).first()
        return report.to_dict(), 200

api.add_resource(Login, '/login', endpoint='login')
api.add_resource(CheckSession, '/check_session')
api.add_resource(ClientID, '/clients/<int:id>', endpoint = 'clients/id')
api.add_resource(MedicationTimes, '/medication_times', endpoint='medication_times')
api.add_resource(MedicationTimesId, '/medication_times/<int:id>', endpoint='medication_times/<int:id>')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(Reports, '/reports', endpoint='reports')
api.add_resource(InventoryId, '/inventory/<int:id>', endpoint='inventory/<int:id>')
api.add_resource(ReportId, '/reports/<int:id>', endpoint='reports/<int:id>')
api.add_resource(DoctorId, '/doctors/<int:id>', endpoint = 'doctors/<int:id>')





if __name__ == '__main__':
    app.run(port=5555, debug=True)

