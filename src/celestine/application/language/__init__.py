"""Application for translating text to other languages."""
from celestine.core import load

from celestine.application.language.argument import parser


from celestine.application.language.keyword import APPLICATION
from celestine.application.language.keyword import LANGUAGE


def main(session):
    """def main"""

    argument = parser.parse_args()
    task = argument.task

    module = load.module(APPLICATION, LANGUAGE, task)
    module.main(argument=argument, session=session)
