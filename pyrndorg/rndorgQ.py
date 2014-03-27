# pyRndOrg v0.1
# random.org Python API
#
# Copyright 2009 Felix Rauch <toastwaffel(at)gmail.com>
# released under the GNU Lesser General Public License 3
# 	http://www.gnu.org/licenses/lgpl.html
#
# === Brief introduction ===
# The pyRndOrg library consists of four modules:
#	rndint  -  Get a number of integers
#	rndseq  -  Get a sequence of integers
#	rndstr  -  Get a number of strings
#	rndorgQ -  Get your current quota
# You can import either the whole package or only the needed
# modules. Every module has one public function get([args]),
# whose possible arguments are explained in the README file
# aswell as in each module.
#
# === Usage <rndorgQ.py> ===
# Gets your current quota
#
# get()
#
# For more information on usage and restrictions, 
# read the README file or http://www.random.org/clients/http/

import urllib

def get():
	quotachk = urllib.urlopen("http://www.random.org/quota/?format=plain")
	return int(quotachk.read())
