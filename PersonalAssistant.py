class PersonalAssistant:
  def __init__(self, todos):

    # Contacts dictionary
    self.contacts = {
      'Ann': 'Marketing Coordinator',
      'Chelsea': 'Software Developer',
      'Nichole': 'Sales Representative',
      'Max': 'Technical Writer'
    }

    # Birthdays dictionary
    self.birthdays = {
      "Midge": "02/24/18",
      "Shea": "04/26/14",
      "Sammy": "05/15/17",
      "Ollie": "10/11/18"
    }

    # To-do list
    self.todos = todos

  # Get a contact from dictionary
  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "No Contact Found."

  # Add contact to dictionary
  def add_contact(self, name, position):
    if name in self.contacts:
      return "Contact already exists."
    else:
      self.contacts[name] = position

  # Remove contact from dictionary
  def remove_contact(self, name):
    if name in self.contacts:
      self.contacts.pop(name, None)
    else:
      return "No Contact Found."

  # Get to-do list
  def get_todo(self):
    return self.todos

  # Add a to-do to the list
  def add_todo(self, new_item):
    if new_item in self.todos and new_item != "":
      return "To-do is already on the list."
    else:
      self.todos.append(new_item)

  # Remove a to-do from the list
  def remove_todo(self, todo_item):
    # Checks if todo_item is in todos list
    if todo_item in self.todos:
      # Gets the todo_item index in list
      index = self.todos.index(todo_item)
      # pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
      return "To-do is not in list."

  # Get a birthday from the dictionary
  def get_birthday(self, name):
    if name in self.birthdays:
      return self.birthdays[name]
    else:
      return "No birthday found."

  # Add a birthday to the dictionary
  def add_birthday(self, name, birthday):
    if name in self.birthdays:
      return "This birthday is already saved."
    else:
      self.birthdays[name] = birthday

  # Remove a birthday from the dictionary
  def remove_birthday(self, name):
    if name in self.birthdays:
      self.birthdays.pop(name)
    else:
      return "No birthday found."
