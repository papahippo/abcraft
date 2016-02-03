#!/usr/bin/python
"""
Copyright 2015 Hippos Technical Systems BV.

@author: larry
"""
from __future__ import print_function
import musicraft
print ("imported musicraft package from", musicraft.__file__)
musicraft.abcraft.external.Abcm2svg.exe = '/usr/local/bin/abcm2ps'
musicraft.abcraft.external.Abc2midi.exe = '/usr/local/bin/abc2midi'
musicraft.abcraft.external.Abc2midi.reMsg = r'.*in\s+line-char\s(\d+)\-(\d+).*'

#print ("running musicraft.main")
#musicraft.abcraft.main()
print ("running raft.main")
musicraft.raft.main()
