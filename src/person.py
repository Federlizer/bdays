from datetime import date

class Person():
    """
    A class to represent a person.

    Attributes
    ----------
    name: str
        a name for the person, should be unique, not enforced
    birthday: date
        the date at which this person is born

    """


    BDAY_FORMAT = '%d %b %Y'


    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday


    def __repr__(self):
        return '{}: {}'.format(self.name, self.birthday.__format__(Person.BDAY_FORMAT))


    def to_json(self):
        """
        Transform person to a json readable data structure.
        """

        return {
            'name': self.name,
            'birthday': self.birthday.isoformat(),
        }


    @staticmethod
    def from_dict(person_dict: dict):
        """
        Builds a person entity from a dictionary.

        The dictionary must oblige the following standard:
        person['name']: the name of the person
        person['birthday']: an iso format string of a date, example: 2020-07-31
        """

        name = person_dict['name']
        birthday = date.fromisoformat(person_dict['birthday'])

        return Person(name, birthday)