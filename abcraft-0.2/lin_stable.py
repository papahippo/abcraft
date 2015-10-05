#!/usr/bin/python
"""
Copyright 2015 Hippos Technical Systems BV.

@author: larry
"""
from __future__ import print_function
import abcraft
print ("imported abcraft package from", abcraft.__file__)

# The ugly use of a 'fudge factor' makes the "click-on-note to show ABC source
# cursor" work. I'm still looking for a sounder algorithm for this!
#
abcraft.score.SvgDigest.gScaleMultiplier = 1.25

# Usually the stable version of abcm2ps (etc.) will be accessible as simply
# 'abcm2ps', so (e..g.) 'abcraft.external.Abcm2svg.exe' wil not need to be
# customized. Otherwise, uncomment (remove the '#') line below and edit
# the path as appropriate.
#
#abcraft.external.Abcm2svg.exe = '/home/larry/musicprogs/abcm2ps-7.8.14/abcm2ps'

abcraft.abcraft.main()
