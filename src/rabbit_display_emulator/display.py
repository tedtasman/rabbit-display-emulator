from dataclasses import field, fields

from nicegui import binding


@binding.bindable_dataclass
class Side:
    text: str = '---'
    large: str = '000'
    small: str = '000'
    pips: int = 0


@binding.bindable_dataclass
class Shared:
    time: str = '00:00'
    small: str = '00'


@binding.bindable_dataclass
class Display:
    left: Side = field(default_factory=Side)
    shared: Shared = field(default_factory=Shared)
    right: Side = field(default_factory=Side)

    def update(self, data: dict) -> None:
        for section_name, values in data.items():
            section = getattr(self, section_name, None)
            if section is None or not isinstance(values, dict):
                continue
            names = {f.name for f in fields(section)}
            for key, value in values.items():
                if key in names:
                    setattr(section, key, value)


display = Display()