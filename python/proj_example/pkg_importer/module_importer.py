import sys
from pathlib import Path

if len(sys.argv)>1 and sys.argv[1]=='--with_insert':
    # through bash it only works if I add the root folder to PYTHONPATH:
    dir_path = str(Path(__file__).resolve().parent.parent)
    sys.path.insert(0, dir_path)

print('module_importer.py pythonpath state:')
print(sys.path)

# all the options below work fine
# this works when run as a python module (no need for insert, because `$python -m pkg_importer.module_importer` will have the root folder in PYTHONPATH)

# from pkg_imported.module_imported import useful_func
# useful_func()

import pkg_imported.module_imported
pkg_imported.module_imported.useful_func()

# from pkg_imported import module_imported
# module_imported.useful_func()

print("Good, managed to import the module and run the function.")

## this doesn't work:
print("\nattempt relative import of root module:")
from .. import root_module