import sys
sys.path.append('.')

from examples.base_uri import BaseAPI, headers, data_to_json
import requests

class UserWorkoutSessionsAPI(BaseAPI) : 

    def __init__(self, uri) : 
        super().__init__(uri)

    def get(self, query_params) : 
        query_params = data_to_json(query_params)
        res = requests.get(self.uri, params=query_params,  headers = headers)
        self.print_response('GET', res) 

data = {
    'user' : 1, 
    'date' : '2025-02-11', 
    'status' : 'Process',
    'is_completed' : False    
}

query_params = {
    'from_date' : '2025-01-01', 
    'to_date' : '2025-03-01', 
    'search_date' : 'period'
}

query_params = {
    'from_date' : '2025-01-01', 
    'to_date' : '2025-03-01', 
    'search_date' : 'period'
}

user_id = 1

if __name__ == '__main__' : 
    uri = f'/users/{user_id}/workout_sessions' 
    api = UserWorkoutSessionsAPI(uri)

    api.post(data)

    api.get({
        'from_date' : '2025-01-01', 
        'to_date' : '2025-03-01', 
        'search_date' : 'period'
    })

    api.get({
         'date' : '2025.02-11' 
    })    