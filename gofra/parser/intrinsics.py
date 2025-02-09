from enum import IntEnum, auto


class Intrinsic(IntEnum):
    INCREMENT = auto()
    DECREMENT = auto()

    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    MODULUS = auto()

    EQUAL = auto()
    NOT_EQUAL = auto()
    LESS_THAN = auto()
    GREATER_THAN = auto()
    LESS_EQUAL_THAN = auto()
    GREATER_EQUAL_THAN = auto()

    COPY = auto()
    COPY_OVER = auto()
    COPY2 = auto()
    FREE = auto()
    SWAP = auto()


WORD_TO_INTRINSIC = {
    "+": Intrinsic.PLUS,
    "-": Intrinsic.MINUS,
    "*": Intrinsic.MULTIPLY,
    "/": Intrinsic.DIVIDE,
    "==": Intrinsic.EQUAL,
    "!=": Intrinsic.NOT_EQUAL,
    "<": Intrinsic.LESS_THAN,
    ">": Intrinsic.GREATER_THAN,
    ">=": Intrinsic.LESS_EQUAL_THAN,
    "<=": Intrinsic.GREATER_EQUAL_THAN,
    "%": Intrinsic.MODULUS,
    "dec": Intrinsic.DECREMENT,
    "inc": Intrinsic.INCREMENT,
    "swap": Intrinsic.SWAP,
    "copy": Intrinsic.COPY,
    "copy2": Intrinsic.COPY2,
    "copy_over": Intrinsic.COPY_OVER,
    "free": Intrinsic.FREE,
}
