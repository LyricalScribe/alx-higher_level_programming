#!/usr/bin/python3
""" script which takes in a url and email
as a paramter and return the email """


if __name__ == '__main__':
    from urllib import request, parse
    from sys import argv

    url = argv[1]
    email = argv[2]

    params = parse.urlencode({'email': email}).encode('utf-8')
    with request.urlopen(url, data=params) as response:
        content = response.read().decode('utf-8')
        print(content)
