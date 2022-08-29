from yearver import Version
import pytest
import freezegun

freezegun.freeze_time('2018')

@pytest.mark.parametrize('version', ['2018.1', '2018.12', '2019.12-alpha.3',  '2019.12-b.17'])
def test_version_validation(version):
    Version.validate_version(version)

@pytest.mark.parametrize('version', ['201801', '2018-01', '1.2.3','2019.12.alpha.3', '2019.12-alpha-3', '2019.12-alpha.b'])
def test_version_validation_error(version):
    with pytest.raises(AssertionError):
        Version.validate_version(version)


def test_new_version_iteration():
    assert Version('2018.1').bump() == '2018.2'
    assert Version('2018.11').bump() == '2018.3'


def test_version_parser():
    version = Version.from_string('2019.17') 
    version.year == 2019
    version.iteration == 2019
    version.pr_name is None
    version.pr_iteration is None

    version = Version.from_string('2019.17-alpha.15')
    version.year == 2019
    version.iteration == 2019
    version.pr_name == 'alpha'
    version.pr_iteration == 15
