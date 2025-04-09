class chatbook:
    def __init__(self):
        self.username= ""
        self.password= ''
        self.loggedin =False
        self.menu()


    def menu(self):
        user_input = input(""" welcome to the chatbook !! how would you like to proceed?"
                            1. press 1 to signup
                            2. press 2 to login
                            3. press 3 write to post
                            4. press 4 to message your furned 
                            5. press any key to exit""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.login()
        elif user_input == "3":
            self.post()
        elif user_input == "4":
            self.message()
        else:
            exit()

    def signup(self):
        email = input("enter your email->")
        password = input("enter your password->")
        self.username = email
        self.password = password
        print("you have signuped successfully")
        print("\n")
        self.menu()
    def login(self):
        if self.username == '' and self.password== '' :
            print("you are not logged in")
        else:
            user = input("pleae neter your email/username")
            password = input("please enter your password")
            if user == self.username and password == self.password:
                print("you have logged in successfully")
                self.loggedin = True
            else:
                print("you have entered wrong username or password")
                print("\n")
            self.menu()
    def post(self):
        if self.loggedin == True:
            post = input("enter your post->")
            print(f"your post has been posted successfully {post}")
        else:
            print("you are not logged in")
            print("\n")
            self.menu()

    def message(self):
        if self.loggedin == True:
            msg = input("enter your msg here")
            friend = input("whom to send this msg")
        else:
            print("you are not logged in")
            print("cdc")
            print("\n")
            self.menu()






obj = chatbook()