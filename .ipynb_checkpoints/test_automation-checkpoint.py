# coding=utf-8
"""Generate unit tests "on-the-fly" based upon JSON files which exist in the designated folder."""

import glob
import os
import pytest

import configparser
import ujson

# TODO: Run locate tests, and run tests concurrently -> asyncio
# TODO: Manage the JSON files (update/delete/create) via RESTful API/Web Portal
# TODO: PYTEST conventions:
# Exit code 0:	All tests were collected and passed successfully
# Exit code 1:	Tests were collected and run but some of the tests failed
# Exit code 2:	Test execution was interrupted by the user
# Exit code 3:	Internal error happened while executing tests
# Exit code 4:	pytest command line usage error
# Exit code 5:	No tests were collected
# TODO: How to know which path to use to locate the JSON files?
# For now, we are being lazy and using the current directory.
# TODO: Logging!

REQUIRED_PARAMS = ('module', 'function', 'args', 'kwargs', 'expected_result')
SETTINGS_FILE = ''
SETTINGS = dict(configparser.RawConfigParser().read(SETTINGS_FILE))


def iter_json_files(directory: str, recursive=False) -> str:
    """Locate JSON files within the given directory.  Optionally look recursively."""
    for filename in glob.iglob('{}/*'.format(directory), recursive=recursive):
        # Search for ".json" files.
        _, extension = os.path.splitext(filename)
        if extension == '.json':
            full_path = os.path.abspath(filename)
            # TODO: exclude, include files by fnmatch patterns?
            yield full_path


def gather_test_parameters(directory: str) -> None:
    """Locate and get parameters to run tests based upon JSON files."""
    # TODO: Use settings here!
    # recursive = True if SETTINGS['test_locating']['recursive'] == 'True' else False
    recursive = True
    for test_file in iter_json_files(directory, recursive=recursive):
        with open(test_file, 'rt') as json_file:
            test_parameters = ujson.load(json_file)
        yield test_parameters


# TODO: Update this when we aren't using current directory anymore; get it from pytest!
# i.e. make this an actual pytest plugin!
@pytest.mark.parametrize('test_parameters', gather_test_parameters(os.getcwd()))
def test_magic(test_parameters: dict):
    """Run a test based upon the given parameters dictionary."""
    missing = validate_parameters(test_parameters)
    missing_msg = 'Unit test is missing required parameters: {}.'.format(missing)
    assert not missing, missing_msg
    
    # TODO: Support Class __init__ and more complex operations...
    module = __import__(test_parameters['module'])
    funct = test_parameters['function']
    bad_funct = 'Unit test parameters are invalid.  {} has no {} member.'.format(module, funct)
    assert hasattr(module, funct), bad_funct

    # TODO: Run tests in parallel instead of serially -> asyncio?
    result = getattr(module, funct)(*test_parameters['args'], **test_parameters['kwargs'])
    expected_result = test_parameters['expected_result']
    # TODO: Custom failure messages
    # TODO: Custom test parameters, not just ==...
    assert result == expected_result


def validate_parameters(test_parameters: dict) -> set:
    """Ensure that tests have all of the required parameters."""
    # TODO: Get REQUIRED_PARAMS from settings?
    # TODO: Validate types and values?
    return set(param for param in REQUIRED_PARAMS if param not in test_parameters)
