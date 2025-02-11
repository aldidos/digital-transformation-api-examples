import sys
sys.path.append('.')

from base_uri import BaseAPI, headers, data_to_json
import requests

class CenterAuthenticationAPI(BaseAPI) : 

    def __init__(self, uri) : 
        super().__init__(uri)

    def get(self, data) : 
        data = data_to_json(data)
        res = requests.get(self.uri, data = data, headers = headers)
        self.print_response('GET', res)
        return res

put_data = {
    'center_name' : 'test_center_1', 
    'center_address' : 'test_center_address_1dshjkdsa',
    'user_id' : '1'       
}

get_data = {
    'user_id' : 1,
    'center_id' : 1
}

if __name__ == '__main__' : 
    uri = f'/center_authentication' 
    api = CenterAuthenticationAPI(uri)

    # api.put(put_data)

    api.get(get_data)