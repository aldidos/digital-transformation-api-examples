import sys
sys.path.append('.')

from base_uri import BaseAPI

class SignupAPI(BaseAPI) : 

    def __init__(self, uri) : 
        super().__init__(uri)

data = {
    'login_id' : 'test_user_1', 
    'login_pw' : 'aaaaaabb'
}

if __name__ == '__main__' : 
    uri = f'/signin' 
    api = SignupAPI(uri)

    api.put(data)