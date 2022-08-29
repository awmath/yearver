from yearver.yearver import Version
import pytest
import freezegun


@pytest.fixture(autouse=True)
def _past():
    freezegun.freeze_time('2018')

@pytest.mark.parametrize('version', ['2018.1', '2018.12', '2019.12-alpha.3',  '2019.12-b.17'])
def test_version_validation(version):
    Version.validate_version(version)

@pytest.mark.parametrize('version', ['201801', '2018-01', '1.2.3','2019.12.alpha.3', '2019.12-alpha-3', '2019.12-alpha.b'])
def test_version_validation_error(version):
    with pytest.raises(AssertionError):
        Version.validate_version(version)


def test_year_change():
    release_2017 = Version.from_string('2017.11')
    str(Version.from_string('2017.11').bump(release_2017)) == '2018.1'
    str(Version.from_string('2014.11').bump(Version.from_string('2014.11'))) == '2018.1'

    str(Version.from_string('2018.1-alpha.2').bump(release_2017)) == '2018.1'

    str(Version.from_string('2017.11').bump(release_2017, channel='alpha')) == '2018.1-alpha.1'
    str(Version.from_string('2018.1-alpha.2').bump(release_2017, channel='alpha')) == '2018.1-alpha.3'

def test_release():
    release = Version.from_string('2018.11')

    str(Version.from_string('2018.11').bump(release)) == '2018.12'
    str(Version.from_string('2018.11-alpha.1').bump(release)) == '2018.12'
    str(Version.from_string('2018.11-alpha.3').bump(release)) == '2018.12'
    str(Version.from_string('2018.11-beta.3').bump(release)) == '2018.12'

def test_prerelase():
    release = Version.from_string('2018.11')

    str(Version.from_string('2018.11').bump(release, channel='alpha')) == '2018.12-alpha.1'
    str(Version.from_string('2018.11-alpha.3').bump(release, channel='alpha')) == '2018.12-alpha.4'
    str(Version.from_string('2018.11-beta.3').bump(release, channel='alpha')) == '2018.12-alpha.1'

def test_version_parser():
    version = Version.from_string('2019.17') 
    version.year == 2019
    version.iteration == 2019
    version.channel is None
    version.channel_iteration is None

    version = Version.from_string('2019.17-alpha.15')
    version.year == 2019
    version.iteration == 2019
    version.channel == 'alpha'
    version.channel_iteration == 15
