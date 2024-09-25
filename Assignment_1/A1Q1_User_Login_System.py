class LoginSystem:
    def __init__(self, usernames, user_passwords):
        self.usernames = ["bob123", "realuser123"]
        self.user_passwords = ["123qwe!@#QWE", "321ewq#@!EWQ"]
        self.login_attempts = [0,0]
        self.user_status = ["unlocked", "unlocked"]

    def usernamePrompt(self):
        # print("\n-------------- LOGIN: --------------")
        username_input = input("Enter your Username: ")
        return username_input

    def passwordPrompt(self, userindex):
        while True:
            password_input = input("Enter your password: ")
            if self.user_passwords[userindex] == password_input:
                # print("\nLogged in Successfully")
                # displayDashboard()
                # break
                return True
            else:
                if not self.checkUserStatus(userindex):
                    return False  # Account locked
                # print("Incorrect password. Try again.")  # Inform the user
                #else:
                    #checkUserExists(usernamePrompt())

#    def reEnter():
#        re_enter = input("Back to Login? (y/n): ").lower()
#        if re_enter == "y":
#            checkUserExists(usernamePrompt())
#        else:
#            exit()

    def checkUserStatus(self, userindex):
        self.login_attempts[userindex] = self.login_attempts[userindex] + 1
        attempts_left = 3 - self.login_attempts[userindex]
        if attempts_left >= 1:
            # print("\nLogin unsuccessful you have", attempts_left, "attempts left")
            return True
        else:
            self.user_status[userindex] = "locked"
            return False  # Account locked
            # print("\nYour account has been locked since you failed to enter the correct password thrice")
            # reEnter()

#    def displayDashboard():
#        print("-------------------------------\n"
#              "|                             |\n"
#              "|    THIS IS THE DASHBOARD    |\n"
#              "|                             |\n"
#              "-------------------------------\n")

    def checkUserExists(self, username):
        if username in self.usernames:
            # print("\nUser exists")
            user_index = self.usernames.index(username)
            if self.user_status[user_index] == "locked":
                # print("\nYour account has been locked, re-run the program to revert")
                # reEnter()
                return "locked"
            else:
                return self.passwordPrompt(user_index)
        else:
            # print("\nUser does not exist, try again")
            # reEnter()
            return None  # User does not exist




