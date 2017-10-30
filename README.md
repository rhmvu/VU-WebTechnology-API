# VU WebTechnology: HTML webpage + RESTful API #
During the course Web Technology we (Kostas Moumtzakis and I) had to build a webpage. The webpage had to communicate with a RESTful API.  
The RESTful API was (in our setup) hosted on the same machine as were the webpage was opened. The API is built using the bottle framework, running on Python 2.7.  
The API will create a file named "inventory.db" on the server where the input will be stored.

## How to get started ##

### Locations ###
The client webpage is located in the "/HTML/main/" folder.  
The API's documentation is found in the "/HTML/Documentation API.html" file.  
The API framework is located in the "/Server/" folder.

### Serving the API ###
To run the API on your localhost you will need Python 2.7.  
When installed run the following command from the root of this repo:  
`python /Server/Server.py `  
