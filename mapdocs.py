from operator import itemgetter
import urllib, urllib2
import json


BING_IMAGE_SEARCH_URL='http://api.search.live.net/json.aspx?Appid=FC73C29F84C524731765F16BB16867A6F45A4FFF&sources=image&query='
coverflow_html = '''<div='col'><h3>%s (%s)</h3><div class="ft"><img src="%s" alt="%s" style="height:150px;weight:150px;align:middle;"/><p>%s</p></div></div>

'''



mapping = {}
for line in open('data/names').xreadlines():
	name = line.split(',')[1]
	filename = line.split(',')[0]
	try:
		if filename not in mapping[name]:
			mapping[name].append(filename)
	except:
		mapping[name] = [filename]

count_list = {}
for name,files in mapping.items():
	count_list[name]=len(files)
		
#for name,count  in count_list:
main_list = sorted(count_list, key=itemgetter(1),reverse=True)


html_output = open('coverflow.html','w')
for name in main_list:
        sname = name.replace('\n','').strip()
        links =""
        try:
                count = len(mapping[name])
        
                for file in mapping[name]:
                        links += "<a href=\'http://dl.dropbox.com/u/18146922/cables/%s\'>%s</a>, " % (file,file)
                
        
                url = BING_IMAGE_SEARCH_URL + sname
                results = json.load(urllib.urlopen(url))
                try:
                        feeling_lucky = results["SearchResponse"]["Image"]["Results"][0]["Thumbnail"]["Url"]
                except:
                        pass
                s = coverflow_html % (sname,count,feeling_lucky,sname,links)
                html_output.write(s)
        except:
                pass

