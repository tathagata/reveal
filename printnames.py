def write_named_entity(f,w):
	p = open(w,'w')
	for line in open(f).xreadlines():
		filename = line.split(':')[0]
    		name = line.split(':')[1]
		name = name.replace("[LOC ","").replace("[PER ","").replace("[MISC ","").replace("[ORGS ","").replace("]", "")
		s= filename + "," + name
		p.write(s)


if __name__ == "__main__":
	write_named_entity("/tmp/locos","data/locos") 
	write_named_entity("/tmp/names","data/names")
	write_named_entity("/tmp/orgs","data/orgs") 
	write_named_entity("/tmp/miscs","data/miscs") 
