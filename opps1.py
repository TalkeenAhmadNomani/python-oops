#initiating the class

class employe:
    #special method/magic-constructor
    def __init__(self):
        self.id = 123
        self.salary = 4500
        self.designation= "SDE"

    #function inside the class is knowna as methods

    def travel(self, destination):
        print(f"Employee {self.id} is traveling to {destination}")


# creating an object/instance for that class

talkeen = employe()

#printing the attribute or dataa

print(talkeen.id)

#calling the method

talkeen.travel("patna")