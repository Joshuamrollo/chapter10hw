class Procedure:
    def __init__(self, p, d, n, c, id):
        self.procedure = p
        self.date = d
        self.name = n
        self.charges = str(c)
        self.id = str(id)
        # print('procedure name: ' + self.procedure)
        # print('date: ' + self.date)
        # print('practitioner name: ' + self.name)
        # print('cost: ' + self.charges)
        # print('patient id: ' + self.id)

    def get_id(self):
        print('patient id: ' + self.id)
    
    def get_procedure(self):
        print('procedure name: ' + self.procedure)
    
    def get_name(self):
        print('practitioner name: ' + self.name)

    def get_date(self):
        print('date: ' + self.date)

    def get_charges(self):
        print('cost: ' + "${:,.2f}".format(int(self.charges)))