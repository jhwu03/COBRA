#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/cobra/")
sys.path.insert(0,"/var/www/cobra/cobra/")

import logging
logging.basicConfig(stream=sys.stderr)

from cobra import app as application

