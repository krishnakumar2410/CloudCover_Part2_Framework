import requests
import pytest
import json
import jsonpath
from jsonschema import Draft6Validator
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
import pandas as pd

class Test_Get_Badges:
    uri=ReadConfig.getUri()
    logger = LogGen.loggen()
    datafilepath = ReadConfig.getfilepath()


    @pytest.fixture()
    def setup(self):
        url = self.uri+"/2.2/badges?order=desc&sort=rank&site=stackoverflow"
        response = requests.get(url)
        return response


    def test_validateStatusCode(self,setup):
        response=setup
        self.logger.info("Test case test_validateStatusCode started")
        assert response.status_code == 200
        self.logger.info("Test case test_validateStatusCode finished")


    def test_Count_of_expected_badges(self,setup):
        response = setup
        self.logger.info("Test case test_Count_of_expected_badges started")
        responseJson = json.loads(response.text)
        badgeidcount=len(jsonpath.jsonpath(responseJson, 'items[*].badge_id'))
        assert badgeidcount==30
        self.logger.info("Test case test_Count_of_expected_badges finished")


    def test_validate_Data_Header_Present(self,setup):
        response = setup
        self.logger.info("Test case test_validate_Data_Header_Present started")
        assert response.headers.get('date')
        self.logger.info("Test case test_validate_Data_Header_Present finished")


    def test_validate_if_response_is_empty(self,setup):
        response = setup
        self.logger.info("Test case test_validate_if_response_is_empty started")
        responseJson = json.loads(response.text)
        badgeidcount = len(jsonpath.jsonpath(responseJson, 'items[*].badge_id'))
        assert badgeidcount != 0
        self.logger.info("Test case test_validate_if_response_is_empty finished")


    def test_validate_response_for_bad_parameter_pass(self,setup):
        response = setup
        self.logger.info("Test case test_validate_response_for_bad_parameter_pass started")
        assert response.status_code != 400
        self.logger.info("Test case test_validate_response_for_bad_parameter_pass finished")


    def test_validate_resposesize_not_greaterthan_10000bytes(self,setup):
        response = setup
        self.logger.info("Test case test_validate_resposesize_not_greaterthan_10000bytes started")
        resSize= len(response.content)
        assert resSize < 10000
        self.logger.info("Test case test_validate_resposesize_not_greaterthan_10000bytes finished")


    def test_schema_datatype_validations(self,setup):
        self.logger.info("Test case test_schema_datatype_validations started")
        schema = {
            "type": "object",
            "properties": {
                "quota_max": {"type": "number"},
                "items": {
                    "type": "array",
                    "maxItems": 1,  # Check max items in array
                    "items": {
                        "type": "object",
                        "properties": {
                            "badge_type": {"type": "string"},
                            "award_count": {"type": "number"},
                            "badge_id": {"type": "number"},

                        },
                        "required": ["badge_id"]
                    }
                }
            },
            "required": ["quota_max"]
        }

        Draft6Validator.check_schema(schema)
        self.logger.info("Test case test_schema_datatype_validations finished")

    def test_validate_if_any_duplciate_badgeid_present_in_respose(self,setup):
        response=setup
        self.logger.info("Test case test_validate_if_any_duplciate_badgeid_present_in_respose started")
        responseJson = json.loads(response.text)
        badgeId = jsonpath.jsonpath(responseJson, 'items[*].badge_id')
        duplicate = []
        for i in range(len(badgeId)):
            k = i + 1
            for j in range(k, len(badgeId)):
                if badgeId[i] == badgeId[j] and badgeId[i] not in duplicate:
                    duplicate.append(badgeId[i])
        print(duplicate)
        assert len(duplicate) != 1
        self.logger.info("Test case test_validate_if_any_duplciate_badgeid_present_in_respose finished")

    def test_validate_badgeIds_against_expected_badgeids(self,setup):
        response = setup
        self.logger.info("Test case test_validate_badgeIds_against_expected_badgeids started")
        responseJson = json.loads(response.text)
        resbadgeId = jsonpath.jsonpath(responseJson, 'items[*].badge_id')

        #Get the ids from expected data file
        df = pd.read_csv(self.datafilepath, skiprows=[1])
        csvbadgeid = df.values.tolist()
        flat_list = [item for sublist in csvbadgeid for item in sublist] # Created flat list from list of list
        diff_list = [i for i in resbadgeId + flat_list if i not in resbadgeId or i not in flat_list]
        print(diff_list)
        assert len(diff_list) == 0
        self.logger.info("Test case test_validate_badgeIds_against_expected_badgeids finished")