class Con:
    def __init__(self, contact_id, contact_phone, contact_mail, contact_free_start_time,
                 contact_free_end_time):
        self.contact_id = contact_id
        self.contact_phone = contact_phone
        self.contact_mail = contact_mail
        self.contact_free_start_time = contact_free_start_time
        self.contact_free_end_time = contact_free_end_time

    # def get_patient_detials(self):
    #     print (vars(self.C))

# class Patient(Contact):
#     def __init__(self, patient_id, patient_bad):
#         super(Contact, self).__init__(self, patient_id, patient_bad)
#

class Patient():
    def __init__(self, patient_id, patient_bad):
        self.patient_id =patient_id
        self.patient_bad = patient_bad


#
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#     def perimeter(self):
#         return 2 * self.length + 2 * self.width
#
#
# class Square(Rectangle):
#     def __init__(self, length):
#         super(Square, self).__init__(length, length)
