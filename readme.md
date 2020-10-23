** Part 2- API Automation

# Tools/Technology Used
- Python, Pycharm, Pandas
- Framework: Pytest

1. Install Python 3
2. Install Pycharm editor if not already installed
3. Go to filea and click on create new project> Import downloaded project from GIT

#  Packages Required
- requests
- pytest
- json
- jsonpath
- pandas
- jsonschema

- For installation, go to Pycharm: File>Setting>Project:CloudCover>Python Interpreter > Add package.
- From command line: pip install package_name or python -m pip install package_name

#  Framework Folder Structure
__Project Name: Par2CloudCover__
- *Logs*: Execution logs getting stored here.
- *Reports* : Html file gets generated here, which we can open and check execution results for __pass/fail__ in browser.
- *TestCases*: All the api test cases are created here.
- *Utilities* : Here logger file created to print and store the logs for each execution. Additionaly ReadProperties is there which reads the url and path of the test data file from config.ini.
- *Configuration*: Here I have created config file where I have mentioned the common uri and data file path.
- *Test Data*: Here I have kept the expected badgeid csv file which I am using under Get_Badges request.


# Test Cases Covered 
__Most of test cases I have covered in *Get_Badges* request,we can replicate the same in others__
1. Status code check
2. Schema/DataType check using Draft6Validator
3. Empty response check
4. Number of items returned in response
5. Header Check 
6. Validation for bad parameter pass to requests
7. Reposne size
8. Validation for duplicate badgeID in response
9. Validation of expected badgeid in response

#  Steps to execute the test cases
- Go to terminal tab of the Pycharm
- Use below command to run

- pytest -s -v TestCases --html=Reports/SuiteExecutionResult.html [__This is for all the test cases to run at one go__]
- pytest -s -v TestCases/test_Get_Badges.py --html=Reports/test_Get_Badges.html
- pytest -s -v TestCases/test_Get_Badges_ID.py --html=Reports/test_Get_Badges_ID.html- Pass
- pytest -s -v TestCases/test_Get_BadgeNames.py --html=Reports/test_Get_BadgeNames.html- Pass
- pytest -s -v TestCases/test_Get_Badge_Recipients.py --html=Reports/test_Get_Badge_Recipients.html- Pass
- pytest -s -v TestCases/test_Get_Badge_ID_Recipients.py --html=Reports/test_Get_Badge_ID_Recipients.html- Pass
- pytest -s -v TestCases/test_Get_Badge_Tags.py --html=Reports/test_Get_Badge_Tags.html- Pass

# Note
- *TestCases.test_Get_BadgeNames.Test_Get_Badges_Names*: This request sometimes does not work if we hit multiple times from same IP and gives below response, in that case this will fail
{
    "error_id": 502,
    "error_message": "Violation of backoff parameter",
    "error_name": "throttle_violation"
}

- *test_Get_Badge_ID_Recipients.Test_Get_Badges_ID_Recipients*: This is have failed intentionally, we can change the expected count and it will pass
- *test_Get_Badge_ID_Recipients.py::Test_Get_Badges_ID_Recipients*: This is skipped through pytest framework for testing purpose 
