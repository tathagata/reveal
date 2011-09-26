import urllib, urllib2
import json


BING_IMAGE_SEARCH_URL='http://api.search.live.net/json.aspx?Appid=FC73C29F84C524731765F16BB16867A6F45A4FFF&sources=image&query='
coverflow_html = '''<div class="ft"><img src="%s" alt="%s" height=160 width=160 /><p>%s %s</p></div>
'''

html_output = open('coverflow.html','w')

for line in open('sig_names').xreadlines(): 
	name = line.split(",")[0].strip()
	count = line.split(",")[1].strip()
	url = BING_IMAGE_SEARCH_URL + name
	results = json.load(urllib.urlopen(url))
	feeling_lucky = results["SearchResponse"]["Image"]["Results"][0]["Thumbnail"]["Url"]
	s= coverflow_html % (feeling_lucky,name,name,count)
	html_output.write(s)
	

