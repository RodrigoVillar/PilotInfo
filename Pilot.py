"""
Note: Additions may be made to this project (e.g. adding a GUI interface).
However, I am leaving the project as it is in order to learn more about
the world of Python and its various frameworks.

Pilot.py is the file in charge when it comes to PilotInfo. When run as
a script, this file creates an instance of the PilotInfo class and
eventually calls to PilotURL.py to get the information requried for
this program.

- Rod (01/11/2021)
"""

import json
import requests
from PilotURL import *

class PilotInfo(object):

    """
    This is the program that will control the entire pilot information. Separate
    subclasses may have to be made in order to faciliate the entire program, but
    this program will still retain higher authority over all other (possible)
    classes and subclasses.

    Attribute ICAO: the ICAO code for the user's airport
    Invariant: ICAO is a string that is a valid ICAO airport code

    Attribute IATA: the IATA code for the user's airport
    Invariant: IATA is a string that is a valid ICAO airport code
    """

    # Hidden Attributes GO HERE

    # Attribute _file: the JSON containing the necessary information to
    # run this program
    # Invariant: _file is an immutable dictionary containing airport
    # information

    # Attribute _adURL: the adURL object containing the PDF link of
    # the airport diagram
    # Invariant: _adURL is an immutable adURL object
    
    # Attribute _metarsURL: the metarsURL object containing the most
    # recent metars for the airport
    # Invariant: _metarsURL is an immutable metarsURL object


    # Explicit Methods and Initializer GO HERE
    def __init__(self, value):
        """
        Initializes the program and creates the necessary attributes needed
        for the class to operate as expected.
        
        Attribute value: value is the text that the user imports when
        first running this program
        
        Precondition: value is a string and is also a valid ICAO airport
        code
        """
        assert type(value) == str, 'Precondition Violation'
        assert value in self._file, 'Precondition Violation'
        
        self._fileHelper()

        self.ICAO = value
        if self.ICAO in self._file:
            self.IATA = self._file[self.ICAO]['iata'] 
            #print(self._file[self.ICAO])
            self._adURL = adURL(self.ICAO, self.IATA)
            self._metarsURL = metarsURL(self.ICAO, self.IATA)
            self.control()
        else:
            print('The code inputted is not a valid ICAO airport code')


    def control(self):
        """
        Once the initializer is complete, this method is called and will
        control the program for the rest of the user session
        """
        # Prints out static airport info
        for row in self._file[self.ICAO]:
            key = row
            value = self._file[self.ICAO][row]
            print(str(key) + ' : ' + str(value))
        self._adURL.adRetrieve()
        self._metarsURL.metarsRetrieve()


    # Hidden Methods GO HERE
    def _fileHelper(self):
        """
        Helper method that opens the file 'airports.json' and converts it from
        a JSON file to a readable Python dictionary, which is stored in _file,
        a hidden attribute in this class.

        This method is meant to be hidden and only be used by the PilotInfo
        initializer (this is subject to change)
        """
        file = open('airports.json')
        fileData = file.read()
        self._file = json.loads(fileData)
        file.close()


# Pilot.py is meant to be run as a script only when debugging

if __name__ == "__main__":
    x = input('Type in the ICAO code of the airport you want info\
 from in capital letters: ')
    PilotInfo(x)
