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

#what is the need of data should initate as sson as object is called? why we are not making fucntion and calling when we required?
# so the answer is that in real world when application loaded , some data should be appear without doing anything
# like when we open the face , user doen't connect with inter to fb or to database, as soon as app opne class is called and these thing connect automatically.