#!/usr/bin/env python2
from __future__ import print_function
import os
import re
import sys
import urllib2
import json
import glob
import subprocess


def get_version_from_pypi(module_name):
    url = 'https://pypi.python.org/pypi/{}/json'.format(module_name)
    f = urllib2.urlopen(url)
    return json.loads(f.read())['info']['version']


def get_existing_spec_filename(spec_directory, module_name, module_version):
    find_spec_file_pattern = r'{}/{}-{}-fasrc[0-9]*.spec'.format(spec_directory, module_name, module_version)
    filenames = glob.glob(find_spec_file_pattern)
    if filenames:
        return os.path.basename(filenames[0])
    return None


def create_spec_path(spec_directory, module_name, module_version, helmod_version):
    helmod_version_str = str(helmod_version).zfill(2)
    return '{}/{}-{}-fasrc{}.spec'.format(spec_directory, module_name, module_version, helmod_version_str)


def get_next_fasrc_version(spec_directory, module_name):
    find_module_pattern = r'{}/{}-*-fasrc[0-9]*.spec'.format(spec_directory, module_name)
    filenames = glob.glob(find_module_pattern)
    max_helmod_version = 0
    for filename in filenames:
        version = get_fasrc_version(filename)
        max_helmod_version = max(max_helmod_version, version)
    return max_helmod_version + 1


def get_fasrc_version(filename):
    m = re.search('.*fasrc(.+).spec', filename)
    if m:
        return int(m.group(1))
    raise ValueError("Not a valid spec filename {}".format(filename))


def usage():
    print("usage: {} <MODULE_DIRECTORY> <PYPI_NAME> <MODULE_NAME> <INSTALL_SCRIPT>".format(sys.argv[0]))


def main():
    try:
        module_directory = sys.argv[1]
        pypi_name = sys.argv[2]
        module_name = sys.argv[3]
        install_command = sys.argv[4]
    except IndexError:
        usage()
        sys.exit(1)
    pypi_version = get_version_from_pypi(pypi_name)
    spec_filename = get_existing_spec_filename(module_directory, module_name, pypi_version)
    if spec_filename:
        print("Module already exists {}".format(spec_filename))
    else:
        fasrc_release = get_next_fasrc_version(module_directory, module_name)
        print("Installing {} version {}".format(module_name, pypi_version))
        subprocess.call([install_command, module_name, pypi_version, str(fasrc_release).zfill(2)])


if __name__ == "__main__":
    main()
