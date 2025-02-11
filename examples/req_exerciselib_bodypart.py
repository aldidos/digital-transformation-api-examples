import sys
sys.path.append('.')

from base_uri import BaseAPI

class ExerciseLibraryBodypartAPI(BaseAPI) : 

    def __init__(self, uri) : 
        super().__init__(uri)

if __name__ == '__main__' : 
    uri = f'/exerciselib_bodyparts' 
    api = ExerciseLibraryBodypartAPI(uri)
    api.get()

