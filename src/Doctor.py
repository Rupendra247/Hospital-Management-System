class Doctor:
    """A class that deals with the Doctor operations"""
    fields = ['ID', 'first_name', 'surname', 'speciality', 'patients', 'appointments']

    def __init__(self, first_name, surname, speciality, ID=-1):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """
        self.ID = ID
        self.__first_name = first_name
        self.__surname = surname
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []

    def to_dict(self):
        return {
            'first_name': self.__first_name,
            'surname': self.__surname,
            'speciality': self.__speciality,
            'patients': self.__patients,
            'appointments': self.__appointments,
            'ID': self.ID
        }

    def next_ID(doctors, discharged_doctors):
        return max(
            [p.ID for p in doctors] + [p.ID for p in discharged_doctors]
        ) + 1
  
    def from_dict(data: dict):
        doc = Doctor(data['first_name'], data['surname'], data['speciality'], int(data['ID']))
        for patient in data['patients']:
            doc.add_patient(patient)
        for appointment in data['appointments']:
            doc.add_appointments(appointment)
        return doc

    def full_name(self) :
        #ToDo1
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

    def get_speciality(self) :
        #ToDo6
        return self.__speciality

    def set_speciality(self, new_speciality):
        #ToDo7
        self.__speciality = new_speciality
        return new_speciality

    def add_patient(self, patient):
        self.__patients.append(patient)

    def add_appointments(self, appointment):
        self.__appointments.append(appointment)

    def get_appointments(self):
        return self.__appointments

    def remove_patient(self, patient_id):
        try:
            self.__patients.remove(patient_id)
        except:
            pass

    def __str__(self) :
        return f'{self.full_name():^30}|{self.__speciality:^15}'
