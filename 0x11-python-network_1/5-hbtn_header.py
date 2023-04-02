#!/usr/bin/python3
'''fetches data from a url using requests'''

if __name__ == '__main__':
    import requests
    import sys

    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
