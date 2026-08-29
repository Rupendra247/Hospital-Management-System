class Patient:
    """Patient class"""
    fields = ['first_name', 'surname', 'age', 'mobile', 'postcode', 'symptoms', 'ID', 'doctor', 'doctor_id']
    def __init__(self, first_name, surname, age, mobile, postcode, ID=-1):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """
        self.ID = ID
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile 
        self.__postcode = postcode
        self.__symptoms = []

        #ToDo1
        self.__doctor: str = None
        self.doctor_id = -1

    def set_doctor_id(self, doctor_id):
        self.doctor_id = doctor_id

    def next_ID(patients, discharged_patients):
        return max(
            [p.ID for p in patients] + [p.ID for p in discharged_patients]
        ) + 1

    def to_dict(self):
        return {
            'first_name': self.__first_name,
            'surname': self.__surname,
            'age': self.__age,
            'mobile': self.__mobile,
            'postcode': self.__postcode,
            'symptoms': self.__symptoms,
            'ID': self.ID,
            'doctor': self.__doctor,
            'doctor_id': self.doctor_id
        }

    def from_dict(data: dict):
        patient = Patient(data['first_name'], data['surname'], data['age'],
                           data['mobile'], data['postcode'], int(data['ID']))
        for symptom in data['symptoms']:
            patient.add_symptom(symptom)
        patient.set_doctor_id(data['doctor_id'])
        patient.link(data['doctor'])

        return patient

    def full_name(self) :
        """full name is first_name and surname"""
        #ToDo2
        return self.__surname + ', ' + self.__first_name
    
    def get_first_name(self) :
        #ToDo2
        return self.__first_name

    def set_first_name(self, new_first_name):
        #ToDo3
        self.__first_name = new_first_name
        return new_first_name

    def get_surname(self) :
        #ToDo4
        return self.__surname

    def set_surname(self, new_surname):
        #ToDo5
        self.__surname = new_surname
        return new_surname

    def set_age(self, age):
        self.__age = age

    def age(self):
        return self.__age
    
    def mobile(self):
        return self.__mobile

    def set_mobile(self, mobile):
        self.__mobile = mobile

    def postcode(self):
        return self.__postcode

    def set_postcode(self, postcode):
        self.__postcode = postcode

    def get_doctor(self) :
        #ToDo3
        return self.__doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
        #ToDo4
        if len(self.__symptoms):
            print(self.__symptoms)
        else:
            print('No symptoms !?')

    def add_symptom(self, symptom):
        self.__symptoms.append(symptom)

    def __str__(self):
        doc = self.__doctor if self.__doctor is not None else " - "
        return f'{self.full_name():^30}|{doc:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'

    
def __str__(self):
        if self.__doctor is not None:
            doctor_name = self.__doctor.get_full_name()
        else:
            doctor_name = "Not Assigned"
        return f'{self.full_name():^30}|{doctor_name:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
    