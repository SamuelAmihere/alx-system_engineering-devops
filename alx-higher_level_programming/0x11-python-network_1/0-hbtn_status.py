#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status
"""
from urllib import request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    with request.urlopen(url) as response:
        hbody = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(hbody)))
        print("\t- content: {}".format(hbody))
        print("\t- utf8 content: {}".format(hbody.decode("utf-8")))
