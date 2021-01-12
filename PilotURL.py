"""
PilotURL.py is in charge of initializing the various URL classes and retrieving
the links/downloading files that Pilot.py requests. PilotURL.py can only recieve
information from Pilot.py and cannot access any attributes/methods of Pilot.py
unless it is passed through

- Rod (01/11/2021)
"""

import requests
from bs4 import BeautifulSoup

class MainURL(object):
    """
    This class is meant to be used as a base for current and future subclasses.
    Since PilotsProgram will require many files/resources from the internet,
    having just one main class work all the necessary operations of the program
    is not feasable.

    Since this is a helper module, all attributes are hidden.
    """

    # Hidden Attributes

    # Attribute _ICAO: the ICAO code for the user's airport
    # Invariant: _ICAO is a string that is a valid ICAO airport code

    # Attribute _IATA: the IATA code for the user's airport
    # Invariant: _IATA is a string that is a valid IATA airport code


    # Getters/Setters GO HERE
    def getICAO(self):
        """
        Returns self._ICAO (the ICAO airport code)
        """
        return self._ICAO


    def getIATA(self):
        """
        Returns self._IATA (the IATA airport code)
        """
        return self._IATA


    def __init__(self, icao, iata):
        """
        When called, the initializer creates the attribute necessary for the
        class (in this case, it is '_ICAO'). No preconditions need to be enforced
        as Pilot.py verifies that code (the airport code the user has inputted)
        corresponds to ICAO format.
        """
        self._ICAO = icao
        self._IATA = iata


class adURL(MainURL): # Inherits from MainURL class
    """
    This class is responsible for handling the process behind retrieving the
    airport diagram of the airport the user has inputted.

    This class inherits its initializer from MainURL, adds the _payload
    attribute and (currently) contains the methods needed to retrieve (and
    download, but that's a work in progress) the airport diagram from the
    FAA's website
    """

    # Hidden Attributes

    # Attribute _payload: the information needed to submit a form to the FAA
    # diagram system and retrieve the airport diagram
    # Invariant: _payload is a dictionary that contains the correct information
    # to make a POST request

    # Getters/Setters GO HERE
    def getPayload(self):
        """
        Returns self._payload, a dictionary that contains infomration used
        when making a POST request to the FAA website for airport diagrams.
        """
        return self._payload


    def __init__(self, icao, iata):
        """
        When called, this initializer uses super to call the initializer for
        MainURL. Afterwards, it creates the attribute _payload which is a
        dictionary used for the POST request to the FAA website
        """
        super().__init__(icao, iata)
        self._payload = {
            'ident': self.getICAO(),
            #state: # Commented out sections need a look at later.
            #airport:
            #'ver': '2013',
            #'eff': '12-03-2020',
            #'end': '12-31-2020',
            'diagrams': '1', # For future improvements, changing the diagram
            #number changes the diagram given by the URL
            'cycle': '2013',
        }


    def adRetrieve(self):
        """
        When called, this procedure takes the attributes _ICAO and _IATA and uses it to
        retrieve the corresponding airport diagram from the FAA's website
        """
        temp = requests.session()
        response = temp.post('https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dtpp/search/results/',
        data=self.getPayload()) # SHORTEN !!!
        cleanResponse = response.text

        soup = BeautifulSoup(cleanResponse, 'lxml')

        result = ''
        value = True
        for link in soup.find_all('a'):
            p = str(link.get('href'))
            if p.find(self.getIATA()) > 0 and p.find('http://aeronav.faa.gov/') >= 0 and value:
                result = p
        #        print(result)
                value = False

        final = requests.get(str(result))

        fileName = str(self.getICAO()) + 'diagram.pdf'

        with open(fileName, 'wb') as f:
            f.write(final.content)


class metarsURL(MainURL):
    """
    This class is responsible for fetching the metars that pilots need prior
    to flying. This class currently (only contain methods) and uses GET
    requests to call to a website that contains metar information and parses
    it using BeautifulSoup.
    """
    # Hidden Attributes Go Here

    def metarsRetrieve(self):
        """
        When called, this procedure takes the attributes _ICAO and/or _IATA to
        retrive the corresponding metars information from a website on the
        internet.
        """
        temp = requests.session()
        link = 'https://www.aviationweather.gov/metar/data?ids=' + str(self.getICAO()) +'&format=raw&date=&hours=0'
        response = temp.get(link)
        cleanResponse = response.text

        soup = BeautifulSoup(cleanResponse, 'lxml')

        result = ''
        value = True
        for info in soup.find_all('code'):
            test = str(info)
            if test.find(self.getICAO()) >= 0 and value:
                result = info.text
                value = False

        self.metarsText = result
        print(self.metarsText)
