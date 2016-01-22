# MachineHypermediaToolkit
Reference implementation and demonstration system for the machine hypermedia interface

Based on the Hypermedia Collection described in the IETF CoRE Interfaces draft 
https://datatracker.ietf.org/doc/draft-ietf-core-interfaces/

Following the article at
http://iot-datamodels.blogspot.com/2015/10/hypermedia-design-for-machine-interfaces.html

# Create a working directory and install the tools with the following:

git clone https://github.com/mjkoster/MachineHypermediaToolkit 

cd MachineHypermedia Toolkit

### If you want to use virtualenv:

virtualenv --no-site-packages venv/ 

source venv/bin/activate

python setup.py develop

### Otherwise:

(sudo) python setup.py install

### Test using these 2 commands. Start a local instance of the server, then run the Resource Constructor self-test, which creates and inspects a set of resources on the server:

python MachineHypermediaToolkit/test/StartLocalServer.py

python MachineHypermediaToolkit/model/ResourceConstructor.py