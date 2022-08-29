"""Main module."""
#!/bin/python3
from datetime import date
import sys
import re

VERSION_REGEX = "^[0-9]{4}\\.[0-9]+(?:-[a-z]+\\.[0-9]+)?$"

class Version:
    """
    year version based class
    """

    year: int = None
    iteration: int = None
    channel: str = None
    channel_iteration: str = None

    def __init__(self, year, iteration, channel=None, channel_iteration=None):
        self.year = year
        self.iteration = iteration
        self.channel = channel
        self.channel_iteration = channel_iteration

    
    def bump(self, release, channel=None):
        assert release.is_prerelease is False, "The last release version can't be a prerelease"
        
        # if we have a new year we start with iteration 1
        year_now = date.today().year

        # handle year changes
        if channel is None:
            if release.year != year_now:
                # if the year has changed start a new cycle
                return Version(year=year_now, iteration=1)
        else:
            if self.year != year_now:
                # if the year has changed start a new cycle
                return Version(year=year_now, iteration=1, channel=channel, channel_iteration=1)
        
        # from now on we don't have to deal with year changes
        new_version = Version(year=self.year)

        # no prerelease -> bump to next version
        if channel is None:
            return Version(year=year_now, iteration=release.iteration + 1)

        # prerelease
        # if release iteration changed start a new channel cycle
        next_iteration = release.iteration + 1
        if self.iteration != next_iteration:
            return Version(year=year_now, iteration=next_iteration, channel=channel, channel_iteration=1)

        # if release channel changed start a new cycle
        if self.channel != channel:
            return Version(year=year_now, iteration=next_iteration, channel=channel, channel_iteration=1)

        if self.channel == channel:
            return Version(year=year_now, iteration=next_iteration, channel=channel, channel_iteration=self.channel_iteration + 1)
            

        raise RuntimeError('No release version could be created.')


    @classmethod
    def from_string(cls, version_string):
        """
        create Version instance from given string representation

        Args:
            version_string (str): version string with VERSION_REGEX pattern

        Returns:
            Version: instance with parsed version string
        """
        return cls(*cls.parse(version_string))
    

    def __str__(self):
        if self.channel is None:
            return '{}.{}'.format(self.year, self.iteration)

        return '{}.{}-{}.{}'.format(self.year, self.iteration, self.channel, self.channel_iteration)


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
        channel = None
        channel_iteration = None
        parts = version_string.split('-')
        main = parts[0]
        year, iteration = main.split('.')
        try:
            channel, channel_iteration = parts[1].split('.')
        except IndexError:
            return int(year), int(iteration), None, None

        return int(year), int(iteration), channel, int(channel_iteration)

    @property
    def is_prerelease(self):
        return self.channel is not None
