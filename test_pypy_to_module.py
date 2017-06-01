import unittest
import urllib2
from pypi_to_module import get_existing_spec_filename, get_version_from_pypi, create_spec_path, \
    get_next_fasrc_version, get_fasrc_version

MODULE_DIRECTORY = './test_files'


class TestModuleBuilderFuncs(unittest.TestCase):
    def test_get_existing_spec_filename_existing_file1(self):
        spec_filename = get_existing_spec_filename(MODULE_DIRECTORY, 'perl', '5.10.1')
        self.assertEqual(spec_filename, 'perl-5.10.1-fasrc03.spec')

    def test_get_existing_spec_filename_existing_file2(self):
        spec_filename = get_existing_spec_filename(MODULE_DIRECTORY, 'perl', '5.10.3')
        self.assertEqual(spec_filename, 'perl-5.10.3-fasrc04.spec')

    def test_get_existing_spec_filename_no_version(self):
        spec_filename = get_existing_spec_filename(MODULE_DIRECTORY, 'perl', '5.10.5')
        self.assertEqual(spec_filename, None)

    def test_get_existing_spec_filename_no_module(self):
        spec_filename = get_existing_spec_filename(MODULE_DIRECTORY, 'nodejs', '5.10.1')
        self.assertEqual(spec_filename, None)

    def test_get_version_from_pypi_bogus_module(self):
        with self.assertRaises(urllib2.HTTPError):
            get_version_from_pypi('not-a-real-python-name')

    def test_get_version_from_pypi_known_module(self):
        version = get_version_from_pypi('DukeDSClient')
        self.assertIsNotNone(version)

    def test_create_spec_path(self):
        self.assertEqual('/tmp/modules/perl-5.10.1-fasrc01.spec',
                         create_spec_path('/tmp/modules', 'perl', '5.10.1', '1'))
        self.assertEqual('/tmp/modules/perl-5.10.3-fasrc12.spec',
                         create_spec_path('/tmp/modules', 'perl', '5.10.3', '12'))

    def test_get_next_helmod_version(self):
        # Current max perl version in MODULE_DIRECTORY is 4
        next_version = get_next_fasrc_version(MODULE_DIRECTORY, 'perl')
        self.assertEqual(5, next_version)

    def test_get_next_helmod_version_new_module(self):
        # There are no spec files in MODULE_DIRECTORY for newperl
        next_version = get_next_fasrc_version(MODULE_DIRECTORY, 'newperl')
        self.assertEqual(1, next_version)

    def test_get_helmod_version(self):
        self.assertEqual(1, get_fasrc_version('/tmp/modules/perl-5.10.1-fasrc01.spec'))
