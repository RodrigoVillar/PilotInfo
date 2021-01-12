# PilotInfo

This is my first solo Python project, so please excuse me for any amateur mistakes!

PilotInfo is a basic tool meant to help pilots get the neccessary information for their desired airport. Once this program recieves the pilot's desired airport code, it returns the airport's static (as in, information that never changes over time) information along with the current METARs for the airport. As well, PilotInfo downloads the airport's runway diagram to the directory where PilotInfo is stored.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
### Prerequisites

What things you need to install the software and how to install them

```
Python 3.8.3, BeautifulSoup
```

### Installing

To run the program, open up a command window to the directory where PilotInfo is stored and type the following:
Say what the step will be

```
python Pilot.py
```

Once the program runs, it will show the following:

```
Type in the ICAO code of the airport you want info from in capital letters: 
```

From here, type the ICAO code for your desired airport in all caps and without any spaces. Once you enter the ICAO code, the following will appear (this example utilizes the aiport code KJFK)


```
icao : KJFK
iata : JFK
name : John F Kennedy International Airport
city : New York
state : New-York
country : US
elevation : 13
lat : 40.63980103
lon : -73.77890015
tz : America/New_York
http://aeronav.faa.gov/d-tpp/2013/00610ad.pdf#nameddest=(JFK)
KJFK 120051Z 25005KT 10SM FEW085 BKN250 01/M03 A3022 RMK AO2 SLP233 T00061033
```

## Built With

* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - The web framework used to make/send PULL requests and GET requests.

## Contributing

Just send a pull request!

## Versioning

Version 1.0 is the current and only version at the moment.

## Authors

* **Rodrigo Villar**

## License

See the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Huge thanks to user mwgg for providing the airport dictionary necessary for this program to run!
