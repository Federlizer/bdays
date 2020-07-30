import sys
import datetime
from pprint import pprint

import contact_manager
from person import Person

# globals
CONTACTS_FILENAME = 'contacts.json'

# commands
ADD_COMMAND = 'add'
LIST_COMMAND = 'list'

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
    else:
        print('Unknown command \'{}\''.format(command))
        return


if __name__ == '__main__':
    args = sys.argv[1:]
    main(len(args), args.copy())
