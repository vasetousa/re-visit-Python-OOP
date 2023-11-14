from customer import Customer
import constants
from dvd import DVD


class MovieWorld:
    DVD_CAPACITY = constants.DVD_CAPACITY
    CUSTOMER_CAPACITY = constants.CUSTOMER_CAPACITY

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    def dvd_capacity(self):
        return f'DVD capacity: {__class__.DVD_CAPACITY}, currently in store: {len(self.dvds)}'

    def customer_capacity(self):
        return f'Customer capacity: {__class__.CUSTOMER_CAPACITY}, currently in store: {len(self.customers)}'

    def add_customer(self, customer: Customer):
        if len(self.customers) < constants.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < constants.DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = [cus for cus in self.customers if cus.id == customer_id][0]
        dvds = [dvd for dvd in self.dvds if dvd.dvd_id == dvd_id][0]

        if dvds in customer.rented_dvds:
            return f'{customer.name} has already rented {dvds.name}'

        if dvds.is_rented:
            return f"DVD is already rented"

        if customer.age < dvds.age_restriction:
            return f'{customer.name} should be at least {dvds.age_restriction} to rent this movie'

        dvds.is_rented = True
        customer.rented_dvds.append(dvds)
        return f'{customer.name} has successfully rented {dvds.name}'

    def return_dvd(self, customer_id, dvd_id):
        dvd = [dv for dv in self.dvds if dv.dvd_id == dvd_id][0]
        customer = [c for c in self.customers if c.id == customer_id][0]

        if customer and dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f'{customer.name} has successfully returned {dvd.name}'
        return f'{customer.name} does not have that DVD'

    def __repr__(self):
        customer_result = [c for c in self.customers]
        customer_dvds = [d for d in self.dvds]

        return f'{"\n".join(map(str, customer_result))}\n{"\n".join(map(str, customer_dvds))}'
