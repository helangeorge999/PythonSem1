class Softwarica:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}") 


student_helan = Softwarica("HELAN", "17")
student_george = Softwarica("GEORGE", "18")           
student_adhikari = Softwarica("ADHIKAR", "19")

student_helan.display_info()
student_george.display_info()
student_adhikari.display_info()
