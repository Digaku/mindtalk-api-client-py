#
# Copyright (C) 2011 Ansvia
# License: 		MIT
# Summary: 		This example use anonymous API class only.
#

import sys
import urllib
import datetime
import simplejson as json

API_BASEURL = 'http://api.mindtalk.com/v1'

# this is my example client APi key
# you can use your own key
# Please create client from http://auth.mindtalk.com/ui/client/create
# to get an api key
API_KEY = 'f88faaa11fe119f502b760a0f64a1886baf04788'

class MtClient(object):
	def __init__(self, api_key):
		self.api_key = api_key
	
	def request(self, endpoint, params=None):
		if params:
			add_params = urllib.urlencode(params)
			url = '%s/%s?api_key=%s&%s' % (API_BASEURL, endpoint, self.api_key, add_params)
		else:
			url = '%s/%s?api_key=%s' % (API_BASEURL, endpoint, self.api_key)
		u = urllib.urlopen(url)
		rv = u.read()
		u.close()
		return rv

## Our entry point

if __name__ == '__main__':
	client = MtClient(API_KEY)

	if len(sys.argv) < 2:
		print "Invalid arguments"
		print "Usage: "
		print "		  python minds.py [USER-NAME]"
		print ""
		print "Example:"
		print "			 python minds.py giringnidji99"
		sys.exit(1)
		
	user_name = sys.argv[1]

	rv = client.request('/user/posts', {'name':user_name})
	rv = json.loads(rv)
	if rv.get('error'):
		print "Error: " + rv['error']
		sys.exit(1)
	
	for p in rv['result']:
		print "Writer: %s (%s)" % (p['creator']['name'],p['creator']['full_name'])
		print "Minds: " + p['message'].encode('utf-8')[:512] # strip only show max 512 characters
		print ""
		print "When: %s" % str(datetime.datetime.fromtimestamp(p['creation_time']))
		print "--------------------------------------------------"
	
	


