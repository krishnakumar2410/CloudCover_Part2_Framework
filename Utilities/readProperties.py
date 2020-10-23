import configparser
import sys
import os

config= configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")

class ReadConfig():
    @staticmethod
    def getUri():
        uri=config.get('common info','uri')
        return uri

    @staticmethod
    def getfilepath():
        # Uncomment of in case if we run without pytest
        #path_current_directory = sys.path[1]
        #path_data_file = os.path.join(path_current_directory, 'TestData', 'expected_bids.csv')
        path_data_file=config.get('common info','datafilepath')
        return path_data_file