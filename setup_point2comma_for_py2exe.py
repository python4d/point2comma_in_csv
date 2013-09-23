from distutils.core import setup
import py2exe

setup(
      options = {"py2exe": {
                            "compressed": 1,
                             "bundle_files": 1,
                             'dll_excludes': [ "w9xpopen.exe" ]
                             } },
      console=['point2comma_in_csv.py'])