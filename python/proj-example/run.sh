echo '# Running ./base.py'

python base.py

echo '# Running ./pkg_imported/module_local_importer.py'

python pkg_imported/module_local_importer.py

echo '# Running ./pkg_importer/module_importer.py without insert'

python pkg_importer/module_importer.py

echo '# Running ./pkg_importer/module_importer.py with insert'

python pkg_importer/module_importer.py --with_insert
