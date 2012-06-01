import os
import urllib2, urllib
from xml.etree import ElementTree
from munin import MuninPlugin

class MuninTomcatPlugin(MuninPlugin):
    
    _status_xml = None
    category = 'Tomcat'
    
    def __init__(self):
        super(MuninPlugin, self).__init__()
        self._url = os.environ.get('TOMCAT_STATUS_URL') or "http://localhost:8080/manager/status"
        self._user = os.environ.get('TOMCAT_USERNAME') or None
        self._password = os.environ.get('TOMCAT_PASSWORD') or None
        self.category = os.environ.get('TOMCAT_CATEGORY') or self.category
    
    def _get_status(self):
        if self._user is not None and self._password is not None:
            realm = urllib2.HTTPPasswordMgrWithDefaultRealm()
            realm.add_password(None, self._url, self._user, self._password)
            handler = urllib2.HTTPBasicAuthHandler(realm)
            opener = urllib2.build_opener(handler)
        else:
            opener = urllib2.build_opener()
        
        params = urllib.urlencode({'XML': 'true'})
        full_url = "%s?%s" % (self._url, params)

        response = opener.open(full_url)
        return response.read()

    def _get_status_xml(self):
        return ElementTree.XML(self._get_status())
            
    def load(self):
        self._status_xml = self._get_status_xml()

    def get_memory_stats(self):
        if self._status_xml is None:
            self.load()
        
        memory_node = self._status_xml.find('jvm/memory')
        stats = {}
        if memory_node is not None:
            for (k, v) in memory_node.items():
                stats[k] = int(v)
        return stats