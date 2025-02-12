'''
====================================================================================
API : /signin
    Methods : 
        PUT : 
            status code: 
                200 : OK
                400 : Bad Request        
====================================================================================
'''

import sys
sys.path.append('.')

from base_uri import BaseAPI

data = {
    'login_id' : 'test_user_1', 
    'login_pw' : 'aaaaaabb'
}

def main() : 
    uri = f'/signin' 
    api = BaseAPI(uri)

    api.put(data)

if __name__ == '__main__' : 
    main()