from enum import Enum


class ItemEnum(Enum):
    """
    Enum class which represents various Item types.
    """
    TOY = "toy"
    ANIMAL = "animal"
    CANDY = "candy"


class ToffeeVariety(Enum):
    """
    Enum class which represents various Toffee Varieties.
    """

    SALT = "sea salt"
    REG = "regular"


class CandyCaneVariety(Enum):
    """
    Enum class which represents various CandyCane Varieties.
    """

    RED = "red"
    GREEN = "green"


class StuffingType(Enum):
    """
    An enum class with all stuffing types used in StuffedAnimal Class.
    """

    POLY = "polyester fiberfill"
    WOOL = "wool"


class FabricType(Enum):
    """
    An enum class with all fabric types used in StuffedAnimal Class.
    """

    LINEN = "linen"
    COTTON = "cotton"
    ACRYLIC = "acrylic"


class SizeOptions(Enum):
    """
    An enum class representing all the sizes of a StuffedAnimal.
    """

    SM = "small"
    MED = "medium"
    LRG = "large"


class EasterBunnyColors(Enum):
    """
    An enum class representing the possible colors
    of an EasterBunny Stuffed Animal
    """
    WHITE = "white"
    GREY = "grey"
    PINK = "pink"
    BLUE = "blue"


class SpiderType(Enum):
    """
    An enum class that represents the various Spider Types of an RC Spider.
    """
    TARANTULA = "tarantula"
    WOLF = "wolf spider"


class RobotBunnyColor(Enum):
    """
    An enum class that represents the various colors of a RobotBunny.
    """
    ORANGE = "orange"
    BLUE = "blue"
    PINK = "pink"