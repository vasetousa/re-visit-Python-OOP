import datetime


class DVD:
    def __init__(self, name: str, dvd_id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.dvd_id = dvd_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @staticmethod
    def int2month(month):
        month_string = datetime.date(1900, month, 1).strftime('%B') # actual month making
        return month_string

    @classmethod
    def from_date(cls, dvd_id, name, date, age_restriction):  # date is in format 'day.mont.year all numbers,
        # makes the digit to a month
        day, month, year = date.split('.')
        month_from_date = DVD.int2month(int(month))
        return cls(name, dvd_id, year, month_from_date, age_restriction)

    @staticmethod
    def status_check(status):
        if status:
            return 'rented'
        return 'not rented'

    def __repr__(self):
        return (f'{self.dvd_id}: {self.name} ({self.creation_month} {self.creation_year})'
                f' has age restriction {self.age_restriction}. Status: {self.status_check(self.is_rented)}')
