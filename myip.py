# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 21:42 2023

@author: manuel soto
@email: manugram.dev@gmail.com
"""

import json
from urllib.request import urlopen



API_URL = "https://api.myip.com"




class Myip():
    """
     Main class to get API json...
    """


    def __init__(self):

        self.ip_info = self.get_api_response(API_URL)

        self.ip = self.ip_info.get('ip')
        self.country = self.ip_info.get('country')
        self.country_code = self.ip_info.get('cc')


        return


    def get_api_response(self, api_url: str) -> dict:
        """
        This method get the json from the web and returns it as a python dictionary...
         Recives only one parameter wich is the api url hard coded as API_URL constant...
        """

        with urlopen(api_url) as w:
            myip_response = json.loads(w.read())

        return myip_response



def get_myip_info() -> dict:

 
    with urlopen(API_URL) as w:
        myip_info = json.loads(w.read())

    return myip_info



def main():
    """
     This main() function is used when calling from the CLI...
    """

    print()

    d = get_myip_info()
    for i in d.keys():
        if i == 'country':
            print(i.upper(), ':', d.get(i))
        else:
            print(i.upper(), '\t:', d.get(i))

    return



if __name__ == '__main__':
    main()