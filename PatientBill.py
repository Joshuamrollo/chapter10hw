from PatientClass import Patient
from ProcedureClass import Procedure


def main():
    #create patient and procedure instances
    patient = Patient(1, 'Matt Jones', '123 Main st, Waco TX 76706', '254-555-7415', True)
    procedures = []
    procedures.append(Procedure('Physical Exam', '2/15/2022', 'Dr. Irvine', 250, 1))
    procedures.append(Procedure('MRI', '2/15/2022', 'Dr. Hamilton', 1500, 1))
    procedures.append(Procedure('CT Scan', '2/17/2022', 'Dr. Drey', 1200, 2))

    #print information xd
    print('*** Patient Bill ***')
    patient.get_name()
    patient.get_address()   
    patient.get_phone()
    print('\n')

    total = 0
    for p in procedures:
        if p.id != patient.ID:
            continue
        p.get_procedure()
        p.get_date()
        p.get_name()
        p.get_charges()
        print('\n')
        total += int(p.charges)
    print('Total Charges: ' + "${:,.2f}".format(total))


main()
#got an interview with Amazon thursday wish me luck 0_0
#got an interview with Amazon thursday wish me luck 0_0
#got an interview with Amazon thursday wish me luck 0_0
#got an interview with Amazon thursday wish me luck 0_0
#got an interview with Amazon thursday wish me luck 0_0
#got an interview with Amazon thursday wish me luck 0_0
#got an interview with Amazon thursday wish me luck 0_0
#got an interview with Amazon thursday wish me luck 0_0
#got an interview with Amazon thursday wish me luck 0_0
#got an interview with Amazon thursday wish me luck 0_0
#got an interview with Amazon thursday wish me luck 0_0