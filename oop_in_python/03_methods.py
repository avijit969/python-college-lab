class Instructor:
    # class object variable or default variable
    instaFollowers = 0

    def __init__(self, name, address):
        self.name = name
        self.address = address

    # method for display instructure details
    def display(self, subject):
        print(f"Hi i am {self.name} i teach {subject}")

    def update_follower(self):
        self.instaFollowers += 1


ins1 = Instructor("avijit", "balasore")
ins1.display("python")
ins1.update_follower()
print(ins1.instaFollowers)

ins2=Instructor("disha","rayagada")
ins2.update_follower()
ins2.update_follower()
print(ins2.instaFollowers)


