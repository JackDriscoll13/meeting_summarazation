# This module will outline and define the inital connection to open api
import os 
from dotenv import load_dotenv


def setup_openai_env():

    load_dotenv()
    aikey = os.getenv('OPENAI_API_KEY')
    orgkey = os.getenv('OPENAI_ORG_KEY')

    os.environ['REQUESTS_CA_BUNDLE'] = 'C:/Users/P3159331/Downloads/CharterRootCert.crt'
    return aikey, orgkey