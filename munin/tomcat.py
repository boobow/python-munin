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

    def _get_status(self):
        req_params = urllib.urlencode({'XML': 'true'})
        req_url = "%s?%s" % (self._url, req_params)

        resp = urllib2.urlopen(req_url)
        return resp.read()

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