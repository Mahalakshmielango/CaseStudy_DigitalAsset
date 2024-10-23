class Employee:
    def __init__(self, employee_id, name, department, email, password):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.email = email
        self.password = password

    # Getters and setters
    def get_employee_id(self):
        return self.employee_id

    def set_employee_id(self, employee_id):
        self.employee_id = employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_department(self):
        return self.department

    def set_department(self, department):
        self.department = department

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password


class Asset:
    def __init__(self, asset_id, name, asset_type, serial_number, purchase_date, location, status, owner_id):
        self.asset_id = asset_id
        self.name = name
        self.type = asset_type
        self.serial_number = serial_number
        self.purchase_date = purchase_date
        self.location = location
        self.status = status
        self.owner_id = owner_id

    # Getters and setters
    def get_asset_id(self):
        return self.asset_id

    def set_asset_id(self, asset_id):
        self.asset_id = asset_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_type(self):
        return self.type

    def set_type(self, asset_type):
        self.type = asset_type

    def get_serial_number(self):
        return self.serial_number

    def set_serial_number(self, serial_number):
        self.serial_number = serial_number

    def get_purchase_date(self):
        return self.purchase_date

    def set_purchase_date(self, purchase_date):
        self.purchase_date = purchase_date

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_owner_id(self):
        return self.owner_id

    def set_owner_id(self, owner_id):
        self.owner_id = owner_id
