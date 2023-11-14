import data


class Customer:
    CUSTOMER_ID = data._PERSONAL_ID

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        Customer.CUSTOMER_ID += 1

    @staticmethod
    def get_next_id():
        return Customer.CUSTOMER_ID + 1

    def __repr__(self):
        return f'Customer <{self.CUSTOMER_ID}> {self.name}; Address: {self.address}; Email: {self.email}'
