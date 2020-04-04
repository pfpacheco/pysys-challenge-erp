from enum import Enum


class GroupEnum(Enum):

    ADMIN = 'ADMIN',
    CLIENT = 'CLIENT',
    VENDOR = 'VENDOR'

    def description(self):
        return self.name, self.value

    def __str__(self):
        return '{0}'.format(self.value)

    @classmethod
    def default_group(cls):
        return cls.CLIENT
