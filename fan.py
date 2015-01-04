# descarga backgrounds de peliculas (title \t year \t imdbid) de fanart.tv

import re
import json
import urllib
import urllib2
from urllib2 import Request, urlopen, URLError


headers={'api-key':'fanart.tv-API-KEY','client-key':'fanart.tv-CLIENT-KEY'}
url='http://webservice.fanart.tv/v3/movies/'


with open('movies.txt','r') as fp:
	for line in fp:
		match=re.search("(.+)\t(.+)\t(.+)$",line)
		
		ide=match.group(3)
		year=match.group(2)
		peli=match.group(1)
		print 'Dwnldng bckgrnd fr:',peli
		fanurl=url+ide
		try:
			request = Request(fanurl,headers=headers)
			response=json.load(urllib2.urlopen(request))
			try:
				bg=response['moviebackground']
				cont=0
				for i in bg:
					u=i['url']
					filename=peli+" ("+year+")"
					if (cont>0):
						filename=filename+" "+str(cont)
					filename=filename+".jpg"
					cont=cont+1
					urllib.urlretrieve(u,filename=filename)
			except:
				print "No art for "+peli

		except URLError, e:
			print 'Nope. Got an error code:', e
