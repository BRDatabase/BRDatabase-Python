"""
    There is no requirement for anyone from a certain group of countries to access brdatabase.

    The old site was hit by many hacking attempts, falling broadly into the following 2 categories:

        1) Denial of Service (DoS) attacks, flooding the database with requests
        2) hacking attempts, trying to access the database by using SQL injection through the query form

    Although these attacks came from a number of countries, by far the most prevalent were attacks from
    China and the far-east (though not Japan), and most, if not all Eastern Bloc countries. As the database holds
    information pertaining to British locomotives exclusively, I don't see any harm in blocking these countries
    en-masse. To be honest, the only countries likely to want access are the United Kingdom and ex-pats in Australia,
    New Zealand, USA, Canada and perhaps Brits who have moved across the Channel and taken up residence in
    France, Italy, Germany, Spain and Scandinavia.

    So, this middleware inspects the IP address and determines the country of origin and either allows access based
    on the above criteria, or rejects it with a polite message :)

"""

import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity

blocked_countries = ["China", "Russia", "Ukraine", "Moldova", "Belarus", "Romania", "Bulgaria", "Slovenia", "Croatia", "Serbia", "Kosovo"]
allowed_countries = []

class CountryDenyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response

    def is_country_blocked(ip_address):
        location = DbIpCity.get(ip_address)

        if location.country in blocked_countries:
            return True
        else:
            return False

    def is_ip_override_allowed(ip_address):
        if ip_address in allowed_ip_addresses:
            return True
        else:
            return False
