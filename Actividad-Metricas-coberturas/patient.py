import re

class Patient:
    def __init__(self, patient_id, name, dob):
        self.patient_id = patient_id
        self.name = self.validate_name(name)
        self.dob = self.validate_dob(dob)
        self.medical_history = []
        
    def validate_name(self, name):
        # Aaaa Bbbbb
        if not re.match(r'^[A-Za-z\s]+$', name):
            raise ValueError("Nombre no valido")
        return name
    
    def validate_dob(self, dob):
        # dd - mm - yyyy
        if not re.match(r'^\d{2}-\d{2}-\d{4}$', dob):
            raise ValueError("Fecha no valida")
        return dob
    
    def update_info(self, name, dob):
        self.name = self.validate_name(name)
        self.dob = self.validate_dob(dob)
        
    def add_medical_history(self, entry):
        self.medical_history.append(entry)
        
    def summary(self):
        return {
            "ID_PATIENT: " : self.patient_id,
            "NAME: " : self.name,
            "DATE: " : self.dob,
            "MEDICAL HISTORY: " : self.medical_history
        }