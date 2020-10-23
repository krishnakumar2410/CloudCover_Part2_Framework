import requests
import pytest
import json
import jsonpath
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig

class Test_Get_Badges_ID_Recipients:
    uri=ReadConfig.getUri()
    logger = LogGen.loggen()

    @pytest.fixture()
    def setup(self):
        url = self.uri+"/2.2/badges/5966/recipients?site=stackoverflow"
        response = requests.get(url)
        return response

    @pytest.mark.skip(reason="Skiping this is just for testing purpose")
    def test_validateStatusCode(self,setup):
        response=setup
        self.logger.info("Test case test_validateStatusCode started")
        assert response.status_code == 200
        self.logger.info("Test case test_validateStatusCode finished")


    def test_Count_of_expected_recipients(self,setup):
        response = setup
        self.logger.info("Test case test_Count_of_expected_recipients started")
        responseJson = json.loads(response.text)
        usercount=len(jsonpath.jsonpath(responseJson, 'items[*].user'))
        assert usercount==1     # Failing intentionally, expected count is 2
        self.logger.info("Test case test_Count_of_expected_recipients finished")


    def test_validate_processedid_against_requestid_Passed(self,setup):
        response = setup
        self.logger.info("Test case test_validate_processedid_against_requestid_Passed started")
        responseJson = json.loads(response.text)
        resbadgeid =jsonpath.jsonpath(responseJson, 'items[0].badge_id')
        assert resbadgeid[0] == 5966
        self.logger.info("Test case test_validate_processedid_against_requestid_Passed finished")
