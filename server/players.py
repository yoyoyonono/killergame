from enum import Enum, auto

class Teams(Enum):
    """
    Enum for different teams
    """
    GOOD = 0
    BAD = 1
    OTHER = 2

class PlayerTypes(Enum):
    """
    Enum for different player types
    """
    CIVILIAN = auto()
    CUPID = auto()
    PLAYBOY = auto()
    INFLUENCER = auto()
    DETECTIVE = auto()
    GUARD = auto()
    DOCTOR = auto()
    PSYCHO = auto()
    KNIGHT = auto()
    UNDERTAKER = auto()
    KILLER = auto()
    SURGEON = auto()
    SUPER = auto()
    ZOMBIE = auto()


class CanVote:
    pass

class CanKill:
    pass

class CanPlayboy:
    pass

class CanInfluence:
    pass

class CanPsycho:
    pass

class CanDoctor:
    pass

class CanGuard:
    pass