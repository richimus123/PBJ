# pytest_simple_json
Generate pytest cases based upon simple JSON files with a rich management portal.

  The intent of this project is to simplify management of Unit test datasets and automate unit testing in Python.  It should require much less human interaction and manual work to update/maintain unit test contents and write unit tests.  The motto in the design here is KISS (Keep it Simple Stupid) and hopefully everything will stay as simple and intuitive as possible.  This is intended for Python3.7.
  
# Goals:
* Automate unit test generation by just dropping a JSON file into a directory.
* Simple Django front-end and/or a RESTful API for managing the JSON test configurations to make it even easier.
* Write this as a pytest plugin for ease of use.
* ~100% Code test coverage -> pytest-cov and pytest-benchmark

# Current Features:  (this was just started, so expect updates relatively soon)
* JSON test file locating
* Simple settings via settings.ini
* Simple automation via JSON files

# Future Features:
* argparse front-end
* RESTful API
* Pretty and robust Django front-end for viewing/creating/updating/removing test contents and running pytest
* asyncio concurrency/parallelism
* Backwards compatibility
* JSON test file validation
* Make this a pytest plugin
* Automated changelog and versioning
* Logging
