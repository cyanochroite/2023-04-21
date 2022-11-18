import configparser
import os

from celestine.string.all import CELESTINE
from celestine.string.session import CONFIGURATION
from celestine.string.session import WRITE
from celestine.string.session import UTF_8


class Configuration():
    """parse configuration stuff."""

    def __init__(self, directory):
        self.directory = directory
        self.path = os.path.join(directory, CELESTINE, CONFIGURATION)

    def load(self, path=None):
        """Load the configuration file."""
        configuration = configparser.ConfigParser()
        configuration.read(path or self.path, encoding=UTF_8)
        return configuration

    @staticmethod
    def make(directory):
        """Make a new configuration file."""
        configuration = Configuration(directory)
        return configuration.load()

    def save(self, configuration, path=None):
        """Save the configuration file."""
        with open(path or self.path, WRITE, encoding=UTF_8) as file:
            configuration.write(file, True)

    def add_configuration(self, configuration, module, application):
        """Build up the configuration file."""
        if not configuration.has_section(application):
            configuration.add_section(application)
        attribute = module.attribute()
        default = module.default()
        for item in zip(attribute, default, strict=True):
            (name, value) = item
            configuration.set(application, name, value)

        return configuration
