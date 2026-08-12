# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient


def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John', 'Smith', 'Internal Med.'),Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('David','Smith', 15, '07123456789','C1 ABC')]
    discharged_patients = []
    family_group = {}
    
    
    while True:
        if admin.login():
            running = True 
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Register/view/update/delete patient')
        print(' 3- Discharge patients')
        print(' 4- View discharged patient')
        print(' 5- Assign doctor to a patient')
        print(' 6- Update admin detais')
        print(' 7- New Family Group')
        print(' 8- Generate Report')
        print(' 0- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            admin.doctor_management(doctors)
        elif op == '2':
            admin.patient_management(patients, discharged_patients)
        elif op == '3':
            # 2- View or discharge patients
            admin.view_patient(patients)
            #ToDo2
            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()
                if op == 'yes' or op == 'y':
                    #ToDo3
                    admin.discharge( patients, discharged_patients)
                    break
                elif op == 'no' or op == 'n':
                    break
                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        elif op == '4':
            # 3 - view discharged patients
            #ToDo4
            admin.view_discharge(discharged_patients)
        elif op == '5':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)
        elif op == '6':
            # 5- Update admin detais
            admin.update_details()

        elif op == '7':  # New Family Group
           admin.new_family_group(patients, family_group)
           
        elif op == '8':
            admin.generate_report(doctors, patients)

        elif op == '0':
            # 6 - Quit
            running = False
            break

        
        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

    # Save current system state.

if __name__ == '__main__':
    main()