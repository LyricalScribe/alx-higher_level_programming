#!/usr/bin/python3
"""script tp fetch url from request"""

if __name__ == "__main__":
	from urllib import request
	from sys import argv

	url = argv[1]
	with request.urlopen(url) as response:
		request_id = response.getheader('X-Request-Id')
		print(request_id)
