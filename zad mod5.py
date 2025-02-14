from faker import Faker
import random
fake = Faker()

class BaseContact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}")
    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name)

class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, phone, email, position, company, work_phone):
        super().__init__(first_name, last_name, phone, email)
        self.position = position
        self.company = company
        self.work_phone = work_phone
    def contact(self):
        print(f"Wybieram numer {self.work_phone} i dzwonię do {self.first_name} {self.last_name} z firmy {self.company}")
    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name) + len(self.company)

def create_contacts(type, amount):
    contacts = []
    for i in range(amount):
        if type == "BaseContact":
            contacts.append(BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), phone=fake.phone_number(), email=fake.email()))
        elif type == "BusinessContact":
            contacts.append(BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), phone=fake.phone_number(), email=fake.email(), position=fake.job(), company=fake.company(), work_phone=fake.phone_number()))
        else:
            print("Błędny typ kontaktu")
            break
    return contacts
base_contacts = create_contacts("BaseContact", 5)
business_contacts = create_contacts("BusinessContact", 5)

for contact in base_contacts:
    contact.contact()
    print(contact.label_length)

for contact in business_contacts:
    contact.contact()
    print(contact.label_length)
