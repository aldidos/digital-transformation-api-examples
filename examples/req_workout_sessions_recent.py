import sys
sys.path.append('.')

from examples.base_uri import BaseAPI, headers, data_to_json
import requests

class UserWorkoutSessionsRecentAPI(BaseAPI) : 

    def __init__(self, uri) : 
        super().__init__(uri)  

user_id = 1
if __name__ == '__main__' : 
    uri = f'/users/{user_id}/workout_sessions/recent' 
    api = UserWorkoutSessionsRecentAPI(uri)

    api.get()


  