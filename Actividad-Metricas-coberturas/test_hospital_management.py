import pytest
from appointment import Appointment
from hospital_management import HospitalManagement
from patient import Patient
from doctor import Doctor
from treatment import Treatment

@pytest.fixture()
def hospital_management_P():
    hospital_management = HospitalManagement()
    hospital_management.manage_patients("create", "P001", "Juan Silva", "16-02-2000")
    yield hospital_management  
    hospital_management.manage_patients("delete", "P001")

@pytest.fixture()
def hospital_management_D():
    hospital_management = HospitalManagement()
    hospital_management.manage_doctors("create", "D001", "Diego Quispe", "Cardiologia", ["10-11-2024, 11:00"])
    yield hospital_management  
    hospital_management.manage_doctors("delete", "D001")

@pytest.fixture()
def hospital_management_C():
    hospital_management = HospitalManagement()
    hospital_management.manage_patients("create", "P001", "Juan Silva", "16-02-2000")
    hospital_management.manage_doctors("create", "D001", "Diego Quispe", "Cardiologia", ["10-11-2024, 11:00"])
    yield hospital_management  

@pytest.fixture()
def hospital_management_T():
    hospital_management = HospitalManagement()
    hospital_management.manage_patients("create", "P001", "Juan Silva", "16-02-2000")
    hospital_management.manage_doctors("create", "D001", "Diego Quispe", "Cardiologia", ["10-11-2024, 11:00"])
    yield hospital_management  

def test_manage_patients_create(hospital_management_P):
    assert "P001" in hospital_management_P.patients

def test_manage_patients_update(hospital_management_P):
    hospital_management_P.manage_patients("update", "P001", "Juan Silva Rojas", "16-02-2000")
    assert hospital_management_P.patients["P001"].name == "Juan Silva Rojas"

def test_manage_patients_delete(hospital_management_P):
    hospital_management_P.manage_patients("create", "P002", "Diego Quispe", "16-05-2001")
    hospital_management_P.manage_patients("delete", "P002")
    assert "P002" not in hospital_management_P.patients

def test_manage_doctors_create(hospital_management_D):
    assert "D001" in hospital_management_D.doctors
    
def test_manage_doctors_add_slot(hospital_management_D):
    hospital_management_D.manage_doctors("add_slot", "D001", "Diego Quispe", "Cardiologia", "05-12-2024, 10:00")
    assert "05-12-2024, 10:00" in hospital_management_D.doctors["D001"].available_slots

def test_manage_doctors_remove_slot(hospital_management_D):
    hospital_management_D.manage_doctors("remove_slot","D001","Diego Quispe","Cardiologia", "10-11-2024, 11:00")
    assert  "10-11-2024, 11:00" not in hospital_management_D.doctors["D001"].available_slots

def test_manage_appointments_schedule(hospital_management_C):
    hospital_management_C.manage_appointments("schedule","C001","P001","D001","10-11-2024, 11:00")
    assert "C001" in hospital_management_C.appointments

def test_manage_appointments_cancel(hospital_management_C):
    hospital_management_C.manage_appointments("schedule","C001","P001","D001","10-11-2024, 11:00")
    hospital_management_C.manage_appointments("cancel","C001","P001","D001","10-11-2024, 11:00")
    assert hospital_management_C.appointments["C001"].status == "cancelled"

def test_manage_treatment_record(hospital_management_T):
    hospital_management_T.manage_treatments("record","T001","P001","D001","Tiene Gripe","11-12-2024")
    assert "T001" in hospital_management_T.treatments

def test_manage_treatment_update(hospital_management_T):
    hospital_management_T.manage_treatments("record","T001","P001","D001","Tiene Gripe","11-03-2025")
    hospital_management_T.manage_treatments("update","T001","P001","D001","Se curó la Gripe","11-03-2025")
    assert hospital_management_T.treatments["T001"].description == "Se curó la Gripe"

def test_invalid_patient_name():
    with pytest.raises(ValueError):
        Patient("P002", "?", "16-02-2000") 

def test_invalid_patient_dob():
    with pytest.raises(ValueError):
        Patient("P003", "Ravichagua", "16/032006") 

def test_invalid_doctor_name():
    with pytest.raises(ValueError):
        Doctor("D001", "###", "Cardiologia", ["10-11-2024, 11:00"])

def test_invalid_doctor_specialitation():
    with pytest.raises(ValueError):
        Doctor("D001", "Tommy Vercetty", "???", ["10-11-2024, 11:00"])

def test_invalid_doctor_slot():
    with pytest.raises(ValueError):
        Doctor("D001", "Bruce Banner", "Oncología", ["10-11-2o2o, 11:00am"])

def test_invalid_appointment_datetime():
    with pytest.raises(ValueError):
        Appointment("C001", "P001","D001", "10-11-2o24, 12:oo","scheduled")    

def test_empty_treatment_description():
    with pytest.raises(ValueError):
        Treatment("T001", "P001","D001","","10-11-2024")        

def test_invalid_treatment_date():
    with pytest.raises(ValueError):
        Treatment("T001", "P001","D001","Tiene sida","10-*|-2o24")      