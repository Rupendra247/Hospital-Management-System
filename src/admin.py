from Doctor import Doctor
from Patient import Patient


class Admin:
    """A class that deals with the Admin operations"""
    fields = ['username', 'password', 'address']

    def __init__(self, username, password, address=''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address


    def to_dict(self):
        return {
            'username': self.__username,
            'password': self.__password,
            'address': self.__address,
        }

    @staticmethod
    def from_dict(data: dict):
        return Admin(data['username'], data['password'], data['address'])

    def view(self, a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        
        return self.__username == username and self.__password == password

    def find_index(self,index, doctors):
        
        # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        first_name = input("Enter your first name: ")
        surname = input("Enter your surname: ")
        speciality = input("Please enter your speciality: ")
        return first_name, surname, speciality
    
    def get_patient_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        first_name = input("Enter your first name: ")
        surname = input("Enter your surname: ")
        age = int(input("Please enter your age: "))
        mobile = input("Please enter your number: ")
        postcode = input(str("Please enter your postcode: "))
        symptoms = input("Please enter your your symptoms: ")
        return first_name, surname, age, mobile, postcode, symptoms
    
    def doctor_management(self, doctors, discharged_doctors=[]):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")
        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        op = input("Choose: ")

        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            
            first_name, surname, speciality = self.get_doctor_details()
            # check if the name is already registered
            name_exists = False
            for idx, doctor in enumerate(doctors):
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists: update doctor details.')
                    name_exists = True
                    
                    break # save time and end the loop
            ID = Patient.next_ID(doctors, discharged_doctors)
            new_doctor = Doctor(first_name, surname, speciality, ID=ID)
            if name_exists:
                doctors[idx] = new_doctor
            else:
                
                # add the doctor to the list of doctors
                doctors.append(new_doctor) 
            print('Doctor registered.')
        # View
        elif op == '2':
            for doctor in doctors:
                print(doctor)
            
        # Update doctor details
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index, doctors)
                    if doctor_index != False:
                        a_doctor: Doctor = doctors[index]
                        break
                    else:
                        print("Doctor not found")
                        # doctor_index is the ID mines one (-1)
                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            print(' 4 Return to main menu')
            op = input('Input: ') # make the user input lowercase

            while True:
                if op == '1':
                    first_name = input("Enter doctor's First name:")
                    a_doctor.set_first_name(first_name)
                    doctors[index] = a_doctor
                    break
                elif op == '2':
                    surname = input("Enter doctor's Surname:")
                    a_doctor.set_surname(surname)
                    doctors[index] = a_doctor
                    break
                elif op == '3':
                    speciality = input("Enter doctor's Speciality:")
                    a_doctor.set_speciality(speciality)
                    doctors[index] = a_doctor
                    break
                elif op == '4':
                    break
        # Delete
        elif op == '4':
            while True:
                print("-----Delete Doctor-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index = self.find_index(index, doctors)
                    if doctor_index != False:
                        # remove the doctor from the list ...
                        a_doctor: Doctor = doctors[index]
                        discharged_doctors.append(a_doctor)
                        doctors.pop(index)
                        break
                    else:
                        print("Doctor not found")
                        # doctor_index is the ID mines one (-1)
                        if index == -1:
                            break
                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')

    def patient_management(self, patients, discharged_patients):
        print("-----Patient Management-----")
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        op = input("Choose: ")

        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the patients\'s details:')
            
            first_name, surname, age, mobile, postcode, symptoms = self.get_patient_details()
            # check if the name is already registered
            name_exists = False
            for idx, patient in enumerate(patients):
                if first_name == patient.get_first_name() and surname == patient.get_surname():
                    print('Name already exists: updating details.')
                    name_exists = True
                    
                    break # save time and end the loop
            ID = Patient.next_ID(patients, discharged_patients)
            new_patient: Patient = Patient(first_name, surname, age, mobile, postcode, ID=ID)
            new_patient.add_symptom(symptoms)
            if name_exists:
                patients[idx] = new_patient
            else:
                patients.append(new_patient) # to the list of patients
            
            #add the doctor
            print('patient registered.')
        # View
        elif op == '2':
            self.view_patient(patients)
            
        # Update
        elif op == '3':
            while True:
                self.view_patient(patients)
                try:
                    index = int(input('Enter the ID of the patients: ')) - 1
                    patient_index = self.find_index(index, patients)
                    if patient_index!=False:
                        a_patient: Patient = patients[index]
                        break
                    else:
                        print("Patient not found")
                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Age')
            print(' 4 Mobile number')
            print(' 5 Postcode')
            print(' 6 Add symptoms')
            print(' 7 Return to main menu')

            op = input('Input: ') # make the user input lowercase
            
            #ToDo8
            if op == '1':
                first_name = input("Enter your first name: ")
                a_patient.set_first_name(first_name)
                patients[index] = a_patient
            elif op == '2':
                surname = input("Enter your surname: ")
                a_patient.set_surname(surname)
                patients[index] = a_patient
            elif op == '3':
                age = int(input("Please enter your age: "))
                a_patient.set_age(age)
                patients[index] = a_patient
            elif op == '4':
                mobile = input("Please enter your number: ")
                a_patient.set_mobile(mobile)
                patients[index] = a_patient
            elif op == '5':
                postcode = input(str("Please enter your postcode: "))
                a_patient.set_postcode(postcode)
                patients[index] = a_patient
            elif op == '6':
                symptoms = input("Please enter your your symptoms: ")
                a_patient.add_symptom(symptoms)
                patients[index] = a_patient
            pass
        # Delete
        elif op == '4':
            while True:
                print("-----Delete patients-----")
                self.view_patient(patients)
                try:
                    index = int(input('Enter the ID of the patient: ')) - 1
                    patient_index = self.find_index(index, patients)
                    if patient_index != False:
                        # remove the doctor from the list ...
                        a_patient: Patient = patients[index]
                        discharged_patients.append(a_patient)
                        patients.pop(index)
                        break
                    else:
                        print("Patient not found")
                        # doctor_index is the ID mines one (-1)
                        if index == -1:
                            break
                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')
        else:
            print('Invalid operation choosen. Check your spelling!')

    def view_patient(self, patients: list):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----  View Patients  -----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo10
        self.view(patients)

    def assign_doctor_to_patient(self, patients: list, doctors: list):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures
            a_patient: Patient = patients[patient_index]
        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index ,doctors)!=False:
                # link the patients to the doctor and vice versa
                #ToDo11
                a_doctor: Doctor = doctors[doctor_index]
                a_patient.set_doctor_id(a_doctor.ID)
                a_patient.link(a_doctor.full_name())
                a_doctor.add_patient(a_patient.ID)
                patients[patient_index] = a_patient
                doctors[doctor_index] = a_doctor
                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharged_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        # print("-----Discharge Patient-----")
        # print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        # self.view(patients)
        while True:
            try:
                patient_index = int(input("Who do you want to discharge ?"))
                break
            except ValueError as e:
                print('Invalid Patient Index.')

        p = patient_index - 1
        if p not in range(1, len(patients)+1):
            print('Invalid Patient Index.'); return
        print("you have removecd the items ", patients[p].full_name())
        discharged_patients.append(patients[p])
        patients.pop(p)

    def generate_report(self, doctors, patients):
        # The total number of doctors in the system
        print('+----------  System Report ---------+')
        print(f'The system has {len(doctors)} doctors.')
        for doctor in doctors:
            patients_filterd = [p for p in patients if p.doctor_id == doctor.ID]
            print(f'The doctor {doctor.full_name()} has {len(patients_filterd)} pantients.')
        for doctor in doctors:
            print(f'The doctor {doctor.full_name()} has {len(doctor.get_appointments())} appointments.')

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(discharged_patients)

    def new_family_group(self, patients: list, family_group: dict):
        print("-----New Family Group-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)
        patient_idxs = []
        while True:
            try:
                patient_index = int(input("Who do you want to add (0 to save)?")) -1
                if patient_index == -1:
                    break
                elif patient_index in range(len(patients)):
                    patient_idxs.append(patient_index)
            except ValueError as e:
                print('Invalid Patient Index.')
        if len(patient_idxs):
            family_group[max([0]+list(family_group.keys()))+1] = patient_idxs

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        print(' 4 Quit')

        while True:
            op = input('Input: ')
            if op == '1':
                #ToDo14
                username = input("Enter the new username ")
                self.__username = username
                break
            elif op == '2':
                password = input('Enter the new password: ')
                # validate the password
                while password == self.__password:
                    password = input('Enter the new password again: ')
                self.__password = password
                break
            elif op == '3':
                #ToDo15
                address = input("Enter the new address ")
                self.__address = address
                break
            elif op == '4':
                break
            else:
                pass