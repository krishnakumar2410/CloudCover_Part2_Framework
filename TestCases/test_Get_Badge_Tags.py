import requests
import pytest
import json
import jsonpath
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig

class Test_Get_Badge_Tags:
    uri=ReadConfig.getUri()
    logger = LogGen.loggen()

    @pytest.fixture()
    def setup(self):
        url = self.uri+"/2.2/badges/tags?order=desc&sort=rank&site=stackoverflow"
        response = requests.get(url)
        return response


    def test_validateStatusCode(self,setup):
        response=setup
        self.logger.info("Test case test_validateStatusCode started")
        assert response.status_code == 200
        self.logger.info("Test case test_validateStatusCode finished")


    def test_Count_of_expected_tags(self,setup):
        response = setup
        self.logger.info("Test case test_Count_of_expected_tags started")
        responseJson = json.loads(response.text)
        usercount=len(jsonpath.jsonpath(responseJson, 'items[*].name'))
        assert usercount==30
        self.logger.info("Test case test_Count_of_expected_tags finished")