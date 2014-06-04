#!/usr/bin/env python
import sys, getopt
import requests

def main(argv):
	url = 'http://data.developers.do/api/v1/provincias'
	id = ''
	try:
		opts, args =  getopt.getopt(argv,'id:',['id='])
	except getopt.GetoptError:
		print 'main.py --id <id>'
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-i","--id"):
			id = arg
			if not id:
				print 'main.py --id <id>'
				sys.exit(3)
			if not id.isdigit():
				print 'id have to be a digit'
				sys.exit(4)
			if (int(id) < 1) or (int(id) > 32):
				print 'id have to be between 1 and 32'
				sys.exit(5)
	if not id:
		print 'main.py --id <id>'
		sys.exit(6)

	url = url+'/'+id+'.json'
	response = requests.get(url);
	json = response.json()
	print '\nnombre: {}\n'.format(json["nombre"].encode('utf-8'))

if __name__ == '__main__':
	main(sys.argv[1:])