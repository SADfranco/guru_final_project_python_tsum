import dataclasses


@dataclasses.dataclass
class ExistingUser:
    first_name: str
    last_name: str
    email: str
    password: str


@dataclasses.dataclass
class NonExistingUser:
    first_name: str
    email: str
    password: str
