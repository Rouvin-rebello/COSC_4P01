class LoginSystem:
    def __init__(self, usernames, user_passwords):
        self.usernames = usernames
        self.user_passwords = user_passwords
        self.login_attempts = [0] * len(usernames) # To track login attempts
        self.user_status = ["unlocked"] * len(usernames) # Track user status

# This method prompts the user to enter their username.
    def username_prompt(self):
        username_input = input("Enter your Username: ")
        return username_input

# This method prompts the used to enter their password and then validates it
    def password_prompt(self, userindex):
        while True:
            password_input = input("Enter your password: ")
            if self.user_passwords[userindex] == password_input:
                return True
            else:
                if not self.check_user_status(userindex):
                    return False  # Account locked

# This function checks if the user's account is locked or not
    def check_user_status(self, userindex):
        self.login_attempts[userindex] += 1
        attempts_left = 3 - self.login_attempts[userindex]
        if attempts_left > 0:
            return True
        else:
            self.user_status[userindex] = "locked"
            return False  # Account locked

# This method checks if the username exists and allows to login
    def check_user_exists(self, username):
        if username in self.usernames:
            user_index = self.usernames.index(username)
            if self.user_status[user_index] == "locked":
                return "locked"
            else:
                return self.password_prompt(user_index)
        else:
            return None  # User does not exist




