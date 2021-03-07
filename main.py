import json

import remi.gui as gui
from remi import start
from base_app import BaseApp

class MyApp(BaseApp):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    # Error message
    def add_error(self, error):
      self.errors.append(gui.ListItem(error))

    # Clear error message
    def clear_errors(self):
      self.errors.empty()

    # Add new to-do or get error message
    def add_todo(self, widget):
        todo_item = self.textinput.get_value()
        error = self.assistant.add_todo(todo_item)
        if error:
          self.add_error(error)

        # update json file
        with open("todo.json", "w") as write_file:
            json.dump(self.assistant.get_todo(), write_file)
        self.reset_dropdown(widget)

    # Remove to-do or get error message
    def remove_todo(self, widget):
        todo_item = self.textinput.get_value()
        error = self.assistant.remove_todo(todo_item)
        if error:
          self.add_error(error)

        # update json file
        with open("todo.json", "w") as write_file:
            json.dump(self.assistant.get_todo(), write_file)
        self.reset_dropdown(widget)

    # Add a birthday
    def add_birthday(self, widget):
        name = self.textinput.get_value()
        birthday = self.textinput2.get_value()
        if name != "" and birthday != "":
            error = self.assistant.add_birthday(name, birthday)
            if error:
                self.add_error(error)
            else:
                self.reset_dropdown(widget)
        self.reset_dropdown(widget)

    # Remove a birthday
    def remove_birthday(self, widget):
        name = self.textinput.get_value()

        error = self.assistant.remove_birthday(name)
        if error:
          self.add_error(error)

        self.reset_dropdown(widget)

    # Get birthday dictionary
    def get_birthday(self, widget):
        self.dialog = gui.GenericDialog(title="Get Birthday", width="500px")
        name = self.textinput.get_value()
        result = self.assistant.get_birthday(name)
        self.label = gui.Label(name + " is " + result, width=200, height=30)
        self.dialog.add_field("label", self.label)
        self.dialog.cancel_dialog.connect(self.reset_dropdown)
        self.dialog.show(self)
        self.reset_dropdown(widget)

    # Add contact
    def add_contact(self, widget):
        self.clear_errors()
        name = self.textinput.get_value()
        contact = self.textinput2.get_value()
        if name != "" and contact != "":
            error = self.assistant.add_contact(name, contact)
            if error:
                self.add_error(error)
            else:
                self.reset_dropdown(widget)

    # Remove contact
    def remove_contact(self, widget):
        name = self.textinput.get_value()
        error = self.assistant.remove_contact(name)
        if error:
            self.add_error(error)
        self.reset_dropdown(widget)

    # Get a contact
    def get_contact(self, widget):
        self.dialog = gui.GenericDialog(title="Get Contact", width="500px")
        name = self.textinput.get_value()
        result = self.assistant.get_contact(name)
        self.label = gui.Label(name + " is " + result, width=200, height=30)
        self.dialog.add_field("label", self.label)
        self.dialog.cancel_dialog.connect(self.reset_dropdown)
        self.dialog.show(self)
        self.reset_dropdown(widget)

    def reset_dropdown(self, widget):
        self.todoDropDown.select_by_value("")
        self.birthdayDropDown.select_by_value("")
        self.contactDropDown.select_by_value("")



start(MyApp, debug=False, address="0.0.0.0", port=3000, multiple_instance=True)
