#!/usr/bin/env python

from munin.jboss import MuninJBossPlugin

class MuninJBossMemoryPlugin(MuninJBossPlugin):
    
    title = 'JBoss Memory'
    vlabel = 'Memory'
    args = '--base 1000'

    fields = (
        ('max', dict(
            label = 'Total memory',
            type = 'GAUGE',
            draw = 'LINE2',
            min = '0',
        )),
        ('total', dict(
            label = 'Used memory',
            type = 'GAUGE',
            draw = 'LINE2',
            min = '0',
        )),
        ('free', dict(
            label = 'Free memory',
            type = 'GAUGE',
            draw = 'LINE2',
            min = '0',
        ))
    )
    
    def execute(self):
        stats = self.get_memory_stats()
        
        return dict(
            total = stats['max'],
            used = stats['total'],
            free = stats['free'],
        )
        
if __name__ == '__main__':
    MuninJBossMemoryPlugin().run()