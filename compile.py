from distutils.core import setup
import py2exe
 
setup(windows=['JustCopy.py'], options={"py2exe": {"includes": ["sip", "PyQt4.QtGui"]}})