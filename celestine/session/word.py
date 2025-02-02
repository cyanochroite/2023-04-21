"""Build up strings here."""

import io

from celestine.typed import (
    L,
    S,
)
from celestine.unicode import (
    APOSTROPHE,
    COLON,
    COMMA,
    LEFT_PARENTHESIS,
    LINE_FEED,
    NONE,
    RIGHT_PARENTHESIS,
    SPACE,
)


def parser_error(argument: S, name: S, message: S) -> S:
    """"""
    string = io.StringIO()
    if name is not None:
        string.write(argument)
        string.write(SPACE)
        string.write(name)
        string.write(COLON)
        string.write(SPACE)
    string.write(message)
    value = string.getvalue()
    return value


def parser_formatter(usage: S) -> S:
    """"""
    string = io.StringIO()
    string.write(usage)
    string.write(COLON)
    string.write(SPACE)
    value = string.getvalue()
    return value


def parser_parser_error(program: S, error: S, message: S) -> S:
    """"""
    string = io.StringIO()
    string.write(program)
    string.write(COLON)
    string.write(SPACE)
    string.write(error)
    string.write(COLON)
    string.write(SPACE)
    string.write(message)
    string.write(LINE_FEED)
    value = string.getvalue()
    return value


def parser_value(choice: S, value: S, choose: S, choices: L[S]) -> S:
    """"""
    string = io.StringIO()
    string.write(choice)
    string.write(COLON)
    string.write(SPACE)
    string.write(APOSTROPHE)
    string.write(value)
    string.write(APOSTROPHE)
    string.write(SPACE)
    string.write(LEFT_PARENTHESIS)
    string.write(choose)
    string.write(SPACE)
    join = NONE.join([COMMA, SPACE])
    string.write(join.join(map(repr, choices)))
    string.write(RIGHT_PARENTHESIS)
    value = string.getvalue()
    return value
