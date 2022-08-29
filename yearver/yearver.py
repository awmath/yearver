"""Main module."""
#!/bin/python3
from datetime import datetime
import sys
import re

VERSION_REGEX = '^[0-9]{4}\.[0-9]+(?:-[a-z]+\.[0-9]+)?$'

class Version:
    """
    year version based class
    """

    year: int = None
    iteration: int = None
    pr_name: str = None
    pr_iteration: str = None

    def __init__(self, year, iteration, pr_name, pr_iteration):
        self.year = year
        self.iteration = iteration
        self.pr_name = pr_name
        self.pr_iteration = pr_iteration
    
    @classmethod
    def from_string(version_string):
        """
        create Version instance from given string representation

        Args:
            version_string (str): version string with VERSION_REGEX pattern

        Returns:
            Version: instance with parsed version string
        """
        return Version(*self.parse_version(version))

    def __eq__(self, other): 
        if not isinstance(other, MyClass):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.year == other.year and self.iteration == other.iteration and self.pr_name == other.pr_name and self.pr_iteration == other.pr_iteration

    def __str__(self):
        if self.pr_name is None:
            return '{}.{}'.format(self.year, self.iteration)

        return '{}.{}-{}.{}'.format(self.year, self.iteration, self.pr_name, self.pr_iteration)


    @staticmethod
    def validate_version(version):
        """
        validate wether a version string matched the year scheme regex

        Args:
            version (str): version string
        """
        assert re.match(VERSION_REGEX, version), f"{version} does not match the expected version format: year.count[-prerelease.prereleasecount]"

    @staticmethod
    def parse(version_string):
        """
        parse a given version string

        Args:
            version_string (_type_): _description_

        Returns:
            _type_: _description_
        """
        # try to split main and prelease
        pr_name = None
        pr_iteration = None
        try:
            main, prelease = version_string.split('-')
            pr_name, pr_iteration = prelease.split('.')

        except ValueError:
            return int(year), int(iteration)

        year, iteration = main.split('.')

        return int(year), int(iteration), pr_name, int(pr_iteration)

    @property
    def is_prerelease(self):
        return self.pr_name is not None
    


def bump(release: Version, current: Version):
    assert release.is_prerelease() is False, "The last release version can't be a prerelease"

    # if the last release was no prelease bump
    if release == current:
        current.iteration += 1
        return current
    
    new_version = Version()

    current_year = datetime.now().year
    version_year, iteration = main.split('.')

    # if we have a new year we start with iteration 1
    if current_year != version_year:
        new_main = f'{current_year}.1'

    # request release but last is prerelease
    # keep last intended version
    elif channel is None and prelease is not None:
        new_main = main
    
    # last release was a pr and request is also a pr
    elif channel is not None and prelease is not None:

    # same channel as last pr is requested
    elif channel == pr_name:

    
        

    


