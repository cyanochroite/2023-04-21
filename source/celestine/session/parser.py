""""""

import argparse
import dataclasses

import types
import typing

from celestine.session.argument import Argument
from celestine.session.argument import Optional
from celestine.session.argument import Override
from celestine.session.argument import Name

from celestine.session.argument import Positional


from celestine.text.unicode import NONE


from celestine.session import load

from celestine.text import CELESTINE
from celestine.text import VERSION_NUMBER

from celestine.text.directory import APPLICATION
from celestine.text.directory import LANGUAGE

from celestine.text.session import HELP
from celestine.text.session import STORE_TRUE
from celestine.text.session import VERSION

from celestine.text.unicode import HYPHEN_MINUS
from celestine.text.unicode import QUESTION_MARK

from celestine.session.configuration import Configuration

CONFIGURATION = "configuration"


class Hippo():
    """"""

    def __init__(
        self,
        application: str,
        language: str,
        *path: str,
    ):

        self.application = application
        self.language = language

        module = load.module(*path)

        self.attribute = module.Session()
        self.dictionary = self.attribute.dictionary(self.language)

    def items(
        self,
    ) -> typing.Iterable[typing.Tuple[str, Argument]]:
        """"""

        return self.dictionary.items()


class Parser():
    """"""

    @ staticmethod
    def flag(
        name: str
    ) -> str:
        """name = -n"""

        iterable = (HYPHEN_MINUS, name[0])
        return str().join(iterable)

    @ staticmethod
    def name(
        name: str
    ) -> str:
        """name = --name"""

        iterable = (HYPHEN_MINUS, HYPHEN_MINUS, name)
        return str().join(iterable)

    def __init__(
        self,
        args: list[str],
        exit_on_error: bool
    ) -> None:
        """"""

        parser = argparse.ArgumentParser(
            add_help=False,
            exit_on_error=exit_on_error,
        )

        idea = {
            APPLICATION: Name(APPLICATION),
            LANGUAGE: Name(LANGUAGE),
        }

        parser.add_argument(
            self.flag(APPLICATION),
            self.name(APPLICATION),
        )

        parser.add_argument(
            self.flag(LANGUAGE),
            self.name(LANGUAGE),
        )

        (parse_known_args, _) = parser.parse_known_args(args)

        configuration = Configuration.make()

        override = parse_known_args.application
        database = configuration.get(CELESTINE, APPLICATION)
        fallback = "__init__"
        application = override or database or fallback

        override = parse_known_args.language
        database = configuration.get(CELESTINE, LANGUAGE)
        fallback = "__init__"
        language = override or database or fallback

        language = load.module_fallback(LANGUAGE, parse_known_args.language)

        # (application, language) = self.essential(args, exit_on_error)

        self.dictionary: typing.Dict[str, str] = {}
        self.parser = argparse.ArgumentParser(
            add_help=False,
            prog=CELESTINE,
            exit_on_error=exit_on_error,
        )

        # FLAGS WITH NO PARAMETER
        self.information = self.parser.add_argument_group(
            title=language.ARGUMENT_INFORMATION_TITLE,
            description=language.ARGUMENT_INFORMATION_DESCRIPTION,
        )

        self.override = self.parser.add_argument_group(
            title=language.ARGUMENT_OVERRIDE_TITLE,
            description=language.ARGUMENT_OVERRIDE_DESCRIPTION,
        )

        self.positional = self.parser.add_argument_group(
            title=language.ARGUMENT_OVERRIDE_TITLE + "MOO",
            description=language.ARGUMENT_OVERRIDE_DESCRIPTION + "COW",
        )

        self.optional = self.parser.add_argument_group(
            title=language.ARGUMENT_OVERRIDE_TITLE + "MOO",
            description=language.ARGUMENT_OVERRIDE_DESCRIPTION + "COW",
        )

        self.information.add_argument(
            self.flag(CONFIGURATION),
            self.name(CONFIGURATION),
            action=STORE_TRUE,
            help=language.ARGUMENT_HELP_HELP,
        )

        self.information.add_argument(
            self.flag(HELP),
            self.name(HELP),
            action=HELP,
            help=language.ARGUMENT_HELP_HELP,
        )

        self.information.add_argument(
            self.flag(VERSION),
            self.name(VERSION),
            action=VERSION,
            help=language.ARGUMENT_VERSION_HELP,
            version=VERSION_NUMBER,
        )

        # ignore above for now

        self.add_argument = {}
        self.add_argument[Positional] = self.positional
        self.add_argument[Optional] = self.optional
        self.add_argument[Override] = self.override

        # rest of stuff
        self.args = args
        self.application = application
        self.language = language
        self.configuration = configuration

    def dostuff(self):

        old_attribute = Hippo(
            self.application,
            self.language,
            "session",
            "session",
        )
        new_attribute = Hippo(
            self.application,
            self.language,
            APPLICATION,
            self.application,
        )

        self.head(old_attribute)
        self.head(new_attribute)
        self.parse_args = self.parser.parse_args(self.args)
        self.foot(old_attribute)
        self.foot(new_attribute)

        self.configuration.save()

        session = old_attribute.attribute
        session.attribute = new_attribute.attribute

        return session

    def head(  # feed the parser
        self,
        attribute: Hippo,
    ) -> None:
        """"""

        for (name, argument) in attribute.items():
            (args, kwargs) = argument.value(name)
            parser = self.add_argument[argument]
            parser.add_argument(*args, **kwargs)

    def foot(
        self,
        attribute: Hippo,
    ) -> None:
        """"""

        application = attribute.application

        for (name, fallback) in attribute.items():
            override = getattr(self.parse_args, name, NONE)
            database = self.configuration.get(application, name)
            value = override or database or fallback.fallback
            setattr(attribute.attribute, name, value)
            if self.parse_args.configuration:
                self.configuration.set(application, name, override)


def start_session(
    argv: list[str],
    exit_on_error: bool,
) -> None:
    """"""

    argument = Parser(argv, exit_on_error)
    session = argument.dostuff()
    return session
