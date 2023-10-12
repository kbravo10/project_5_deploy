#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Inventory, Med_times, Client, Doctor, Medication, Employee, Report

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        Inventory.query.delete()
        Med_times.query.delete()
        Client.query.delete()
        Doctor.query.delete()
        Medication.query.delete()
        Employee.query.delete()
        Report.query.delete()

        #add data to medication class
        meds = {
            'Adderall':'Adderall is used to treat attention deficit hyperactivity disorder (ADHD) and narcolepsy.',
            'Atorvastatin':"It's used to help lower cholesterol and fat levels in your blood",
            'Levothyroxine':"Levothyroxine is a man-made hormone that is used to treat hypothyroidism. Hypothyroidism is a condition where your thyroid doesn't produce enough thyroid hormone naturally.",
            'Lisinopril':"Lisinopril is a type of angiotensin-converting enzyme (ACE) inhibitor used to treat high blood pressure.",
            'Metformin' : "Metformin is used to treat type 2 diabetes",
            'Albuterol' :"Albuterol is used to treat bronchospasm, which is when your airways spasm and tighten and make it hard to breathe.",
            'Gabapentin' : "Gabapentin works in your brain to prevent seizures and relieve certain types of pain. It is used to treat epilepsy, nerve pain after shingles, and moderate to severe restless leg syndrome. It's also sometimes used to treat other types of nerve pain, fibromyalgia, hot flashes after menopause, anxiety, mood disorders, irritable bowel syndrome (IBS), alcohol withdrawal, migraines, itching, and insomnia.",
            'Omeprazole' : "Omeprazole is used to treat conditions that result from too much acid in your stomach.",
            'Losartan' : "Losartan is the fourth in the top 10 medicines used to treat high blood pressure."
        }
        medications = []
        for i in range(len(meds)):
            med = Medication(
                name = [i for i in meds][i],
                medication_use = [values for values in meds.values()][i],
            )
            db.session.add(med)
            medications.append(med)
        


        #inventory object
        inventory_list = [
            "Adhesive bandages",
            "Bandages",
            "Gauze pads",
            "Tape",
            "Scissors",
            "Tweezers",
            "Thermometer",
            "Pain reliever",
            "Antiseptic wipes",
            "Cold compress",
            "Hot compress",
            "First aid manual"
        ]

        inventory_all = []
        for i in range(len(inventory_list)):
            inventory = Inventory(
                inventory = inventory_list[i],
                count_inventory = randint(1, 10),
                instructions = 'Consult doctor'
            )
            db.session.add(inventory)
            inventory_all.append(inventory)
        # db.session.add_all(inventory_all)

         

        #doctors object
        doctors_all = []
        for i in range(3):
            doc = Doctor(
                name = fake.unique.name(),
                email = fake.unique.email(),
                number = fake.phone_number()
            )
            db.session.add(doc)
            db.session.commit()
            doctors_all.append(doc)

        # clients object
        client_all =[]
        for i in range(5):
            doc = rc(doctors_all)
            client = Client(
                name = fake.unique.name(),
                age = randint(1, 100),
                image = 'data:image/jpeg;base64,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',
                bio = fake.paragraph()
            )
            client.doctor = doc
            db.session.add(doc)
            client_all.append(client)

        #add employee seed
        emails = [
        'userOne@doctork.com',
        'userTwo@doctork.com',
        'userThree@doctork.com',
        'userFour@doctork.com',
        ]
        employees = []
        for i in range(len(emails)):
            employee = Employee(
                name = fake.name(),
                username = emails[i],
                admin = randint(0,1),
                number = fake.phone_number()
            )
            employee.password_hash = "pass"
            db.session.add(employee)
            employees.append(employee)

        #med_times object
        med_times_all = []
        for client in client_all:
            for i in range(randint(2, 5)):
                meds = rc(medications)
                t = 4*i
                time = ''
                if t >= 12:
                    time = str(t) + ":00"
                else:
                    time = "0" + str(t) + ":00"
                mt = Med_times(
                    time_slot = time,
                    amount = 'NA',
                    signed_off = '------Not Signed Off------',
                )
                mt.clients = client
                mt.medications = meds
                med_times_all.append(mt)
        db.session.add_all(med_times_all)


        #reports
        report_types =[
            'small-injury',
            'end of shift',
            'emergency'
        ]
        reports_list = []
        for i in range(5):
            emp = rc(employees)
            report = Report(
                type_of_report = rc(report_types),
                context = fake.paragraph(),
                )
            report.employee = emp
            report.client = rc(client_all)
            reports_list.append(report)
        db.session.add_all(reports_list)


        db.session.commit()
        

