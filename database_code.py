

'''
PRESCRIPTION_STORE = {
    patient_id: {
        "patient_id": ,
        "email": '',
        "preferred_pharmacy": ''
        "mode_of_delivery": '',
        "location": '',
        "prescription": '', 
        "permission"
    }
}
'''
MODIFY_PERMISSION = 1
VIEW_PERMISSION = 0

PRESCRIPTION_STORE = {
    "doctor_id": {
        "patient_id": 0 ,
        "email": 0,
        "preferred_pharmacy": 0,
        "mode_of_delivery": 0,
        "location": 0,
        "prescription": 0, 
        "permission": 1
    },
    "pharmacy_id": {
        "patient_id": 0 ,
        "email": 0,
        "preferred_pharmacy": "epping",
        "mode_of_delivery": 0,
        "location": 0,
        "prescription": 0, 
        "permission": 0
    },
    "patient_id": {
        "patient_id": 0 ,
        "email": 0,
        "preferred_pharmacy": "epping",
        "mode_of_delivery": 0,
        "location": 0,
        "prescription": 0, 
        "permission": 0
    }
}

def get_patient_info(patient_id):
    '''Function which returns the details corresponding to the given patient ID'''
    return PRESCRIPTION_STORE[patient_id]

def get_email_by_id(patient_id):
    '''Function which returns the email corresponding to the given patient ID'''
    return PRESCRIPTION_STORE[patient_id]["email"]

def get_pharmacy_by_id(patient_id):
    '''Function which returns the permission corresponding to the given patient ID'''
    return PRESCRIPTION_STORE[patient_id]["preferred_pharmacy"]

def get_mode_by_id(patient_id):
    '''Function which returns the permission corresponding to the given patient ID'''
    return PRESCRIPTION_STORE[patient_id]["mode"]

def get_location_by_id(patient_id):
    '''Function which returns the permission corresponding to the given patient ID'''
    return PRESCRIPTION_STORE[patient_id]["location"]

def get_prescription_by_id(patient_id):
    '''Function which returns the permission corresponding to the given patient ID'''
    return PRESCRIPTION_STORE[patient_id]["prescription"]

def get_permission_by_id(patient_id):
    '''Function which returns the permission corresponding to the given patient ID'''
    return PRESCRIPTION_STORE[patient_id]["permission"]

def post_new_patient(patient_id, email, pharmacy, mode, location, prescription, permission):
    '''Function which creates and adds a new prescription'''
    new_patient = {
        "patient_id": patient_id,
        "email": email,
        "preferred_pharmacy": pharmacy,
        "mode_of_delivery": mode,
        "location": location,
        "prescription": prescription,
        "permission": VIEW_PERMISSION
    }
    PRESCRIPTION_STORE[patient_id] = new_patient

    return new_patient

def patch_prescription(patient_id, prescription):
    '''Function which changes the password of a user with the given user ID'''
    PRESCRIPTION_STORE[patient_id]["prescription"] = prescription

def reset_prescription_store():
    '''Function which resets the prescription store'''
    PRESCRIPTION_STORE.clear()

def cancel_prescription(patient_id):
    '''Function which cancels the prescription given the patient ID'''
    del PRESCRIPTION_STORE[patient_id]

if __name__ == "__main__":

    user_id = input("Login ID: ")
    permission_id = get_permission_by_id(user_id)

    if user_id == "doctor_id":
    # checks that only the doctor is able to modify the database
        if permission_id == VIEW_PERMISSION:
            raise AccessError(description="You do not have access to modify prescription")
        
        patient_id = input("Patient ID: ")
        prescription = input("Prescription: ")
        
        email = "email@gmail.com"
        pharmacy = "None"
        mode = "None"
        location = "None"
        permission = "0"

        patient = post_new_patient(patient_id, email, pharmacy, mode, location, prescription, permission)
        print(patient)

    elif user_id == "patient_id":
        patient_id = input("Patient ID: ")
        pharmacy = input("Preferred pharmacy: ")
        mode = input("Mode of delivery: ")
        location = input("Location of delivery or pickup: ")
        
        email = "email@gmail.com"
        pharmacy = "epping"
        mode = "delivery"
        location = "my house"
        prescription = "this is your prescription"
        permission = "0"

        patient = post_new_patient(patient_id, email, pharmacy, mode, location, prescription, permission)
        print(patient)

    elif user_id == "pharmacy_id":
        patient_id = "0"
        email = "email@gmail.com"
        pharmacy = "epping"
        mode = "delivery"
        location = "my house"
        prescription = "this is your prescription"
        permission = "0"

        patient = post_new_patient(patient_id, email, pharmacy, mode, location, prescription, permission)

        input("Patient ID: ")  
        pharmacy1 = get_pharmacy_by_id(user_id)   
        pharmacy2 = get_pharmacy_by_id(patient_id) 
        print("pharmacy_id_location is " + pharmacy1) 
        print("patient_id_location is " + pharmacy2) 
        print("Access granted") 
 
        # if the pharmacy is the pharmacy chosen by the patient, then the 
        # patient's details are revealed
        if pharmacy1 == pharmacy2:
            print(patient)
