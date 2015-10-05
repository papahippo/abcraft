#!/usr/bin/python
"""
Copyright 2015 Hippos Technical Systems BV.

@author: larry
"""
from __future__ import print_function
import os
from PySide import QtCore, QtGui, QtSvg

_imported_via_us_ = QtCore, QtGui, QtSvg
#dbg_print = lambda *pp, **kw: None
# replace (or overrule in certain modules) above to show debug printout by...
dbg_print = print
# ... or use soemething more pythonically correct like the logging module!

def filenameFromUrl(url):
    path = str(url)
    print ('filenameFromUrl', url, path)
    return path
    #if not path.startswith(r"file://"):
    #    return None
    if os.name == 'nt':
        # On Windows platforms, a local path reads: file:///c:/...
        # and a UNC based path reads like: file://server/share
        if path.startswith(r"file:///"): # this is a local path
            path=path[8:]
        else: # this is a unc path
            path = path[5:]
    else:
        path = path[7:]
    #if not os.path.splitext(path)[1] == '.abc':
    #    return None
    #if not os.path.exists(path):
    #    return None
    return path

class Common:  # yes, shades of FORTRAN; sorry!
    timer = None
    stdBook = None
    abcm2ps = None
    abcm2svg = None
    abc2midi = None
    abc2abc = None
    printer = None
    abcEditor = None
    score = None
    abcraft = None
    snippets = {
        'V': ('V:', ' name="', '" sname="', '"\n',),    # new voice
        'Q': ('Q:1/4', ),                 # new tempo indication
        '12': ('[1 ', ' :| [2 ',),        # varied repeat ending coding
        'cr': ('!<! ', ' !<!)',),         # hairpin dynamic
        'dim': ('!>! ', ' !>!)',),        # hairpin dynamic
        'CR': ('"_cresc."',),
        'Cr': ('"^cresc."',),
        'MR': ('"_molto rit."',),
        'Mr': ('"^molto rit."',),
        'PR': ('"_poco rit."',),
        'Pr': ('"^poco rit."',),
        'SB': ('"_steady beat"',),
        'Sb': ('"^steady beat"',),
        'm': ('[M:', '2/', '4]',),       # mid-line time-sig change 
        'tt': ('!tenuto!',),
        'tp': ('!teepee!',),
        'ac': ('!>!',),                  # accent; '><TAB>' also works
        'ro': ('!///!',),                # roll/roffel; '///<TAB>' also works
        'st': ('!dot!',),                # staccato; 'dot<TAB>' also works
        '.': ('!dot!',),                 # staccato; 'dot<TAB>' also works
        'gl': ('!-(!', '!-)!'),          # glissando
    }
    

class Printer(QtGui.QPrinter):
    pageSize = QtGui.QPrinter.A4
    
    def __init__(self):
        dbg_print ("Printer.__init__")
        QtGui.QPrinter.__init__(self, QtGui.QPrinter.HighResolution)
        self.setPageSize(self.pageSize)
        dbg_print ("!Printer.__init__")

def myQAction(menuText, shortcut=None, triggered=None, enabled=None,
              checkable=None, checked=None):
    """ Factory function to emulate older version of QAction.
    """
    action = QtGui.QAction(menuText, Common.abcraft)
    if shortcut:
        action.setShortcut(shortcut)
    if triggered:
        action.triggered.connect(triggered)
    if enabled is not None:
        action.setEnabled(enabled)
    if checkable is not None:
        action.setCheckable(checkable)
    if checked is not None:
        action.setChecked(checked)
    return action

class widgetWithMenu(object):
    loadFileArgs= ("Choose a data file", '', '*.txt')
    saveFileArgs= ("Save file as", '', '*.txt')
    headerText = 'Edit'
    menuTag = '&File'
    whereDockable   = QtCore.Qt.AllDockWidgetAreas
    waitCondition = None
    latency = 8
    counted =0
    fileName = None
    minimumWidth = None
    minimumHeight = None

    def __init__(self):  # provider being phaed out!
        self.menu = QtGui.QMenu(self.menuTag)
        if not self.menuItems():
            return
        for tag, shortcut, func in self.menuItems():
            action = myQAction(tag, shortcut=shortcut, triggered=func)
            self.menu.addAction(action)
        Common.abcraft.menuBar().addMenu(self.menu)
        #QtGui.QMainWindow().menuWidget ().addMenu(self.menu)

    def menuItems(self):
        return [
        ]
            
    def changeMyFont(self):
        font, ok = QtGui.QFontDialog.getFont(self.font(),self)
#           font, ok = QtGui.QFontDialog.getFont(QtGui.QFont(self.toPlainText()), self)
        if ok:
            self.setFont(font)
            #self.textCursor().setCharFormat.document().setFont(font.key())
            #self.fontLabel.setFont(font)
         
