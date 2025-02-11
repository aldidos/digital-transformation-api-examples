import sys
sys.path.append('.')

from base_uri import BaseAPI

class ExerciseLibraryAPI(BaseAPI) : 

    def __init__(self, uri) : 
        super().__init__(uri)

if __name__ == '__main__' : 
    uri = f'/exercise_libraries' 
    api = ExerciseLibraryAPI(uri)

    api.get()