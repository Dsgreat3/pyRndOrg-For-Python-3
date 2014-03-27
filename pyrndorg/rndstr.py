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
# === Usage <rndstr.py> ===
# Gets a number of random strings
#
# get(num, len, [[dig], [ua], [la], [uni]])
# num : Number of strings to get (required)
# len : Length of strings (required)
# dig : Digits allowed (1: yes / 0: no) (default: 0)
# ua  : Uppercase characters allowed (1: yes / 0: no) (default: 0)
# la  : lowercase characters allowed (1: yes / 0: no) (default: 1)
# uni : Whether the strings picked should be unique (1: yes / 0: no) (default: 0)
#
# For more information on usage and restrictions, 
# read the README file or http://www.random.org/clients/http/ 

import urllib
from string import Template

def get(num, len, dig=0, ua=0, la=1, uni=0):
	sdig = "on" if dig else "off"
	sua = "on" if ua else "off"
	sla = "on" if la else "off"
	suni = "on" if uni else "off"
	
	# Check quota	
	quotachk = urllib.urlopen("http://www.random.org/quota/?format=plain")
	if int(quotachk.read()) <= 0:
		return ("ERROR: Your Quota limit is below zero. Try again later\n"
			    "ERROR: or buy new random numbers @ random.org")

	# Get and return strings
	urltmp = Template("http://www.random.org/strings/?"
					  "num=${num}&len=${len}&digits=${sdig}&upperalpha=${sua}&"
					  "loweralpha=${sla}&unique=${suni}&format=plain&rnd=new")
	url = urltmp.substitute(num=num, len=len, sdig=sdig, sua=sua, sla=sla, suni=suni)
	
	dice = urllib.urlopen(url)
	strresult = dice.read()
	numlist = strresult.split("\n")
	numlist.pop()

	return numlist		
