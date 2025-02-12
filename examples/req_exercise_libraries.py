'''
====================================================================================
API : /exercise_libraries
    Methods : 
        GET : 
            status code : 
                200 : OK
====================================================================================
'''

import sys
sys.path.append('.')

from base_uri import BaseAPI

def main() : 
    uri = f'/exercise_libraries' 
    api = BaseAPI(uri)

    api.get()

if __name__ == '__main__' : 
    main()