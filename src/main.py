import sys
import datetime
import smtplib
from pprint import pprint
from typing import List

import contact_manager
from person import Person

# globals
CONTACTS_FILENAME = 'contacts.json'

# commands
ADD_COMMAND   = 'add'
LIST_COMMAND  = 'list'
CHECK_COMMAND = 'check'

def main(argc, argv):
    # TODO: provide help string
    if argc < 1:
        print('You need to provide a command')
        return

    command = argv[0].lower()

    if command == ADD_COMMAND:
        name = ' '.join(argv[1:-1])
        birthday = datetime.date.fromisoformat(argv[-1])

        person = Person(name, birthday)

        contact_manager.add_contact(person, CONTACTS_FILENAME)

    elif command == LIST_COMMAND:
        contacts = contact_manager.get_contacts(CONTACTS_FILENAME)
        pprint(contacts)

    elif command == CHECK_COMMAND:
        all_contacts = contact_manager.get_contacts(CONTACTS_FILENAME)
        have_bday_today = [contact for contact in all_contacts if has_bday_today(contact)]

        print(have_bday_today)

    else:
        print('Unknown command \'{}\''.format(command))
        return


def has_bday_today(person: Person) -> bool:
    """
    Checks if the person passed has a birthday today.

    Parameters
    ----------
    person: Person
    """

    today = datetime.date.today()
    persons_birthday = datetime.date(
        today.year,
        person.birthday.month,
        person.birthday.day)

    if persons_birthday == today:
        return True

    return False


def send_mail(contacts: List[Person]):
    with smtplib.SMTP('localhost') as smtp:
        smtp.sendmail('noreply@federlizer.com', 'federlizer@gmail.com', 'Some test string')

        # TODO: Finish me

if __name__ == '__main__':
    args = sys.argv[1:]
    main(len(args), args.copy())
