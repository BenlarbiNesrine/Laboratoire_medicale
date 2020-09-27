#!c:\users\dell\desktop\django\mysite\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'search-cli==0.1.1','console_scripts','search_gui'
__requires__ = 'search-cli==0.1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('search-cli==0.1.1', 'console_scripts', 'search_gui')()
    )
