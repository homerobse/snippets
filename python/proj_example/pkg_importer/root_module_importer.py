# with absolute import:
#import proj_example.pkg_imported.module_imported
#proj_example.pkg_imported.module_imported.useful_func()

# with relative imports:
from .. import pkg_imported
## this doesn't work:
#import pkg_imported.module_imported  # ModuleNotFoundError: No module named 'pkg_imported'
#pkg_imported.module_imported.useful_func()

##but this does
from ..pkg_imported import module_imported
module_imported.useful_func()

print("Good, managed to import the module and run the function.")

print("\nattempt relative import of root module:")
from .. import root_module
