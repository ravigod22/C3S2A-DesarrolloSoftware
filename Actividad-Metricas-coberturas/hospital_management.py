from appointment import Appointment
from doctor import Doctor
from patient import Patient
from treatment import Treatment

class HospitalManagement:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = {}
        self.treatments = {}

    def manage_patients(self, action, patient_id, name=None, dob=None):
        if action == "create":
            if patient_id in self.patients:
                raise ValueError("El paciente ya existe")
            patient = Patient(patient_id, name, dob)
            self.patients[patient_id] = patient
            
        elif action == "update":
            if patient_id not in self.patients:
                raise ValueError("El paciente no exite")
            self.patients[patient_id].update_info(name, dob)
                    
        elif action == "delete":
            if patient_id not in self.patients:
                raise ValueError("El paciente no existe")
            del self.patients[patient_id]
            
        else:
            raise ValueError("Accion invalida")

    def manage_doctors(self, action, doctor_id, name=None ,specialization=None, slot=None):
        if action == "create":
            if doctor_id in self.doctors:
                raise ValueError("El doctor ya existe")
            doctor = Doctor(doctor_id, name, specialization, slot)
            self.doctors[doctor_id] = doctor
            
        elif action == "add_slot":
            if doctor_id not in self.doctors:
                raise ValueError("El doctor no existe")
            self.doctors[doctor_id].add_available_slot(slot)
            
        elif action == "remove_slot":
            if doctor_id not in self.doctors:
                raise ValueError("El doctor no existe")
            self.doctors[doctor_id].remove_available_slot(slot)
             
        elif action == "delete":
            if doctor_id not in self.doctors:
                raise ValueError("El doctor no existe, nada que eliminar")
            del self.doctors[doctor_id]
           
        else:
            raise ValueError("Acción invalida")

    def manage_appointments(self, action, appointment_id, patient_id, doctor_id, datetime):
        if action == "schedule":
            if appointment_id in self.appointments:
                raise ValueError("La cita ya existe")
            
            patient = self.patients.get(patient_id)
            doctor = self.doctors.get(doctor_id)
            
            if not patient or not doctor:
                raise ValueError("Paciente o doctor no encontrado")
            
            appointment = Appointment(appointment_id, patient, doctor, datetime,"scheduled")
            appointment.schedule()
            self.appointments[appointment_id] = appointment
            
        elif action == "cancel":
            if appointment_id not in self.appointments:
                raise ValueError("Cita no encontrada")
            
            self.appointments[appointment_id].cancel()
            
        else:
            raise ValueError("Accion invalida")

    def manage_treatments(self, action, treatment_id, patient_id, doctor_id, description, date):
        if action == "record":
            if treatment_id in self.treatments:
                raise ValueError("El tratamiento ya existe")
            
            patient = self.patients.get(patient_id)
            doctor = self.doctors.get(doctor_id)
            
            if not patient or not doctor:
                raise ValueError("Paciente o doctor no encontrados")
            
            treatment = Treatment(treatment_id, patient, doctor, description, date)
            self.treatments[treatment_id] = treatment
    
        elif action == "update":
            if treatment_id not in self.treatments:
                raise ValueError("El tratamiento ya existe")
            
            self.treatments[treatment_id].update_treatment(description)
            
        else:
            raise ValueError("Accion invalida")

        