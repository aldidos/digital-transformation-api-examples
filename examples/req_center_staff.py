import sys
sys.path.append('.')

from examples.base_uri import BaseAPI

class CenterStaffAPI(BaseAPI) : 

    def __init__(self, uri) : 
        super().__init__(uri)

data = {    
    'center_id' : 1, 
    'name' : '센터 지원 5',
    'birth_day' : '1982-02-12' 
}

center_id = 1

if __name__ == '__main__' : 
    uri = f'/centers/{center_id}/staffs' 
    api = CenterStaffAPI(uri)

    api.post(data)

    api.get()