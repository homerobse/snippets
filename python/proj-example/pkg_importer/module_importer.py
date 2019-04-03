import sys

if len(sys.argv)>1 and sys.argv[1]=='--with_insert':
    # through bash it only works if I include this:
    dir_path = "/home/homero/dphil/snippets/python/proj-example"
    sys.path.insert(0, dir_path)

print('module_importer.py pythonpath state:')
print(sys.path)

# all the options below work fine

# from pkg_imported.module_imported import useful_func
# useful_func()

import pkg_imported.module_imported
pkg_imported.module_imported.useful_func()

# from pkg_imported import module_imported
# module_imported.useful_func()
