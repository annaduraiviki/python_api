import requests
import logging
import urllib3
import urllib2
import urllib3.contrib.pyopenssl
import webbrowser


urllib3.disable_warnings()
logging.getLogger("urllib3").setLevel(logging.WARNING)
class check():
    r = requests.get('https://github.com/timeline.json')
    print r
    print r.status_code,'status_code'
    print r.encoding,'encoding'
    r = requests.post('http://www.google.com', data = {'key':'value'})
    print r,'R'
    print r.url,'Url'
    print r.text,"Text"
    print r.status_code == requests.codes
    print r.history ,"History"

    response = urllib2.urlopen('http://python.org/')
    html = response.read()
    webbrowser.open('http://google.com')
    print " This Py file opens web site in a browser "
