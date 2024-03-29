
#! /usr/bin/python3

import os
import sys

##Virtualenv Settings
#activate_this = '/usr/share/openstack_horizon_reg_service/venv/bin/activate_this.py'
#execfile(activate_this, dict(__file__=activate_this))


##Replace the standard out
sys.stdout = sys.stderr

##Add this file path to sys.path in order to import settings
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..'))

##Add this file path to sys.path in order to import app
sys.path.append('/usr/share/FlaskApp/')

##Create appilcation for our app
from app import app as application

