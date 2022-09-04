import time


class Door:
    def __init__(self):
        self.access_code = self.set_up_code()
        self.confirm_code()
        self.count = 0

    def set_up_code(self):
        """This function returns the code set by the user"""
        access_code = int(input("SET UP CODE: "))
        if access_code:
            return access_code
        else:
            print("NO INPUT RECEIVED")
            self.set_up_code()

    def confirm_code(self):
        """This function returns the confirmation of the entered code."""
        confirm_lock_code = int(input("RECONFIRM CODE:  "))
        if confirm_lock_code == self.access_code:
            print("MATCH")
            return confirm_lock_code
        else:
            print("NO MATCH")
            self.confirm_code()

    def access_door(self):
        """Returns the code the user enters to check against the registered code."""
        code = int(input("ENTER CODE:  "))
        if code == self.access_code:
            print("✔")
            return True
        else:
            print("❌")
            self.count += 1
            if self.count % 4 == 0 and self.count == 12:
                print("SERVICE NEEDED")
                return
            elif self.count % 4 == 0:
                time.sleep(10)
            self.access_door()
