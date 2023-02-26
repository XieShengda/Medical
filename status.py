from enum import Enum, unique


@unique
class Status(Enum):
    Raw = 0
    Processing = 1
    Completed = 2
