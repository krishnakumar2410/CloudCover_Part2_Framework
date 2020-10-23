import requests
import pytest
import json
import jsonpath
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_Get_Badges_ID:
    uri=ReadConfig.getUri()
    logger = LogGen.loggen()

    @pytest.fixture()
    def setup(self):
        url = self.uri+"/2.2/badges/5966?order=desc&sort=rank&site=stackoverflow"
        response = requests.get(url)
        return response

    def test_validateStatusCode(self,setup):
        response = setup
        self.logger.info("Test case test_validateStatusCode started")
        assert response.status_code == 200
        self.logger.info("Test case test_validateStatusCode finished!")

    def test_Count_of_expected_badges(self,setup):
        response = setup
        self.logger.info("Test case test_Count_of_expected_badges started")
        responseJson = json.loads(response.text)
        badgeidcount=len(jsonpath.jsonpath(responseJson, 'items[*].badge_id'))
        assert badgeidcount==1
        self.logger.info("Test case test_Count_of_expected_badges finished!")

    def test_validate_processedid_against_requestid_Passed(self,setup):
        response = setup
        self.logger.info("Test case test_validate_processedid_against_requestid_Passed started")
        responseJson = json.loads(response.text)
        resbadgeid =jsonpath.jsonpath(responseJson, 'items[0].badge_id')
        assert resbadgeid[0] == 5966
        self.logger.info("Test case test_validate_processedid_against_requestid_Passed finished!")

    def test_check_if_invalid_id_passed(self,setup):
        response = setup
        self.logger.info("Test case test_check_if_invalid_id_passed started")
        responseJson = json.loads(response.text)
        resitems = jsonpath.jsonpath(responseJson, 'items')
        lislength = resitems[0]
        assert len(lislength) !=0
        self.logger.info("Test case test_check_if_invalid_id_passed finished!")