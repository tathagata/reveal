import re
import os

root = '/var/www/cable/cable'

def extract_cables(root):
	for root, dirnames, filenames in os.walk(root):
		for filename in filenames:
			absfn = os.path.join(root,filename)
			cable_text = open(absfn).readlines()[1204]
			clear_cable_text = cable_text.replace('&#x000A;','\n')
			
			outfn = '/tmp/cables/'+filename.replace('.html','.txt')	
			print outfn
			fpo = open(outfn,'wb')
			fpo.write(clear_cable_text)
			fpo.close()


def named_entity_extraction(root, tagger_path, tagged_file_path):
	for root, dirnames, filenames in os.walk(root):
		for filename in filenames:
			inputfn = os.path.join(root,filename)
			tagged_output_fn = os.path.join(tagged_file_path,filename)
			
			cmdString = 'java -cp '+ tagger_path + 'LBJ2.jar:LBJ2Library.jar:bin -Xmx2000m LbjTagger.NerTagger -annotate ' + inputfn + ' ' + tagged_output_fn + ' true Config/allFeaturesBigTrainingSet.config'
			print cmdString
			try:
				os.system(cmdString)
				break				 
			except:
				print "Something fucked up"
	

if __name__ == "__main__":
#	extract_cables('/var/www/cable/cable')	
	named_entity_extraction('/tmp/cables', '/home/tathagata/cs582/tools/LbjNerTagger1.11.release/','/tmp/tagged')		
