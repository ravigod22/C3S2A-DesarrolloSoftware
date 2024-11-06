import re

class Appointment:
    
    def __init__(self, appointment_id, patient, doctor, datetime, status):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.datetime = self.validate_datetime(datetime)
        self.status = "scheduled"
    
    def validate_datetime(self, datetime):
        if not re.match(r'^\d{2}-\d{2}-\d{4}, \d{2}:\d{2}$', datetime):
            raise ValueError("La cita debe tener el formato DD-MM-YYYY, HH-MM")
        return datetime

    def schedule(self):
        datetime_validated = self.validate_datetime(self.datetime)
        if datetime_validated not in self.doctor.available_slots:
            raise ValueError("La cita no esta disponible")
        self.doctor.remove_available_slot(datetime_validated)
    
    def cancel(self):
        self.status = "cancelled"
        self.doctor.add_available_slot(self.datetime)
    
    def summary(self):
        return {
            "ID_APPOINTMENT: " : self.appointment_id,
            "PATIENT: " : self.patient,
            "DOCTOR: " : self.doctor,
            "DATE_TIME: " : self.datetime,
            "STATUS: " : self.status
        }
            