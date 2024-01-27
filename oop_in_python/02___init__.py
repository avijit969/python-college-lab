#python constructer

class Instructor:
    def __init__(self,Instructor_name,Instructor_address):
        self.name=Instructor_name
        self.address=Instructor_address

instructor1=Instructor("avijit","balasore")

print(instructor1.name +" " + instructor1.address)
print(f"{instructor1.name} address is {instructor1.address}")
        