# Obtiene el imdbID de peliculas (titulo-con-espacios year)

import sys
import urllib2
import re
import json
from urllib2 import Request, urlopen, URLError

fanurl='http://webservice.fanart.tv/v3/movies/'

with open('moviesnotfound.txt','r') as fp:
	for line in fp:
		a=line.replace('-','+')
		match=re.search("(.+)(\d\d\d\d)$",a)
		peli=match.group(1)
		peli=peli[:-1]
		year=match.group(2)
		url = "http://www.imdbapi.com/?t=" + peli + "&y="+year
		request = urllib2.Request(url)
		response = json.load(urllib2.urlopen(request))
		try:
			id=response['imdbID']
		except:
			id="Not found"
		print("%s\t%s\t%s" % (peli,year,id))
		
