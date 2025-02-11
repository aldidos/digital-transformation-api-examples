import sys
sys.path.append('.')

from examples.config import base_url, headers
import requests
import json
from base_uri import BaseAPI

class SignupAPI(BaseAPI) : 

    def __init__(self, uri) : 
        super().__init__(uri)

user_account = {
    'login_id' : 'tester_id', 
    'login_pw' : 'tester_id_pw'
}

user_info = {
    'name' : '테스터', 
    'weight' : 75.5, 
    'height' : 175.4, 
    'birthday' : '1984-03-18', 
    'contact' : '010-1123-2841', 
    'gender' : '여'
}

data = {
    'user_account' : user_account, 
    'user_info' : user_info
}

if __name__ == '__main__' : 
    uri = f'/signup' 
    api = SignupAPI(uri)

    api.post(data)