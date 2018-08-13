#!/usr/bin/env python

import httplib, json, urllib, urllib2

# device: IP address
# Gets the session ID to
c = httplib.HTTPSConnection(device)
c.request("GET", "/services/rest/V2/?method=authenticate&amp;username=admin&amp;password=a10&amp;format=json")
response = c.getresponse()
data = json.loads(response.read())
session_id = data['session_id']
print("Session Created. Session ID:", session_id)

# Construct HTTP URL and Post Body
# post_body = open(commandFile, ‘r’).read()
post_body = "show run"

url = "https://" + device + "/services/rest/V2/?&amp;session_id=" + session_id + "&amp;format=json&amp;method=cli.show_info"
print("URL Created. URL: " + url + " body: " + post_body)

# Making request
req = urllib2.Request(url, post_body)
rsp = urllib2.urlopen(req)
content = rsp.read()
print("Result: ", content)
