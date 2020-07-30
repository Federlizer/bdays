import json

def add_contact(person, filepath):
    """
    Adds a contact to the contacts file

    Parameters
    ----------
    person: Person
        a person object
    filepath: str
        a path to the contacts file including the file name itself
    """

    contacts = []

    with open(filepath, 'r') as contacts_file:
        contacts = json.load(contacts_file)

    print(contacts)
    contacts.append(person.to_json())
    print(contacts)

    with open(filepath, 'w') as contacts_file:
        json.dump(contacts, contacts_file)


def get_contacts(filepath):
    """
    Opens, reads and returns all contacts from `filepath`

    Parameters
    ----------
    filepath: str
        a path to the contacts file including the file name itself
    """

    contacts = []

    with open(filepath, 'r') as contacts_file:
        contacts = json.load(contacts_file)

    return contacts