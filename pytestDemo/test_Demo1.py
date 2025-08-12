#any pytest file should start with test_ or end with _test
# pytest method names should start with test
# any code should be wrapped in method only
#Method name should have sense
# -k stands for method name execution, -s logs in output -v stands for more info metadata
# You can run a specific file with #Command line "python -m pytest test_demo2.py -v -s" This will work even if pytest is not in your system’s PATH.
# you can mark (tag) tests. and then run with -m
# @pytest.mark.xfail this will execute but not consider in the report
# @pytest.mark.skip this will skip particular test
#fixture are used as setup and tear dowm method for testcases, conftest.py will generalize the same for the all test files
# datadriven and parameterization can be done with return statement in tuple format
#when you define fixture scope to class only, it will run once before class id initiate at the end
#pytest -n 2 for parallel test run execution.
# pytest --html reports/reports.html for generate reports.

import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("hello")

def test_SecondProgramCreditCard():
    print("Good Morning")
# To run tests from command prompt, type 'py.test -v -s'

def test_crossBrowser(crossBrowser):
    print(crossBrowser)


