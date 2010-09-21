#!/usr/bin/env python

#         __________________________
#         |____C_O_P_Y_R_I_G_H_T___|
#         |                        |
#         |  (c) NIWA, 2008-2010   |
#         | Contact: Hilary Oliver |
#         |  h.oliver@niwa.co.nz   |
#         |    +64-4-386 0461      |
#         |________________________|

import Pyro.core, Pyro.naming, Pyro.errors
import os,sys,socket

# PYRO NAMESERVER GROUP AND OBJECT NAME MUST MATCH CYLCLOCKD.
groupname = ':cylclockd'
name = 'broker'

class lockserver:
    def __init__( self, pns_host=None ):
        # Pyro exceptions should be handled at a higher level, as we don't
        # necessarily want to abort if the lockserver cannot be contacted.
        self.server = Pyro.core.getProxyForURI('PYRONAME://' + pns_host + '/' + groupname + '.' + name)
        
    def get( self ):
        return self.server

    def dump( self ):
        return self.server.dump()

    def clear( self ):
        return self.server.clear()

    def get_filenames( self ):
        return self.server.get_filenames()
