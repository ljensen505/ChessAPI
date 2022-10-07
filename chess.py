from dataclasses import dataclass


@dataclass
class Chess:
    turn:   int = 0
    orig:   str = ""
    dest:   str = ""
