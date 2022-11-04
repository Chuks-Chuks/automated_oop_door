import time


class Door:
    def __init__(self):
        self.times_opened = 0
        self.count = 0
        self.check_set_up()

    def check_set_up(self):
        """Checks if the user has already set up a password"""
        with open("times_opened.txt", "r") as file:
            if file.read() == "":
                self.set_up_code()
                self.confirm_code()
                self.access_door()
            else:
                self.access_door()

    def set_up_code(self):
        """This function returns the code set by the user"""
        self.times_opened += 1
        with open("times_opened.txt", "w") as verify_already_set_up_account:
            verify_already_set_up_account.write(f"{self.times_opened}")
        access_code = input("SET UP CODE:")
        if access_code:
            with open("password.txt", "w") as password_created:
                password_created.write(f"{access_code}")
            return access_code
        else:
            print("NO INPUT RECEIVED")
            self.set_up_code()

    def confirm_code(self):
        """This function returns the confirmation of the entered code."""
        confirm_lock_code = input("RECONFIRM CODE:")
        with open("password.txt", "r") as password_read:
            the_password = password_read.read()
        if confirm_lock_code == the_password:
            print("MATCH")
            return confirm_lock_code
        else:
            print("NO MATCH")
            print(type(password_read))
            self.confirm_code()

    def access_door(self):
        """Returns the code the user enters to check against the registered code."""
        code = input("ENTER CODE:  ")
        with open("password.txt", "r") as password_read:
            the_password = password_read.read()
        if code == the_password:
            print("✔")
            return True
        else:
            print("❌")
            self.count += 1
            if self.count == 4:
                time.sleep(10)
            self.access_door()
