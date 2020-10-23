import requests
import pytest
import json
import jsonpath
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig

class Test_Get_Badge_Recipients:
    uri=ReadConfig.getUri()
    logger = LogGen.loggen()

    @pytest.fixture()
    def setup(self):
        url = self.uri+"/2.2/badges/recipients?site=stackoverflow"
        response = requests.get(url)
        return response


    def test_validateStatusCode(self,setup):
        response=setup
        self.logger.info("Test case test_validateStatusCode started")
        assert response.status_code == 200
        self.logger.info("Test case test_validateStatusCode finished")


    def test_Count_of_expected_recipients(self,setup):
        response = setup
        self.logger.info("Test case test_Count_of_expected_recipients started")
        responseJson = json.loads(response.text)
        usercount=jsonpath.jsonpath(responseJson, 'items[*].user')
        assert len(usercount)==30
        self.logger.info("Test case test_Count_of_expected_recipients finished")