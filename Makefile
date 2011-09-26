all: annotate dump

clean:	
	rm -f data/*
annotate:
	./annotate
dump:
	./dump
