from faker import Faker
import random
fake = Faker()

class BaseContact:
    def __init__(self, frist_name, last_name, phone, email):
        self.frist_name = frist_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.frist_name} {self.last_name}")
    @property
    def label_length(self):
        return len(self.frist_name) + len(self.last_name)
class BusinessContact(BaseContact):
    def __init__(self, frist_name, last_name, phone, email, position, company, work_phone):
        super().__init__(frist_name, last_name, phone, email)
        self.position = position
        self.company = company
        self.work_phone = work_phone
    def contact(self):
        print(f"Wybieram numer {self.work_phone} i dzwonię do {self.frist_name} {self.last_name} z firmy {self.company}")
    @property
    def label_length(self):
        return len(self.frist_name) + len(self.last_name) + len(self.company)
def create_contacts(type, amount):
    contacts = []
    for i in range(amount):
        if type == "BaseContact":
            contacts.append(BaseContact(frist_name=fake.first_name(), last_name=fake.last_name(), phone=fake.phone_number(), email=fake.email()))
        elif type == "BusinessContact":
            contacts.append(BusinessContact(frist_name=fake.first_name(), last_name=fake.last_name(), phone=fake.phone_number(), email=fake.email(), position=fake.job(), company=fake.company(), work_phone=fake.phone_number()))
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
