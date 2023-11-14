import re
import typing



class EmailValidator:
    def __init__(self, min_length: int, mails: list[str], domains: list[str]):
        self.__min_length = min_length
        self.__mails = set(mails)
        self.__domains = set(domains)

    def validate(self, email):
        (name, mail, domain) = re.split(r'[@.]', email)
        return (self.__validate_name(name)
                and self.__validate_mail(mail)
                and self.__validate_domain(domain))

    def __validate_name(self, name):
        return name and self.__min_length <= len(name)

    def __validate_mail(self, mail):
        return mail in self.__mails

    def __validate_domain(self, domain):
        return domain in self.__domains






mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains) # data for the validator to compare
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
print(email_validator.validate("abv2333@softuni.bg"))
