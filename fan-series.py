# descarga backgrounds de series (title \t tvdbid) de fanart.tv

import re
import json
import urllib
import urllib2
from urllib2 import Request, urlopen, URLError

url='http://webservice.fanart.tv/v3/tv/'


with open('series-id.txt','r') as fp:
	for line in fp:
		match=re.search("(.+)\t(.+)$",line)
		
		ide=match.group(2)
		peli=match.group(1)
		print 'Dwnldng bckgrnd fr:',peli
		fanurl=url+ide+'?api_key='+'fanart.tv-API-KEY'
		try:
			
			request = Request(fanurl)
			response=json.load(urllib2.urlopen(request))
			try:
				bg=response['showbackground']
				cont=0
				for i in bg:
					u=i['url']
					filename=peli
					if (cont>0):
						filename=filename+" "+str(cont)
					filename=filename+".jpg"
					cont=cont+1
					if cont==3:
						break
					urllib.urlretrieve(u,filename=filename)
			except:
				print "No art for "+peli

		except URLError, e:
			print 'Nope. Got an error code:', e
