import sys
sys.path.append('.')

from examples.base_uri import BaseAPI

class CenterEquipmentAPI(BaseAPI) : 

    def __init__(self, uri) : 
        super().__init__(uri)

center_id = 1

if __name__ == '__main__' : 
    uri = f'/centers/{center_id}/equipments' 
    api = CenterEquipmentAPI(uri)

    api.get()