import dataclasses


@dataclasses.dataclass
class ProfileMenu:
    size: int
    all_menu: list


@dataclasses.dataclass
class MobileTabName:
    tab_name: str
    title_name: str
