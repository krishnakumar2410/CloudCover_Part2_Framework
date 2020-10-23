import requests
import pytest
import json
import jsonpath
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig

class Test_Get_Badges_Names:
    uri = ReadConfig.getUri()
    logger = LogGen.loggen()

    @pytest.fixture()
    def setup(self):
        url = self.uri+"/2.2/badges/name?order=desc&sort=rank&site=stackoverflow"
        response = requests.get(url)
        return response


    def test_validateStatusCode(self,setup):
        response=setup
        self.logger.info("Test case test_validateStatusCode started")
        assert response.status_code == 200
        self.logger.info("Test case test_validateStatusCode finished")


    def test_Count_of_expected_badges_names(self,setup):
        response = setup
        self.logger.info("Test case test_Count_of_expected_badges_names started")
        responseJson = json.loads(response.text)
        badgecount= jsonpath.jsonpath(responseJson, 'items[*].badge_id')
        assert len(badgecount)==30
        self.logger.info("Tcest case test_Count_of_expected_badges_names finished")