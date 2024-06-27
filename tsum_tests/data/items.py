import dataclasses


@dataclasses.dataclass
class Item:
    item: str


@dataclasses.dataclass
class MobileItem:
    kind: str
    name: str
