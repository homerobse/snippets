## about `setup.py` and its relation to pip

https://stackoverflow.com/a/39811884/1273751

https://stackoverflow.com/a/1472014/1273751
`pip install .`

### relation to `pip`

Qa: Can we do `pip install .` instead of `python setup.py install`? And if we want it to be editable, would it be `pip install -e .` instead of `python setup.py develop` Asked: https://stackoverflow.com/questions/1471994/what-is-setup-py#comment140713429_39811884

## `find_packages` function
It returns a list of strings with the names of the packages (folders that contain `__init__.py`) identified in the folder structure, e.g. ["foo", "bar"].
If the package is inside a folder in the current working directory, use `find_packages(where='folder_name')`.
https://stackoverflow.com/a/54430803/1273751

## Other information about packaging in Python

https://packaging.python.org/en/latest/tutorials/packaging-projects/

distribution files are generated after the following commands are run:
`python3 -m pip install --upgrade build`
`python3 -m build`

> "Tools like pip and build do not actually convert your sources into a distribution package (like a wheel); that job is performed by a build backend" (e.g. hatchling or setuptools).

twine is a package to upload distribution files to PyPI servers.


## Open question
* what is a wheel?