"""
NOTE: This project is a work in progress and it is likely that this file will
not be main controller in future iterations.

Pilot.py is (currently) in charge of starting the program, initializing the
PilotInfo class, and handing control over to the control method. This class
can access the PilotURL module.

- Rod
"""

# Remember to insert copyright info before uploading to Github

import json
import requests
from PilotURL import *

class PilotInfo(object):

    """
    This is the program that will control the entire pilot information. Separate
    subclasses may have to be made in order to faciliate the entire program, but
    this program will still retain higher authority over all other (possible)
    classes and subclasses.

    Attribute ICAO:
    Invariant:

    Attribute IATA:
    Invariant:
    """

    # Hidden Attributes GO HERE

    # Attribute _file:
    # Invariant:

    # Attribute _adURL:
    # Invariant:

    # Setters and Getters GO HERE

    # Explicit Methods and Initializer GO HERE
    def __init__(self, value):
        """
        Initializes the program and creates the necessary attributes needed
        for the class to operate as expected.
        """
        self._fileHelper()

        self.ICAO = value
        if self.ICAO in self._file:
            self.IATA = self._file[self.ICAO]['iata'] # Getter probably needed here
        #    print(self._file[self.ICAO])
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
        # My attempt to get the airport diagram
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
