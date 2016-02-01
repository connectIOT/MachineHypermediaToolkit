# MachineHypermediaToolkit
Reference implementation and demonstration system for the machine hypermedia interface

Based on the Hypermedia Collection described in the IETF CoRE Interfaces draft 
https://datatracker.ietf.org/doc/draft-ietf-core-interfaces/

Following the article at
http://iot-datamodels.blogspot.com/2015/10/hypermedia-design-for-machine-interfaces.html

### Create a working directory and install the tools with the following:

git clone https://github.com/connectIOT/MachineHypermediaToolkit 

cd MachineHypermedia Toolkit

### If you want to use virtualenv:

virtualenv --no-site-packages venv/ 

source venv/bin/activate

python setup.py develop

### Otherwise:

(sudo) python setup.py install

### Test using these 2 commands. Start a local instance of the server, then run the Resource Constructor self-test, which creates and inspects a set of resources on the server:

python MachineHypermediaToolkit/test/StartLocalServer.py

or to run the server in the background:

nohup python MachineHypermediaToolkit/test/StartLocalServer.py &

this test client creates a set of resources, reads them back. and exits:

python MachineHypermediaToolkit/model/ResourceConstructor.py