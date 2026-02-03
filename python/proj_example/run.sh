echo '# Running ./base.py'

python base.py

echo
echo '# Running ./pkg_imported/module_local_importer.py'

python pkg_imported/module_local_importer.py

echo
echo '# Running ./pkg_importer/module_importer.py without inserting the root to PYTHONPATH'

python pkg_importer/module_importer.py

echo
echo '# Running ./pkg_importer/module_importer.py with insert of the root path to PYTHONPATH'

python pkg_importer/module_importer.py --with_insert

echo
echo '# Running python -m pkg_importer.module_importer (no explicit change to PYTHONPATH)'
# will have error for relative import because it can't do an import of a module above what python was called
# ImportError: attempted relative import beyond top-level package
python -m pkg_importer.module_importer

echo
echo '# Running python -m pkg_importer.module_importer (with insert of the root path to PYTHONPATH)'
# note that the root directory will appear twice in PYTHONPATH

python -m pkg_importer.module_importer --with_insert

echo
echo '### Imports mentioning proj_example ###'
echo '# Running python -m proj_example.pkg_importer.module_importer (no explicit change to PYTHONPATH) from inside proj_example folder'
python -m proj_example.pkg_importer.module_importer

echo
echo '# Running python -m proj_example.pkg_importer.root_module_importer (no explicit change to PYTHONPATH) but from the directory above proj_example'
cd ..
echo 'changed directory to'
pwd

python -m proj_example.pkg_importer.root_module_importer

echo
echo '# Running ./proj_example/pkg_importer/root_module_importer (no explicit change to PYTHONPATH) but from the directory above proj_example'
# this doesn't work because the PYTHONPATH doesn't have the proj_example folder
# ModuleNotFoundError: No module named 'proj_example'
python proj_example/pkg_importer/root_module_importer.py

echo
echo '### Imports directly in the module_importer folder ###'
echo '# Running python -m module_importer (from pkg_importer folder, no explicit change to PYTHONPATH)'
cd proj_example/pkg_importer
echo 'changed directory to'
pwd
python -m module_importer
# doesn't work because the PYTHONPATH doesn't have the folder pkg_imported
# ModuleNotFoundError: No module named 'pkg_imported'

echo
echo '# Running python -m module_importer (from pkg_importer folder, but with insert of the root path to PYTHONPATH)'
python -m module_importer --with_insert
# works fine, just can't do the relative import, as expected
