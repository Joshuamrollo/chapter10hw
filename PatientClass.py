class Patient:
    def __init__(self, ID, name, address, phone, veteran_status):
        self.ID = str(ID)
        self.name = name
        self.address = address
        self.phone = phone
        self.veteran_status = veteran_status
        # print('patient id: ' + self.ID)
        # print('patient name: ' + self.name)
        # print('address: ' + self.address)
        # print('patient phone: ' + self.phone)
        # print('veteran: ' + ('Yes' if self.veteran_status else 'No'))
    
    def get_ID(self):
        print(self.ID)
    
    def get_name(self):
        print(self.name)
    
    def get_address(self):
        print(self.address)
    
    def get_phone(self):
        print(self.phone)
    
    def get_veteran_status(self):
        print(self.veteran_status)