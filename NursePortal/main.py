
class Patient():
    def __init__(self, patient_id, patient_bad):
        self.patient_id =patient_id
        self.patient_bad = patient_bad

class Contact:
    def __init__(self, contact_id, contact_phone, contact_mail, contact_free_start_time,
                 contact_free_end_time,patient):
        self.contact_id = contact_id
        self.contact_phone = contact_phone
        self.contact_mail = contact_mail
        self.contact_free_start_time = contact_free_start_time
        self.contact_free_end_time = contact_free_end_time
        self.patient = patient

class Event:
    def __init__(self,event_id,event_time,patient,**args):
        self.event_id = event_id
        self.event_time = event_time
        self.patient = patient
        self.conact = []

    def add_contact(self,**args):
        self.contact.append(**args)

p1 = Patient(1,2)
c1 = Contact(1,2,3,4,5,p1)
c2 = Contact(1,2,3,4,5,p1)
e1 = Event(1,12,p1)
e1.add_contact(c1,c2)

