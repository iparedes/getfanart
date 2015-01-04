# Obtiene el seriesid de thetvdb.com (titulo-con-espacios)

import sys
import urllib2
from xml.dom import minidom
from urllib2 import Request, urlopen, URLError

fanurl='http://thetvdb.com/api/GetSeries.php?seriesname='

with open('series.txt','r') as fp:
	for line in fp:
		a=line.replace('-','+')
		a=a[:-1]
		url = fanurl + a
		response = urllib2.urlopen(url)
		xmldoc=minidom.parse(response)
		aux=xmldoc.getElementsByTagName("seriesid")
		try:
			ide=aux[0].firstChild.data
			print("%s\t%s" % (a,ide))
		except:
			print("%s\t%s" %(a,'Not found'))