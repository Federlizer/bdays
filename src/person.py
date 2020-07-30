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
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def to_json(self):
        """
        Transform person to a json readable data structure.
        """

        return {
            'name': self.name,
            'birthday': self.birthday.isoformat(),
        }
