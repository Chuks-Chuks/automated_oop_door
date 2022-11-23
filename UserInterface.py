from tkinter import *
from door_parts import Door
from tkinter import messagebox


class UserInterface:
    def __init__(self, door: Door):
        # create the window from Tkinter
        self.door = door
        self.window = Tk()
        self.window.title("Safe Lock")
        self.window.config(pady=25, padx=25)
        self.canvas = Canvas(width=200, height=189, bg="white")
        self.image = PhotoImage(file="images/lock_pic.png")
        self.check_mark_image = PhotoImage(file="images/checkmark-xxl.png")
        # self.false_image = PhotoImage(file="images/x_check_mark.png")
        self.lock_image = self.canvas.create_image(100, 95, image=self.image)
        self.canvas.grid(row=0, column=1)
        self.pin_label = Label(text="Pin:")
        self.confirm_label = Label(text="Confirm:")
        self.pin_entry = Entry(width=15)
        self.confirm_entry = Entry(width=15)
        self.enter = Button(text="Enter", width=10, command=self.confirm_password)
        if self.door.check_set_up():
            self.no_set_up()
        else:
            self.code_already_setup()
        self.window.mainloop()

    def check_for_empty_fields(self):
        print(self.pin_entry.get())
        if self.pin_entry.get() == "":
            messagebox.showerror(title="Complete empty fields", message="There was no entry for your pin.")
            return False
        elif self.confirm_entry.get() == "":
            messagebox.showerror(title="Confirmation error", message="Confirmation field empty")
            return False
        else:
            return True

    def confirm_password(self):
        if self.door.check_set_up():
            if self.check_for_empty_fields():
                pin = self.door.set_up_code(self.pin_entry.get())
                print(f"This is the pin: {pin}")
                if self.door.confirm_code(self.confirm_entry.get()):
                    self.confirm_entry.grid_remove()
                    self.confirm_label.grid_remove()
                    self.pin_entry.delete(0, END)
                    messagebox.showinfo(title="Success", message="Setup success.")
                else:
                    self.pin_entry.delete(0, END)
                    self.confirm_entry.delete(0, END)
                    messagebox.showerror(title="Error", message="No match")
        else:
            if self.code_already_setup():
                messagebox.showinfo(title="Match", message="Code correct.")
            else:
                messagebox.showerror(title="Error", message="Incorrect details.")
            self.pin_entry.delete(0, END)

    def code_already_setup(self):
        # First of all, we change the UI interface
        self.set_up_ui()
        return self.door.access_door(self.pin_entry.get())

        # self.pin_entry.delete(0, END)
        # self.confirm_entry.delete(0, END)

    def set_up_ui(self):
        self.pin_label.config(text="Enter Pin:")
        self.pin_label.grid(row=1, column=0, columnspan=1)
        self.pin_entry.grid(row=1, column=1)
        self.enter.grid(row=3, column=1)

    def no_set_up(self):
        self.pin_label.grid(row=1, column=0, columnspan=1)
        self.confirm_label.grid(row=2, column=0)
        self.pin_entry.grid(row=1, column=1)
        self.confirm_entry.grid(row=2, column=1)
        self.enter.grid(row=3, column=1)
